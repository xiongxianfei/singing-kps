---
id: "sing:model:rhythm-and-meter"
type: "model"
version: "0.1.0"
language: "KPS 9.x"
status: "draft"
reviewed: null
uses_concepts: ["sing:concept:beat-and-rhythm"]
uses_models: ["sing:model:pitch-relationships"]
references: ["sing:reference:omt-notating-rhythm", "sing:reference:omt-simple-meter", "sing:reference:omt-compound-meter"]
basis_kind: "Selected event, pulse and metrical representation from Western music theory; constructed timelines and arithmetic"
source_alignment: [{"reference":"sing:reference:omt-notating-rhythm","relation":"definition-paraphrase","locator":"Opening discussion, Note Values and Rest Values"},{"reference":"sing:reference:omt-simple-meter","relation":"standard-model-subset","locator":"Terminology, Simple Meter and Time Signatures"},{"reference":"sing:reference:omt-compound-meter","relation":"standard-model-subset","locator":"Compound Meter and Compound Time Signatures"}]
---

# Rhythm and meter

## Key takeaway

Sound events, a recurring pulse and the grouping of that pulse are different views of musical time; silence does not remove the beat.

## Summary

This Model places sounds and rests on a timeline, relates beat positions to elapsed time, and distinguishes simple from compound grouping. Rhythm and metrical organisation share a representation here because their interaction answers the beginner's question about when an event happens. Grouping is not reduced to loudness, and a written fraction alone does not establish how a performance is heard.

## Purpose and boundary

The Model supports interpreting the [first-session pattern](../practices/first-singing-session.md) and explaining why counting subdivisions is not always the same as counting beats. It uses selected Western metrical conventions. Reading notation is optional: the worked grids can be understood as timed slots.

Rubato, swing, tuplets, free rhythm, polyrhythm, detailed beat perception and stylistic timing need further accounts. The representation is descriptive and mathematical, not a neural mechanism or a prescription to sing mechanically.

## Components and variables

| Component | Representation | Meaning |
|---|---|---|
| Event | Start position b and duration d, in declared beat units; sound or rest | What occupies a span of time |
| Pulse | Recurring reference positions | Where a listener or performer locates beats even when no new sound begins |
| Tempo | B beats per minute, with the beat unit stated | How fast the chosen pulse recurs |
| Subdivision | Parts within a beat | Two equal parts in a simple beat or three in a compound beat in the examples |
| Meter | Recurring beat groups and their relative positions | A grouping structure, not a measurement of each sound's volume |
| Elapsed time | Seconds relative to a stated starting point | A performance-time coordinate rather than an additional note value |

A rest is an intended interval without the relevant sounded event. Another voice or accompaniment could still sound. A note sustained across a beat boundary need not restart there. See [Beat and rhythm](../concepts/beat-and-rhythm.md) for the shared vocabulary.

## Relationships and rules

With a constant tempo and origin b = 0 at time zero, **time in seconds = 60 × b / B**. An event lasting d beats lasts **60 × d / B** seconds. The origin is a counting convention; b = 0 is the first beat's start, not a missing beat. For changing tempo a constant multiplier is insufficient.

Metric grouping adds structure to this timeline. Simple and compound describe division of a beat; duple, triple and quadruple describe the number of beats in a group. These are different axes. A structurally strong position may be performed softly; metrical accent is not identical to measured loudness.

The [simple-meter account](../references/open-music-theory-undated-simple-meter.md) and [compound-meter account](../references/open-music-theory-undated-compound-meter.md) support this distinction. The timelines and calculations below are authored examples, not copied scores or recordings.

## Worked example of three sounds and a rest

Take four quarter-note beats at 120 quarter-note beats per minute. Each beat lasts 0.5 seconds. The first Practice's pattern can be represented without choosing sung pitches:

| Count | Beat position b | Time in seconds | Voice event in this constructed pattern |
|---|---|---|---|
| 1 | 0 | 0.0 | Sound for one beat |
| 2 | 1 | 0.5 | Sound for one beat |
| 3 | 2 | 1.0 | Sound for one beat |
| 4 | 3 | 1.5 | Rest for one beat |
| Next 1 | 4 | 2.0 | Next group would begin |

The fourth beat exists even though the voice rests. Replacing the first two separate sounds with one two-beat sound would change the rhythm while preserving the pulse and group length. A correct pitch on every sounded event would not establish correct timing.

This is an explanatory clock, not a replacement for the Practice's comfortable pace. The Model introduces no new repetition dose, metronome requirement or vocal attempt.

## Worked example of six slots with two different groupings

Suppose six equally long eighth-note slots occupy 1.5 seconds. Each slot lasts 0.25 seconds. Compare these declared organisations:

| Representation | Slot grouping | Main beats | Main beat duration | Tempo expressed in that beat unit |
|---|---|---|---|---|
| 3/4, simple triple | 1-2 / 3-4 / 5-6 | Three quarter-note beats | 0.50 seconds | 120 quarter-note beats per minute |
| 6/8, compound duple | 1-2-3 / 4-5-6 | Two dotted-quarter-note beats | 0.75 seconds | 80 dotted-quarter-note beats per minute |

The six slots and bar duration agree, while beat grouping and the number attached to the beat unit differ. Therefore saying only 120 BPM is incomplete when comparing these interpretations. It also follows that six eighth notes do not automatically mean six main beats.

Without phrasing, accent, context or a declared meter, an evenly spaced sequence may not tell the listener which grouping was intended. That is a limit on inference, not a failure of the slot arithmetic. The example describes common conventions, not every performance of those signatures.

## Interfaces

| Connected explanation | Information or constraint exchanged | What is not inferred |
|---|---|---|
| [Pitch relationships](pitch-relationships.md) | A pitch or interval pattern can be assigned to timed events | Correct contour does not establish timing; correct timing does not establish pitch |
| [Tonal organisation](tonal-organisation.md) | Scale-degree events also occur at metric positions | Metric position alone does not identify tonic or harmonic function |
| [Articulation](articulatory-speech-sounds.md) and [Text setting](../docs/body-of-knowledge-outline.md#text-setting) | Syllables, consonants and vowels have transitions that need placement | The start of a scored note does not automatically specify every articulator's onset |
| [Respiratory phonatory system](respiratory-phonatory-system.md) | Durations and gaps constrain demands on voiced sound | A rest or bar line is not automatically a required breath |
| [Auditory vocal matching](auditory-vocal-pitch-matching.md) | Event order and time windows delimit which attempt is compared | A pitch error cannot explain every missed entry |
| [Ensemble coordination](../docs/body-of-knowledge-outline.md#singing-with-others-and-presenting) | Shared timing references can organise starts and endings | This is not yet a model of interpersonal synchronisation or conducting cues |

## Assumptions and unresolved questions

The equations assume constant tempo, explicit beat units and precisely defined event boundaries. Actual attacks, releases and expressive timing can be gradual or ambiguous. Grouping may be inferred rather than given, and other musical traditions require their own accounts.

The open questions for a real example include the intended pulse, expressive timing and which sound boundary is being judged. No learner rhythm accuracy, automatic beat-extraction capability or learning benefit is established here.

## Interpretation check and source basis

Could the pulse continue through a rest? Yes. Could equal-length bars have different main-beat tempi? Yes, if their beat units differ as in the six-slot example. Does every loud event identify a downbeat? No.

The selected [rhythm](../references/open-music-theory-undated-notating-rhythm.md), [simple-meter](../references/open-music-theory-undated-simple-meter.md) and [compound-meter](../references/open-music-theory-undated-compound-meter.md) records identify the underlying accounts and inspection limits. Simple and compound chapter text was rechecked through the credited republication; no source songs or listening examples were analysed.
