---
id: "sing:model:articulatory-speech-sounds"
type: "model"
version: "0.1.0"
language: "KPS 9.x"
status: "draft"
reviewed: null
uses_concepts: ["sing:concept:voice-production", "sing:concept:pitch"]
uses_models: ["sing:model:source-filter-voice-production"]
references: ["sing:reference:anderson-2022-articulation"]
basis_kind: "Selected articulatory phonetic feature representation; not a full language-specific diction or gesture-timing model"
source_alignment: [{"reference":"sing:reference:anderson-2022-articulation","relation":"standard-model-subset","locator":"Essentials of Linguistics 2e, sections 3.2-3.5; articulators, consonant place and manner, voicing, vowel quality and nasality"}]
---

# Articulatory speech sounds

## Key takeaway

Place, manner, voicing and vowel configuration describe different aspects of a speech sound; none alone specifies the sung note or word meaning.

## Summary

This Model uses selected articulatory-phonetic descriptions to relate speech-sound categories to constrictions and airflow routes. It explains contrasts between a nasal and an oral stop, between voiced and voiceless fricatives, and between vowel qualities. These are descriptions for understanding sung words, not a complete pronunciation inventory or instructions to force an articulator into position.

## Purpose and boundary

The explanatory question is **what changes in the sound-forming configuration, and which other distinctions remain separate?** Articulation is kept distinct from acoustic shaping because a configuration and its acoustic consequence are different representations of a connected process. Diction additionally requires a particular language, word and context; text setting requires a musical timeline.

The source account is [Essentials of Linguistics 2e, sections 3.2-3.5](../references/anderson-2022-speech-articulation.md). A speech sound is not a written letter. Square brackets below mark phonetic examples, not note names or a requirement to read the full International Phonetic Alphabet.

## Components and feature relationships

| Dimension | Values or components represented | What it helps distinguish |
|---|---|---|
| Articulators | Tongue, lips, jaw and structures approached by them; the velum helps control nasal coupling | Which configuration and route are involved |
| Consonant place | Where a constriction is formed, such as both lips or the tongue near the alveolar ridge behind the upper teeth | Sounds with similar constriction manner in different locations |
| Consonant manner | Closure, turbulent narrowing, or a relatively open approximation; oral versus nasal passage matters | How the flow path is constrained |
| Voicing | Whether vocal-fold vibration accompanies the sound | A distinction that is not reducible to lip or tongue position |
| Vowel quality | Relative tongue height and front/back position, with lip rounding | Broad dimensions of a relatively open tract configuration |
| Nasality | Whether the nasal passage participates through velum configuration | Oral and nasal variants, including those with oral closure |

The descriptive relation is **a bundle of dimensions identifies a selected sound category**. The physical relation is **configuration constrains the air path and acoustic response**. Those relations are not identical: broad categories do not specify every millimetre of movement, and different speakers may realise a category differently.

A high vowel means a relatively high tongue configuration, not a high musical pitch. In the source's linguistic terminology, phonation is a broader dimension that includes voicing distinctions; the [respiratory phonatory Model](respiratory-phonatory-system.md) uses phonation more narrowly for voiced-source generation. Keep the scope of the term visible rather than treating the two uses as competing facts.

## Worked example of the same place with different routes

Consider idealised [m] and [p], not a recording of the reader. Both involve closure at the lips, so lip place alone cannot distinguish them. For [m], the nasal route permits flow and the sound is voiced. For an ordinary voiceless oral [p], the oral path is closed during the closure, the nasal route is blocked, and release is part of the stop event.

The Model therefore explains why closing the lips does not necessarily eliminate all continuing voiced sound: oral closure does not imply every outlet is closed. It also predicts that a picture of closed lips alone is insufficient to identify [m] or [p]. Velum configuration, voicing and the event sequence matter. No inference about healthy humming follows from this contrast.

A second contrast, idealised [s] versus [z], holds an alveolar fricative description broadly similar while changing voicing. This shows why a consonant question may involve both articulation and source vibration rather than belong exclusively to one folder.

## Worked example of vowel quality versus pitch

Compare idealised [i], a high front unrounded vowel, with [u], a high back rounded vowel. The broad height category is shared; backness and rounding differ. Those configuration differences can change acoustic shaping even when the intended sung note is unchanged.

The useful conclusion is not that a particular vowel always has a specified resonance frequency. It is that vowel quality and musical pitch are separate descriptive axes. A learner who changes the intended syllable while trying to imitate an electronic reference may be solving a tone-colour problem that the [pitch-matching Practice](../practices/match-a-reference-pitch.md) did not ask them to solve. The existing Practice remains the place for any vocal action.

For a syllable such as [mi], a description includes a transition from nasal closure toward a vowel. This Model does not determine whether that transition should begin before, on or after a beat. That is a text-setting and performance question, not a fact contained in the consonant feature bundle.

## Interfaces

| Connected subsystem | What crosses the interface | What this representation cannot supply |
|---|---|---|
| [Source and filter](source-filter-voice-production.md) | Configuration and oral/nasal routing constrain acoustic response | A full response curve from a vowel label alone |
| [Respiration and phonation](respiratory-phonatory-system.md) | Constrictions affect the flow path; voicing involves the sound source | A safe pressure, effort or individual onset instruction |
| [Rhythm and meter](rhythm-and-meter.md) | Speech-sound events can be placed on a timeline | Whether an event boundary is an intended syllable or vowel onset |
| [Diction and meaning](../docs/body-of-knowledge-outline.md#diction-and-meaning) | Phonetic categories contribute to a language-specific pronunciation | Word meaning, accent choice, lexical stress or complete pronunciation rules |
| [Text setting](../docs/body-of-knowledge-outline.md#text-setting) | Syllables and transitions require musical placement | An established model of syllable stress and expressive timing; this remains a gap |
| [Pitch relationships](pitch-relationships.md) | A sound category can accompany different intended pitches | Pitch height from vowel height, or a note name from a written letter |

## Assumptions and unresolved questions

The examples are idealised descriptions, not claims that all languages or accents use identical sounds. Connected speech and singing involve movement and overlap; static categories omit detailed coarticulation, timing, anatomy and acoustic variability. The source's vowel dimensions are a useful descriptive subset, not an exhaustive mapping of every vowel or a direct medical measurement.

A complete diction account still needs a language and repertoire. A gesture-timing account would need further sources and cases. Nothing here establishes a universally superior accent, a correct singing tone, or an individual's ability to produce the examples.

## Interpretation check and source basis

Can two lip-closure sounds differ because the nasal route differs? Yes. Does high vowel mean high note? No. Can a phonetic feature table place every consonant in a song? No; it lacks the musical and linguistic context needed for that decision.

The [2022 textbook record](../references/anderson-2022-speech-articulation.md) locates the inspected articulation, consonant and vowel accounts, including the credited mirror used for section 3.5. The worked comparisons apply their distinctions; no source diagrams, exercise recordings or learner outcomes are reproduced.
