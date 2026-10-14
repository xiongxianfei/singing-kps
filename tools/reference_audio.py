#!/usr/bin/env python3
"""Build/check original reference tones; Python standard library plus FFmpeg.

The 1-cent check is an asset-generation tolerance, NOT a learner pass mark.
Nothing here records or assesses a human voice. Learners need only the MP3s.
"""
from __future__ import annotations
import argparse
import array
import hashlib
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / 'media/reference-pitches'
NOTES = {'a2': 45, 'c3': 48, 'e3': 52, 'a3': 57, 'c4': 60, 'e4': 64, 'a4': 69}
RATE = 16000
SOURCE_SECONDS = 1.6
FADE_SECONDS = 0.05


def run_ffmpeg(args: list[str], data: bytes | None = None) -> bytes:
    if not shutil.which('ffmpeg'):
        raise RuntimeError('FFmpeg is required for maintainer audio checks; not for learner playback.')
    result = subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', *args],
                            input=data, capture_output=True, timeout=30)
    if result.returncode:
        raise RuntimeError(result.stderr.decode('utf-8', errors='replace'))
    return result.stdout


def pcm_bytes(frequency: float) -> bytes:
    count = round(RATE * SOURCE_SECONDS)
    values = array.array('h')
    for i in range(count):
        phase = 2 * math.pi * frequency * i / RATE
        envelope = min(1.0, i / (RATE * FADE_SECONDS), (count - 1 - i) / (RATE * FADE_SECONDS))
        value = 0.14 * envelope * (math.sin(phase) + 0.3 * math.sin(2*phase) + 0.15 * math.sin(3*phase))
        values.append(round(32767 * value))
    if sys.byteorder != 'little':
        values.byteswap()
    return values.tobytes()


def measure(path: Path) -> dict[str, float]:
    data = run_ffmpeg(['-i', str(path), '-f', 's16le', '-ar', str(RATE), '-ac', '1', 'pipe:1'])
    values = array.array('h')
    values.frombytes(data)
    if sys.byteorder != 'little':
        values.byteswap()
    if not values:
        raise ValueError(f'{path.name}: empty decoded audio')
    xs = [v / 32768.0 for v in values]
    central = xs[len(xs)//4:3*len(xs)//4]
    crossings = [i - 1 - central[i-1]/(central[i]-central[i-1])
                 for i in range(1, len(central)) if central[i-1] <= 0 < central[i]]
    if len(crossings) < 10:
        raise ValueError(f'{path.name}: insufficient stable cycles')
    frequency = (len(crossings)-1) * RATE / (crossings[-1]-crossings[0])
    return {'decoded_seconds': len(xs)/RATE, 'measured_hz': frequency,
            'peak': max(abs(v) for v in xs), 'dc': sum(xs)/len(xs),
            'rms': math.sqrt(sum(v*v for v in central)/len(central))}


def build() -> None:
    BANK.mkdir(parents=True, exist_ok=True)
    assets = []
    for name, midi in NOTES.items():
        hz = 440 * 2 ** ((midi-69)/12)
        path = BANK / (name + '.mp3')
        run_ffmpeg(['-y', '-f', 's16le', '-ar', str(RATE), '-ac', '1', '-i', 'pipe:0',
                    '-c:a', 'libmp3lame', '-b:a', '16k', '-write_xing', '0',
                    '-id3v2_version', '0', '-map_metadata', '-1', str(path)], pcm_bytes(hz))
        assets.append({'file': path.name, 'midi': midi, 'frequency_hz': hz,
                       'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
    manifest = {'format': 1, 'origin': 'Original mathematical synthesis; no voice or third-party samples',
                'tuning': '12-tone equal temperament; A4 = 440 Hz', 'source_sample_rate_hz': RATE,
                'channels': 1, 'encoding': 'MP3; libmp3lame; 16 kbit/s',
                'source_tone_seconds': SOURCE_SECONDS, 'linear_fade_seconds': FADE_SECONDS,
                'harmonic_amplitudes': [0.14, 0.042, 0.021],
                'duration_note': 'MP3 encoder padding may extend playback beyond source tone duration',
                'encoder_version': subprocess.check_output(['ffmpeg', '-version'], text=True).splitlines()[0],
                'assets': assets}
    (BANK/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n', encoding='utf-8')


def check() -> None:
    manifest = json.loads((BANK/'manifest.json').read_text(encoding='utf-8'))
    expected = {name+'.mp3' for name in NOTES}
    if {p.name for p in BANK.glob('*.mp3')} != expected:
        raise ValueError('Missing or unexpected MP3 in reference bank')
    entries = manifest['assets']
    if len(entries) != len(expected) or {e['file'] for e in entries} != expected:
        raise ValueError('Manifest coverage differs from specified bank')
    reports = []
    for entry in entries:
        path = BANK / entry['file']
        target = 440 * 2 ** ((NOTES[path.stem]-69)/12)
        if entry['midi'] != NOTES[path.stem] or abs(entry['frequency_hz']-target) > 1e-8:
            raise ValueError(f'{path.name}: target metadata mismatch')
        if hashlib.sha256(path.read_bytes()).hexdigest() != entry['sha256']:
            raise ValueError(f'{path.name}: checksum mismatch')
        result = measure(path)
        cents = 1200 * math.log2(result['measured_hz']/target)
        if not 1.6 <= result['decoded_seconds'] <= 1.8 or abs(cents) > 1.0:
            raise ValueError(f'{path.name}: duration or frequency check failed: {result}')
        if not 0.02 < result['rms'] < 0.25 or result['peak'] >= 0.3 or abs(result['dc']) > 0.005:
            raise ValueError(f'{path.name}: amplitude or DC check failed: {result}')
        reports.append({'file': path.name, 'error_cents': round(cents, 5),
                        'decoded_seconds': result['decoded_seconds'], 'peak': round(result['peak'], 5)})
    print(json.dumps({'ok': True, 'assets': len(reports), 'checks': reports,
                      'scope': 'Synthetic asset integrity only; no learner or device playback assessment'}, indent=2))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', action='store_true', help='Regenerate bank and manifest before checking')
    args = parser.parse_args()
    try:
        if args.build:
            build()
        check()
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.SubprocessError) as exc:
        print(f'Audio check failed: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
