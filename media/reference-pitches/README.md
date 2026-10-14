---
language: "KPS 9.x"
status: "draft"
package_version: "0.2.0"
---

# Reference pitch audio

## Key takeaway

Choose one comfortably usable reference, not a required vocal range or a note assigned by voice type.

## Summary

Seven original synthesized MP3 tones support [Match a reference pitch](../../practices/match-a-reference-pitch.md). Use a normal phone or computer player; no microphone, installation or account is required. The tones are references to pitch height, not examples of human vocal technique.

## Play and choose

On GitHub open a file, use Raw or download if no player appears, then play the saved MP3 normally. Save desired files for offline listening. Start quietly; use normal speed and no pitch-shifting or transposition. Check mute and output selection if nothing is heard. If playback remains unclear, stop the task rather than compensate by singing louder.

| File | Pitch | Target Hz |
|---|---|---|
| [a2.mp3](a2.mp3) | A2 | 110.00 |
| [c3.mp3](c3.mp3) | C3 | 130.81 |
| [e3.mp3](e3.mp3) | E3 | 164.81 |
| [a3.mp3](a3.mp3) | A3 | 220.00 |
| [c4.mp3](c4.mp3) | C4 | 261.63 |
| [e4.mp3](e4.mp3) | E4 | 329.63 |
| [a4.mp3](a4.mp3) | A4 | 440.00 |

A3 is only a first listening suggestion. Audition lower or higher choices according to your own easy voice. None may suit you; that is a valid reason to stop. Do not sing the bank as a range test. Low notes may be less clear on small speakers. The table does not assign pitches by age, sex or voice type.

## Construction and provenance

These files contain original mathematical synthesis, not sampled voices, instruments, copyrighted performances or third-party recordings. They use twelve-tone equal temperament with A4 = 440 Hz and three harmonics with amplitudes 0.14, 0.042 and 0.021. The 16 kHz mono source lasts 1.6 seconds with 50 ms linear fades. MP3 encoding at 16 kbit/s adds padding; decoded files are about 1.69 seconds. You need not sing for their full duration.

The [manifest](manifest.json) records exact target frequencies, encoder version and SHA-256 hashes. [UNSW frequency guidance](../../references/wolfe-undated-note-frequencies.md) supports the calculations, not the timbre or exercise design. A synthetic tone's accuracy cannot establish what a specific listener hears or whether their voice matched it.

## Maintainer checks

Python standard library and FFmpeg are needed only to maintain the assets, not to use the lesson:

```bash
python tools/reference_audio.py
# Intentional rebuild only; review changed audio and manifest:
python tools/reference_audio.py --build
```

The [maintainer script](../../tools/reference_audio.py) verifies bank coverage, hashes, decoding, duration, amplitude, DC offset and central-tone frequency. Its one-cent tolerance is an engineering check on generated assets, not a learner passing score. Different encoder versions may produce different bytes; checks do not promise bit-identical rebuilding across FFmpeg versions. Device playback and independent listener usability have not been tested.
