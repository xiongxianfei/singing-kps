---
id: "sing:model:pitch-relationships"
type: "model"
version: "0.1.0"
language: "KPS 9.x"
status: "draft"
reviewed: null
references: ["sing:reference:omt-aspn", "sing:reference:unsw-note-frequencies"]
uses_concepts: ["sing:concept:pitch", "sing:concept:intonation"]
uses_models: ["sing:model:auditory-vocal-pitch-matching"]
basis_kind: "Authored representation of established pitch notation and equal-tempered frequency relationships; constructed comparisons, not learner observations"
source_alignment: [{"reference": "sing:reference:omt-aspn", "relation": "definition-paraphrase", "locator": "American Standard Pitch Notation and Pitch versus Pitch Class; ASPN and Octave Designations"}, {"reference": "sing:reference:unsw-note-frequencies", "relation": "equation-application", "locator": "Opening octave and equal-temperament explanation; frequency and logarithmic ratio equations"}]
---

# Pitch relationships

## Key takeaway

Pitch height, pitch class and interval answer different questions: two notes can share a class without matching in height, and two patterns can share a contour without sharing their intervals.

## Summary

This Model relates individual pitches, their labels, octave-equivalent classes and interval distances. It uses twelve-tone equal temperament with A4 = 440 Hz for the numerical examples. Worked comparisons distinguish unison from octave equivalence and contour from interval structure. The representation describes targets and constructed comparisons; it does not diagnose a singer, explain vocal production or establish a perceptual accuracy threshold.

## Purpose and boundary

Use this Model to answer: **What relationship does one pitch have to another, and which relationship does a task require?** It is the first focused Model within the outline's Pitch relationships subsystem. The [Pitch Concept](../concepts/pitch.md) gives the shared distinctions; the representation below connects them so the comparisons work without following links.

Here a pitch is described by its heard height and, when a reference convention is declared, its intended musical position. Frequency is a physical rate in cycles per second, or hertz. For the stable periodic reference tones used here, frequency supplies a convenient numerical coordinate. This does not equate every auditory pitch percept with a directly observed single frequency.

Tonal function, scale-degree roles, vocal registers, voice types and the mechanism of pitch perception are outside this Model. The chosen subsystem is minimal for comparing these relationships, not an assertion that it has no internally distinguishable parts.

## Components and representation

| Component | Representation and meaning | Constructed example |
|---|---|---|
| Individual pitch | A named musical position with octave placement | A3 and A4 designate different heights |
| Pitch height | Higher, lower or the same relative to another pitch | A4 is above A3 |
| Pitch class | Groups octave-related pitches; equal-tempered enharmonic spellings can name the same class | A2, A3 and A4 share class A |
| Octave designation | The number in the selected pitch-label convention | A3 has designation 3; the number is not a voice type |
| Interval | A relationship between two pitches, with direction and distance | A3 to A4 is an octave upward |
| Contour | The sequence of directions between successive pitches | Up then down omits the size of each change |

In the selected twelve-tone convention, the classes can be labelled C, C-sharp/D-flat, D, D-sharp/E-flat, E, F, F-sharp/G-flat, G, G-sharp/A-flat, A, A-sharp/B-flat and B. A slash here gives alternative spellings at the same equal-tempered position; it does not erase their possible differences in musical function. Other traditions and tuning systems need their own representation.

A full pitch label combines a note name, any accidental, and an octave designation. For the natural-note examples here, a new numbered octave starts at C. Letter names alone do not run through indefinitely increasing heights: A3 is below C4, while A4 is above C4. Instruments and voices can share a pitch label while differing in loudness and timbre, or tone colour.

## Relationships and rules

For the numerical examples, a **semitone** is one of twelve equal ratio steps in an octave. An octave doubles frequency. If a target has frequency `f`, the note `n` semitones above it has frequency `f × 2^(n/12)`; negative `n` gives a lower note. Equal musical steps use equal ratios, not equal differences in hertz.

For two stated reference frequencies, the signed distance in semitones is `12 × log2(second / first)`. Here `log2` asks which power of two gives the ratio. You do not need a calculator to understand the examples: equal frequencies give zero steps; doubling gives twelve steps; halving gives minus twelve.

| First → second | Frequency ratio | Directed distance | Relationship |
|---|---|---|---|
| A3 → A3 | 220 / 220 = 1 | 0 semitones | Unison: same height and class |
| A3 → A4 | 440 / 220 = 2 | +12 semitones | Same class, one octave higher |
| A3 → A2 | 110 / 220 = 1/2 | −12 semitones | Same class, one octave lower |
| A3 → E4 | Approximately 329.63 / 220 | Approximately +7 semitones | Higher, different class, less than an octave |
| A3 → C4 | Approximately 261.63 / 220 | Approximately +3 semitones | Higher, different class, a smaller distance |

These are intended reference values, rounded where shown. Traditional interval names and spelling distinctions require further explanation; a semitone count does not supply the whole interval-naming system.

The compact structure is: **individual pitches have heights and labels; octave equivalence groups them into classes; pairs define intervals; sequences of interval directions define contour.** Keeping only class loses octave placement. Keeping only contour loses interval size and starting height.

## Worked comparison with a target

Suppose the chosen target is A3 at 220 Hz. The following are constructed alternatives, not measurements of a learner:

| Proposed result | What agrees with the target | What differs | Task interpretation |
|---|---|---|---|
| A3 at 220 Hz | Height and class | No pitch difference in this ideal example | Meets the stated unison relationship |
| A4 at 440 Hz | Class A | Height is one octave above | Does not meet the unison relationship |
| A2 at 110 Hz | Class A | Height is one octave below | Does not meet the unison relationship |
| E4 at about 329.63 Hz | Neither height nor class | About seven semitones above | A different target relationship |

An A-only tuner display cannot distinguish the first three cases. Octave information, frequency or a reliable auditory comparison is needed. Octave singing can be appropriate in another musical context; the conclusion follows from this task's request for the same height.

Changing an uncomfortable reference to a suitable one changes the target. It is not evidence that the original target was matched. The [matching Practice](../practices/match-a-reference-pitch.md) owns reference selection and its existing comfort boundaries; this Model supplies no range-extension exercise.

## Worked comparison of two contours

Compare the constructed patterns **A3 → E4 → A3** and **A3 → C4 → A3**. Both begin at A3, rise, and return. The first rises about seven semitones; the second rises about three. They share contour and starting height, but not interval structure. Describing either as up then down therefore does not establish reproduction of the other melody.

The first-session contour task deliberately leaves exact pitches and intervals unspecified. A correct direction pattern and a same-height reference match are different outcomes. Optional listening examples are the existing [A3](../media/reference-pitches/a3.mp3), [E4](../media/reference-pitches/e4.mp3) and [C4](../media/reference-pitches/c4.mp3) files, played separately; listening does not require singing those notes.

## Interfaces and interpretation limits

| Connected explanation | What this Model contributes | What remains outside it |
|---|---|---|
| [Auditory-vocal pitch matching](auditory-vocal-pitch-matching.md) | Describes the target relationship to compare | Perceiving, remembering, producing and correcting a note are different functions; a mismatch does not locate its cause |
| [Intonation](../concepts/intonation.md) | Supplies a reference relationship for a comparison | A human attempt can vary over time, and measurement or listening can remain uncertain; no universal passing tolerance is declared |
| Rhythmic organisation and text setting | Pitch relationships can be combined with event timing and syllable placement | This Model does not specify rhythm, lyrics or their coordination |
| Tonal organisation | Identifies pitches and distances available to a contextual account | A class name does not identify tonic, scale degree or expressive role |

A stable synthetic reference is not a model of a human timbre or a guarantee of accurate playback. The arithmetic does not establish a listener's discrimination, a safe pitch range, healthy technique or learning effectiveness. An uncertain real comparison stays uncertain rather than being replaced by the idealised table.

## Source basis

The selected [Open Music Theory ASPN sections](../references/open-music-theory-undated-aspn.md) were rechecked through their credited LibreTexts republication for pitch/class and octave-label distinctions. The [UNSW equations](../references/wolfe-undated-note-frequencies.md) were rechecked for octave ratios and twelve equal steps on 2026-10-14. The original OMT host was unavailable; the mirror is the same source family, not independent corroboration.

The tables, two-contour comparison and task interpretation are authored applications of those bounded accounts. No source recording, learner attempt or independent scientific review is claimed. No external figures or exercises are reproduced.
