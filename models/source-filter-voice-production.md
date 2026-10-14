---
id: "sing:model:source-filter-voice-production"
type: "model"
version: "0.1.0"
language: "KPS 9.x"
status: "draft"
reviewed: null
uses_concepts: ["sing:concept:voice-production", "sing:concept:pitch"]
uses_models: ["sing:model:respiratory-phonatory-system", "sing:model:articulatory-speech-sounds"]
references: ["sing:reference:wolfe-2016-source-filter", "sing:reference:wolfe-singing-mechanics"]
basis_kind: "Limited source-filter acoustic representation with explicit coupling limits and synthetic spectra"
source_alignment: [{"reference":"sing:reference:wolfe-2016-source-filter","relation":"standard-model-subset","locator":"Introduction, terminology footnote and Figure 2 with caption, printed pages 187 and 189"},{"reference":"sing:reference:wolfe-singing-mechanics","relation":"standard-model-subset","locator":"Prepublication PDF pages 2-3, source harmonics and vocal-tract resonances"}]
---

# Source and filter in voice production

## Key takeaway

Source repetition and vocal-tract shaping explain different properties of a sound; changing the spectral balance need not change the source pitch.

## Summary

A source-filter representation connects an excitation signal, a tract-dependent acoustic response and the radiated sound. It is useful for explaining why different vowels can share an intended pitch and why a recording alone cannot uniquely identify the source or vocal-tract configuration. The simple multiplication rule assumes limited source-filter independence; the actual voice can have reciprocal coupling.

## Purpose and boundary

Use this Model to separate **what excites the air** from **how the resulting spectrum is shaped**. A spectrum describes the frequency components of a signal and their strengths. A roughly periodic voiced source has components at its fundamental frequency f0 and integer multiples called harmonics. A resonance is a property of an acoustic system's response, not another name for f0.

The [respiratory phonatory Model](respiratory-phonatory-system.md) explains how the source can be generated; [articulation](articulatory-speech-sounds.md) describes configurations that help set the tract response. Neither explanation is replaced here. This introductory account is not a full model of consonant noise, vibrato, registers, hearing or individual anatomy.

## Components and representation

| Component | Variable and units or interpretation | Connection |
|---|---|---|
| Glottal excitation | U(f), the frequency representation of varying volume flow at the glottis, in consistent flow units | Supplies energy at source frequencies |
| Vocal tract and radiation | G(f), the frequency-dependent transfer from glottal flow to sound pressure at a stated observation point | Changes the amplitude and phase balance; depends on configuration and measurement position |
| Radiated sound | P(f), sound-pressure components, in pascals under a calibrated convention | Is the predicted output under the approximation |
| Source repetition | f0 in hertz; harmonic frequencies n × f0 for positive integers n | Locates harmonic components, not tract resonances |
| Tract resonances | R1, R2 and further resonant frequencies in hertz | Describe the response; they need not coincide with a harmonic |
| Spectral envelope | The broad pattern of component amplitudes; peaks are often called formants | Is observed from source and tract together, not a direct image of an organ |

The bounded relation is **P(f) = G(f) × U(f)**. With flow in cubic metres per second, G has units of pressure divided by flow, or Pa·s/m³. It is not automatically a dimensionless amplification number. For magnitudes the corresponding products predict component strengths; the full frequency representation also includes phase. The numerical example below deliberately uses normalised magnitudes only.

Here R denotes a tract resonance; F, when used for a formant, denotes a spectral-envelope peak. Usage differs in voice literature, so the distinction is stated rather than silently equating every visible peak with a measured tract resonance. [Wolfe and colleagues 2016](../references/wolfe-2016-measured-source-filter.md) explains the experimental separation and its terminology.

## Mechanism and approximation

The tract's shape and its open and closed paths affect its acoustic response. A harmonic near a strong part of that response may be prominent in the radiated sound; the response does not create a new fundamental merely by emphasising a harmonic. A voiced source and a vowel-dependent filter can therefore change tone colour without requiring a new intended note.

The calculation treats a configuration as approximately fixed during the analysed segment and the response as linear. In a real voice, acoustic loading can also alter vocal-fold oscillation and glottal flow. The source is not always independent of the filter. The limited model explains a distinction; it does not warrant a universal command to change a vowel without affecting anything else.

## Worked example of the same source with different shaping

Consider a constructed 200 Hz periodic source and three of its harmonics. Values are arbitrary normalised magnitudes, not a measured singer, a specified vowel or a vocal exercise.

| Frequency | Source U | Response A | Output A | Response B | Output B |
|---|---|---|---|---|---|
| 200 Hz | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| 400 Hz | 0.50 | 0.50 | 0.25 | 1.00 | 0.50 |
| 600 Hz | 0.25 | 2.00 | 0.50 | 0.50 | 0.125 |

Each output entry is source × response. The frequency positions stay at 200, 400 and 600 Hz, but their relative strengths differ. The supported prediction is a different spectral balance, not a change from 200 Hz to 600 Hz in fundamental frequency. Nor can these three invented gains identify a vowel or prove a particular perceived timbre.

For [matching a reference](../practices/match-a-reference-pitch.md), this distinction matters: an electronic tone and a voice need not have identical spectral balance to share a pitch. Matching the reference's buzzy tone colour is a different task from matching its height.

## Worked example of an inference that is not supported

At one frequency an observed output magnitude of 0.50 could arise from source 0.25 × response 2, or source 0.50 × response 1. The output alone does not select one explanation. More generally, a microphone spectrum combines source, tract, radiation and recording conditions.

A singer reports that a vowel sounded brighter while the intended note stayed the same. The Model offers acoustic shaping as a possible explanation, but it does not prove that only the filter changed. A reliable comparison would need the intended task and appropriate observations; tissue configuration, health and perceived comfort are not visible in a spectral peak. This is an interpretation limit, not a request to obtain specialised equipment.

## Interfaces

| Connection | Information or effect exchanged | Limit at the boundary |
|---|---|---|
| [Respiratory phonatory system](respiratory-phonatory-system.md) | Flow modulation enters this representation; tract loading may influence the source in return | Multiplication with an independent source omits that feedback |
| [Articulatory speech sounds](articulatory-speech-sounds.md) | Articulator and velum configuration helps determine oral/nasal geometry | A phonetic label is not a unique measured transfer function |
| [Pitch relationships](pitch-relationships.md) | f0 can provide a physical coordinate for a stable target | Pitch class and interval arithmetic do not describe the full spectrum or perception |
| [Auditory vocal matching](auditory-vocal-pitch-matching.md) | Radiated sound becomes sensory input with pitch, timing and tone-colour information | Perception is not a perfect recovery of U or G |
| [Dynamics and vibrato](../docs/body-of-knowledge-outline.md#dynamics-and-vibrato) | Time-varying source and response can affect amplitude and frequency patterns | This stationary subset is not a model of expressive dynamics or vibrato |

## Assumptions and unresolved questions

The numerical example omits phase, noise sources, changing geometry, reflections outside the mouth and sampling limitations. Sparse harmonics at high f0 can make the envelope difficult to infer. The cited physical-model experiment supports separating measured excitation, transfer and output under its conditions, not identifying all such quantities from one beginner recording.

Which source changes accompany a vowel change, when coupling becomes important, and how a particular listener interprets a spectrum remain open questions for an individual case. No healthy configuration, registration strategy or safe intensity is inferred.

## Interpretation check and sources

Does a stronger 600 Hz harmonic prove a 600 Hz fundamental? No. Does equal f0 require identical vowels? No. Does changing tract shape guarantee unchanged vocal-fold behaviour? No; that would exceed the independence approximation.

The [2016 measured source-filter paper](../references/wolfe-2016-measured-source-filter.md), Introduction and Figure 2, supplies the acoustic representation. The [singing mechanics chapter](../references/wolfe-undated-singing-mechanics.md), inspected pages 2-3, supplies source and coupling context. Both figures were inspected but not reproduced. The tables and inference examples are original constructed cases.
