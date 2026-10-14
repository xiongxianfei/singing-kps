---
id: "sing:model:tonal-organisation"
type: "model"
version: "0.1.0"
language: "KPS 9.x"
status: "draft"
reviewed: null
uses_concepts: ["sing:concept:pitch", "sing:concept:intonation"]
uses_models: ["sing:model:pitch-relationships"]
references: ["sing:reference:omt-major-scales", "sing:reference:omt-aspn", "sing:reference:unsw-note-frequencies"]
basis_kind: "Selected major-scale coordinate representation; authored transposition cases, not a complete tonal or perceptual theory"
source_alignment: [{"reference":"sing:reference:omt-major-scales","relation":"standard-model-subset","locator":"Major Scales and Scale Degrees, Solfege, and Scale-Degree Names"},{"reference":"sing:reference:omt-aspn","relation":"definition-paraphrase","locator":"Pitch versus Pitch Class and Octave Designations"},{"reference":"sing:reference:unsw-note-frequencies","relation":"equation-application","locator":"Equal-temperament frequency and logarithmic-ratio equations"}]
---

# Tonal organisation

## Key takeaway

A note's role depends on its declared tonal context: the same pitch can have different scale-degree roles, and a melody can preserve those roles after transposition.

## Summary

This first tonal Model represents a specified major scale, its tonic, ordered degrees and transposition. It extends pitch relationships with context rather than replacing pitch height or interval distance. It does not infer a key from one note, explain all harmony or claim that a scale automatically determines a listener's expectations.

## Purpose and boundary

The question is **how does a pitch participate in a declared major-scale pattern?** A tonic is the reference pitch class for that selected organisation. A scale degree is a numbered position relative to it. Degree 1 is the tonic; the following numbered positions identify relationships rather than absolute frequencies.

The account follows the inspected [Open Music Theory major-scale chapter](../references/open-music-theory-undated-major-scales.md). Only a Western major-scale subset is implemented. Minor keys, modes, modulation, chromatic harmony, phrase closure and empirical theories of tonal expectation remain outside it. The filename denotes the developing topic, not completion of every tonal account.

## Components and representation

| Component | Variable or representation | Relationship |
|---|---|---|
| Tonic | A declared pitch class, such as C or A | Establishes the contextual origin |
| Scale pattern | Whole, whole, half, whole, whole, whole, half steps back to the tonic's octave | Selects the major collection and ordering |
| Degree | Positions 1 through 7; the tonic repeats at the next octave | Associates a pitch class with a role in this declared context |
| Pitch height | A note with octave placement, such as A3 | Specifies a particular target rather than only a scale role |
| Melody | An ordered sequence of pitches, with timing specified separately | Can be described both by absolute targets and relative degrees |
| Transposition | One constant interval applied to all pitches and the tonic | Can retain interval and scale-degree relationships while changing height |

For the numerical representation, use twelve-tone equal temperament. A half step is one semitone; a whole step is two. The seven degree offsets above the tonic are **0, 2, 4, 5, 7, 9, 11 semitones**, with 12 returning to the tonic one octave higher. This is a mapping in a chosen tuning convention, not a universal definition of musical scales.

If a tonic is represented by pitch-class number T with C = 0, a degree's class is **(T + degree offset) modulo 12**. Modulo 12 means retaining the remainder after whole octaves are removed. Octave placement and conventional spelling must still be specified to obtain a full musical target; a class number does not supply either by itself.

## Worked example of one pitch with two roles

In C major, the classes in order are C, D, E, F, G, A and B. A is degree 6. In A major, the order is A, B, C-sharp, D, E, F-sharp and G-sharp. A is degree 1.

Suppose the actual reference remains A3 at 220 Hz under the repository's tuning convention. Moving from the declared C-major context to A-major context changes its scale-degree role, not that reference's frequency. The conclusion follows from the chosen contexts; a recording of A3 by itself would not tell us which context was intended.

This separates two possible learner questions: matching the height of A3 and understanding its role within a song. The [reference-pitch Practice](../practices/match-a-reference-pitch.md) asks the first and does not require identifying a key.

## Worked example of transposition

Consider the constructed fragment C4, D4, E4 in a declared C-major context. Its degrees are 1, 2, 3 and its successive interval distances are two semitones, then two semitones. Transpose the entire fragment and tonic upward by two semitones:

| Original target | Original degree | Transposed target in D major | Retained relationship |
|---|---|---|---|
| C4 | 1 | D4 | Tonic |
| D4 | 2 | E4 | Two semitones above tonic |
| E4 | 3 | F-sharp4 | Four semitones above tonic |

The target heights change; the degree sequence and intervals remain. In the chosen equal temperament, every frequency is multiplied by the same ratio, **2^(2/12)**, approximately 1.12246. Adding a fixed number of hertz would not preserve these equal interval relationships.

For a singing decision, this distinction helps state what changing a song's key preserves and changes. It does not establish that D major is comfortable for a particular voice. Suitability also concerns where pitches recur, duration, words, dynamics and individual conditions; those broader demand Models remain to be developed. This example is not an instruction to sing the fragment.

## Interfaces

| Connected subsystem | Information passed or received | Boundary |
|---|---|---|
| [Pitch relationships](pitch-relationships.md) | Pitch class, octave and interval distance supply coordinates; tonal context supplies scale-degree roles | Class alone cannot identify a role; degree alone cannot identify a unique frequency |
| [Rhythm and meter](rhythm-and-meter.md) | Degree and pitch sequences can be attached to event times | A timed major-scale collection does not determine complete phrasing |
| [Auditory vocal matching](auditory-vocal-pitch-matching.md) | Categorical and learned tonal information may influence target interpretation and planning in the proposed architecture | This coordinate table does not measure stored knowledge or predict every listener's expectation |
| [Intonation](../concepts/intonation.md) | A context contributes to the intended relationship against which an attempt is compared | No universal cent tolerance, expressive tuning rule or judgement of a whole phrase is supplied |
| [Repertoire selection](../docs/body-of-knowledge-outline.md#repertoire-selection) and [Range and tessitura](../docs/body-of-knowledge-outline.md#range-and-tessitura) | Transposition changes pitch placement while retaining selected structure | Range coverage, comfort and repeated demands need individual and song information |
| [Melody harmony and form](../docs/body-of-knowledge-outline.md#melody-harmony-and-musical-form) | The representation supplies one collection and relative positions | Chords, harmonic function, cadence and larger form are not derived from this Model alone |

## Assumptions and unresolved questions

A tonal context is supplied, not discovered by the Model. Actual music may leave its scale collection, change context or support more than one analysis. Relative degree naming must not be silently mixed with a fixed note-naming system. No solfege system or notation reading is a prerequisite here.

Outstanding questions include the appropriate account for other traditions, minor and modal organisation, ambiguity of tonal centre, and what observations support claims about listeners' expectations. The current mathematical mapping is not a perceptual or neurological theory.

## Interpretation check and source basis

Does A always mean degree 1? No. Does preserving contour guarantee preserving intervals? No. Does moving every note by two semitones preserve equal-tempered interval distances? Yes, provided the entire pattern is moved consistently. Does that prove the new version is suitable to sing? No.

[Open Music Theory major scales](../references/open-music-theory-undated-major-scales.md) supplies the step pattern and contextual degree distinction. [ASPN](../references/open-music-theory-undated-aspn.md) supplies the pitch-label boundary, and [UNSW](../references/wolfe-undated-note-frequencies.md) supplies the ratio arithmetic. The two-context and transposition cases are authored applications; no source melody, recording or learner performance is reproduced.
