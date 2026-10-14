"""One-off guarded editorial integration; removed before the final PR tree.

The Markdown changes are authored below. This is not an outline generator or
an automatic source-review procedure. The assistant reviewed the explanations,
source scope and affected receiving summaries before permitting snapshot refresh.
"""
from pathlib import Path
import json
import math
import re
import subprocess

BASE = 'f655562d1411ba29a7845b104c0c02e1d4a1c5af'
ROOT = Path('.')

def read(path):
    return (ROOT / path).read_text(encoding='utf-8')

def write(path, text):
    (ROOT / path).write_text(text.rstrip() + '\n', encoding='utf-8')

def replace_once(text, old, new):
    if text.count(old) != 1:
        raise RuntimeError('Expected exactly one editorial target: ' + old[:110])
    return text.replace(old, new, 1)

def set_meta(text, key, value):
    front, body = text[4:].split('\n---\n', 1)
    pattern = re.compile('^' + re.escape(key) + r': .*$', re.M)
    entry = key + ': ' + json.dumps(value, ensure_ascii=False)
    if pattern.search(front):
        front, count = pattern.subn(lambda m: entry, front)
        assert count == 1
    else:
        front += '\n' + entry
    return '---\n' + front + '\n---\n' + body

# Preserve the successful pitch Model rather than replacing its representation.
pitch = read('models/pitch-relationships.md')
assert 'version: "0.1.0"' in pitch
pitch = set_meta(pitch, 'version', '0.2.0')
pitch = set_meta(pitch, 'uses_models', ['sing:model:auditory-vocal-pitch-matching', 'sing:model:tonal-organisation', 'sing:model:rhythm-and-meter', 'sing:model:source-filter-voice-production'])
pitch = replace_once(pitch, '## Interfaces and interpretation limits', '''## Worked interface with transposition

Take the constructed pair A3 at 220 Hz and E4 at about 329.63 Hz. Raising both by three equal-tempered semitones multiplies both frequencies by `2^(3/12)`, approximately 1.18921. Their new targets are C4 at about 261.63 Hz and G4 at about 392.00 Hz. The pair remains seven semitones apart; its absolute heights and pitch classes have changed.

This is an application of the ratio rule already defined above. It explains one invariant that the [major-scale tonal Model](tonal-organisation.md) uses when context and a whole pattern are transposed. It does not choose a comfortable key for a singer. The [rhythm and meter Model](rhythm-and-meter.md) can attach either pair to the same event times: pitch transposition alone does not change duration.

## Interfaces and interpretation limits''')
pitch = replace_once(pitch, '| Rhythmic organisation and text setting | Pitch relationships can be combined with event timing and syllable placement | This Model does not specify rhythm, lyrics or their coordination |', '| [Rhythm and meter](rhythm-and-meter.md) and [text setting](../docs/body-of-knowledge-outline.md#text-setting) | Pitch relationships are assigned to event times; later accounts must specify syllable placement | A direction sequence loses duration and interval size; timing is not derived from pitch |')
pitch = replace_once(pitch, '| Tonal organisation | Identifies pitches and distances available to a contextual account | A class name does not identify tonic, scale degree or expressive role |', '| [Tonal organisation](tonal-organisation.md) | Provides pitch classes and intervals; receives the declared context needed for scale-degree roles | Class membership does not by itself identify tonic, degree, expressive role or a unique octave |\n| [Source and filter](source-filter-voice-production.md) | A stable source fundamental can supply a physical pitch coordinate while spectral shaping describes a different property | A strong harmonic is not automatically the fundamental, and a frequency value does not identify vowel or vocal configuration |')
write('models/pitch-relationships.md', pitch)

# Maintain every existing topic and heading; update only located coverage cells.
outline = read('docs/body-of-knowledge-outline.md')
old_headings = re.findall(r'^## (.+)$', outline, re.M)
topics = ['Respiration', 'Phonation', 'Vocal tract resonance', 'Articulation', 'Pitch relationships', 'Rhythmic organisation', 'Metrical organisation', 'Tonal organisation', 'Text setting', 'Auditory vocal pitch matching', 'Vocal instrument and individual variation', 'Vocal care and comfortable use', 'Registration', 'Range and tessitura', 'Voice classification', 'Diction and meaning', 'Dynamics and vibrato', 'Repertoire selection', 'Phrasing', 'Style and musical context', 'Singing with others and presenting', 'Melody harmony and musical form', 'Learning and feedback', 'Notation and sight singing']
assert len(topics) == 24 and all(old_headings.count(t) == 1 for t in topics)
outline = set_meta(outline, 'package_version', '0.3.0')
outline = replace_once(outline, '## Purpose and scope', '''The [Model architecture](model-architecture.md) maps every topic to current explanations and remaining questions. Its first implemented groups contain seven complementary Models of physical production, articulation, musical coordinates and auditory-vocal matching. These groups do not replace this directly named topic outline or make every topic complete.

## Purpose and scope''')
outline = replace_once(outline, '## Respiration', '''**Introductory explanation** below means that the stated local distinction has a self-contained representation and worked case, checked editorially. It does not mean the entire topic is complete, a learner can perform it, or the account has received independent scientific approval. Broader requirements remain Partial even when a narrower explanation is sufficient.

## Respiration''')
updates = {
    'Body and breath coordination': '**Partial:** [Respiratory phonatory system](../models/respiratory-phonatory-system.md) explains pressure, flow, respiratory movement and a constructed duration budget. Individual breath coordination, posture/support cues and phrase strategies remain undeveloped; the Model prescribes no breathing target.',
    'Phonation and sound continuity': '**Partial:** the [production Model](../models/respiratory-phonatory-system.md) explains qualitative conditions for initiating, maintaining and ending self-oscillation. Detailed onset strategies, tissue dynamics and individual coordination remain outside this subset.',
    'Source and vocal-tract shaping': '**Introductory explanation:** [Source and filter](../models/source-filter-voice-production.md) relates excitation, response and output with worked spectra and coupling limits. Detailed nonlinear acoustics and individual parameter estimation remain partial.',
    'Vowels and tone quality': '**Partial:** [Articulatory speech sounds](../models/articulatory-speech-sounds.md) and [source-filter acoustics](../models/source-filter-voice-production.md) connect configuration with shaping while distinguishing vowel height from pitch. Language-specific vowels, dynamic changes and perception remain incomplete.',
    'Vowels and consonants': '**Introductory explanation:** the [articulatory Model](../models/articulatory-speech-sounds.md) distinguishes selected place, manner, voicing, vowel and nasal-route features with examples. Full inventories, coarticulation and language-specific instruction remain partial.',
    'Pitch height and pitch class': '**Introductory explanation:** [Pitch](../concepts/pitch.md) and the refined [pitch Model](../models/pitch-relationships.md) distinguish height, class and octave with worked comparisons. A full naming system and pitch-perception account remain outside the subset.',
    'Octaves and interval distance': '**Partial:** the refined [pitch Model](../models/pitch-relationships.md) explains ratio distance, contour loss and transposition invariance. Full interval spelling, alternative tunings and perceptual discrimination still need accounts.',
    'Pulse and tempo': '**Introductory explanation:** [Rhythm and meter](../models/rhythm-and-meter.md) relates beat positions to seconds with an explicit beat unit and constant-tempo example. Expressive timing and an observed learner performance remain outside this explanation.',
    'Durations and rests': '**Introductory explanation:** the [rhythm and meter Model](../models/rhythm-and-meter.md) represents event spans, a rest within a continuing pulse and selected subdivisions. Complex rhythms, tuplets and song-level use remain partial.',
    'Meter and grouping': '**Partial:** [Rhythm and meter](../models/rhythm-and-meter.md) compares simple-triple and compound-duple grouping with a six-slot case and [compound-meter sourcing](../references/open-music-theory-undated-compound-meter.md). Phrasing, ambiguous metre, changing groups and broader traditions remain incomplete.',
    'Intervals and tonal context': '**Partial:** [Pitch relationships](../models/pitch-relationships.md) supplies distances and [Tonal organisation](../models/tonal-organisation.md) adds a declared major-scale context and transposition. Fuller interval naming, musical expectation mechanisms and repertoire transfer remain missing.',
    'Tonal centre and scale degrees': '**Introductory explanation:** the [major-scale tonal Model](../models/tonal-organisation.md) distinguishes a class from its contextual degree and follows a transposed fragment. Minor/modal accounts, key inference and perceptual expectation remain partial.',
    'Intonation and listening feedback': '**Partial:** [Intonation](../concepts/intonation.md), the [comparison Method](../methods/reference-pitch-comparison.md) and refined [auditory vocal Model](../models/auditory-vocal-pitch-matching.md) distinguish acoustic/categorical targets, action and uncertain evidence. Phrase-level expressive intonation and individual causal assessment remain unimplemented.',
    'The vocal instrument': '**Partial:** the [production](../models/respiratory-phonatory-system.md), [source-filter](../models/source-filter-voice-production.md) and [articulatory](../models/articulatory-speech-sounds.md) Models explain complementary functions and interfaces. Individual anatomy, development and variation still require further accounts.'
}
lines = outline.splitlines()
for topic, final_cell in updates.items():
    indices = [i for i, line in enumerate(lines) if line.startswith('| ' + topic + ' |')]
    if len(indices) != 1:
        raise RuntimeError('Coverage row not uniquely located: ' + topic)
    i = indices[0]
    cells = lines[i].split('|')
    assert len(cells) == 6, (topic, cells)
    cells[-2] = ' ' + final_cell + ' '
    lines[i] = '|'.join(cells)
outline = '\n'.join(lines)
outline = replace_once(outline, 'A complete respiratory Model is missing.', 'The [introductory production Model](../models/respiratory-phonatory-system.md) now explains a bounded pressure/flow and vibration account; individual phrase coordination remains a gap.')
outline = replace_once(outline, '## Optional detailed illustrations', '''The first Model groups additionally use selected [OpenStax respiratory mechanics](../references/betts-2022-process-of-breathing.md), [singing mechanics](../references/wolfe-undated-singing-mechanics.md), a [physical source-filter experiment](../references/wolfe-2016-measured-source-filter.md), [articulatory phonetics](../references/anderson-2022-speech-articulation.md) and [compound metre](../references/open-music-theory-undated-compound-meter.md). Their records state actual inspected portions, mirrors and nonclaims. The architecture is authored integration, not an externally prescribed taxonomy. NATS and Trinity retain their existing limited roles; no new clinical or teaching effectiveness claim is added.

## Optional detailed illustrations''')
assert re.findall(r'^## (.+)$', outline, re.M) == old_headings
write('docs/body-of-knowledge-outline.md', outline)

readme = read('README.md')
readme = set_meta(readme, 'package_version', '0.3.0')
readme = replace_once(readme, '## Knowledge coverage', '''## Model architecture

The [Singing Model architecture](docs/model-architecture.md) connects all 24 outline topics while distinguishing implemented explanations from remaining gaps. Seven Models form the first groups: physical production and acoustic shaping; speech-sound articulation; pitch, rhythm/metre and major-scale context; and auditory-vocal matching. The [collection and boundary decisions](docs/model-architecture.md#current-model-collection-and-boundary-decisions) give each entry point and explain why topics are combined or separated.

The two existing pitch Models are refined rather than replaced. Worked cases connect quantities and decisions without prescribing new vocal exercises. Text setting, individual/register and song demands, broader performance, and durable learning remain development questions, not completed coverage. A beginner does not have to study every Model before using the existing Practices.

## Knowledge coverage''')
write('README.md', readme)

pub = json.loads(read('publication.json'))
assert pub['kps_language'] == '9.x' and pub['minimum_validator'] == '9.1.0'
assert pub['core_source_commit'] == '6a6e7aedc24581769fad435f4943856c1060e02a'
pub['version'] = '0.3.0'
pub['scope'] = 'Absolute beginner: two comfortable listening and singing Practices with explanatory Models of production, articulation, musical coordinates and auditory-vocal matching; broader coverage remains partial'
write('publication.json', json.dumps(pub, ensure_ascii=False, indent=2))

simple = read('references/open-music-theory-undated-simple-meter.md')
assert '## Model development inspection' not in simple
simple = set_meta(simple, 'version', '0.1.1')
simple += '''

## Model development inspection

On 2026-10-14, Terminology, Simple Meter and Time Signatures were rechecked through the [credited LibreTexts republication](https://human.libretexts.org/Bookshelves/Music/Music_Theory/Open_Music_Theory_2e_%28Gotham_et_al.%29/01%3A_Fundamentals/1.09%3A_Simple_Meter_and_Time_Signatures). The original host returned 403 in this recheck. The earlier inspection remains recorded above; the mirror is the same source family. The selected text supports the new rhythm/metre representation, not automatic beat perception or a learner outcome. No source recordings or scores were evaluated or copied in this recheck.
'''
write('references/open-music-theory-undated-simple-meter.md', simple)
major = read('references/open-music-theory-undated-major-scales.md')
major = set_meta(major, 'version', '0.1.1')
major = replace_once(major, 'The inspected major-scale account supports coverage of scales, tonic and scale-degree naming in the singing outline. It does not supply a complete local tonal Model or evidence for a beginner exercise.', 'The inspected major-scale account supports scales, tonic and degree relationships in the singing outline and the selected major-scale tonal Model. It is not a complete tonal theory or evidence for a beginner exercise.')
assert '## Model development inspection' not in major
major += '''

## Model development inspection

The named major-scale and degree sections were rechecked on 2026-10-14 through the same credited republication for the local tonal Model. The whole/half-step pattern and contextual roles support its coordinate representation; the two-context and transposition cases are authored applications. The original host remained unavailable. No source melody, learner result, minor/modal theory or experimentally established expectation mechanism is claimed.
'''
write('references/open-music-theory-undated-major-scales.md', major)

# Check constructed calculations independently of source and structural claims.
assert math.isclose(0.12 * 2, 0.24) and math.isclose(0.12 * 4, 0.48)
assert math.isclose(1 / 200, 0.005)
source = [1.0, 0.5, 0.25]
assert [a*b for a,b in zip(source, [1.0, 0.5, 2.0])] == [1.0, 0.25, 0.5]
assert [a*b for a,b in zip(source, [1.0, 1.0, 0.5])] == [1.0, 0.5, 0.125]
assert 0.25 * 2 == 0.5 * 1
assert [60*b/120 for b in range(5)] == [0, 0.5, 1.0, 1.5, 2.0]
assert math.isclose(6*0.25, 3*0.5) and math.isclose(6*0.25, 2*0.75)
assert 60/0.5 == 120 and 60/0.75 == 80
steps = [2, 2, 1, 2, 2, 2, 1]
assert [sum(steps[:i]) for i in range(7)] == [0, 2, 4, 5, 7, 9, 11]
assert (0 + 9) % 12 == (9 + 0) % 12 == 9
assert [p + 2 for p in [0,2,4]] == [2,4,6]
f1, f2 = 220, 220 * 2**(7/12)
factor = 2**(3/12)
assert math.isclose(12*math.log2((f2*factor)/(f1*factor)), 7)
assert round(f1*factor, 2) == 261.63 and round(f2*factor, 2) == 392.00

model_paths = sorted(p.as_posix() for p in Path('models').glob('*.md'))
assert len(model_paths) == 7
for p in model_paths:
    text = read(p)
    assert '## ' in text and 'worked' in text.lower() and 'interface' in text.lower()
    assert 'source_alignment:' in text and 'status: "draft"' in text
arch = read('docs/model-architecture.md')
for topic in topics:
    fragment = topic.lower().replace(' ', '-')
    assert '(body-of-knowledge-outline.md#' + fragment + ')' in arch

# These existing inputs, actions, assets and shared rules must remain unchanged.
subprocess.run(['git','diff','--exit-code',BASE,'--','AGENTS.md','.github/workflows/validate.yml','concepts','methods','practices','media','diagrams','tools'], check=True)
subprocess.run(['git','diff','--check'], check=True)
print(json.dumps({'editorial_targets': 'matched', 'outline_topics_preserved': 24, 'model_files': 7, 'constructed_arithmetic': 'passed', 'shared_guidance_and_practices_and_assets': 'unchanged', 'review_kind': 'assistant editorial and paper self-review, not independent learner testing'}, indent=2))
