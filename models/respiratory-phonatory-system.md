---
id: "sing:model:respiratory-phonatory-system"
type: "model"
version: "0.1.0"
language: "KPS 9.x"
status: "draft"
reviewed: null
uses_concepts: ["sing:concept:voice-production", "sing:concept:pitch"]
uses_models: ["sing:model:source-filter-voice-production"]
references: ["sing:reference:betts-2022-breathing", "sing:reference:wolfe-singing-mechanics", "sing:reference:nidcd-voice-care"]
basis_kind: "Selected respiratory mechanics and self-oscillating voice-source account; constructed cases, not a respiratory prescription"
source_alignment: [{"reference":"sing:reference:betts-2022-breathing","relation":"equation-application","locator":"Section 22.3, Pressure Relationships, Physical Factors Affecting Ventilation and Pulmonary Ventilation"},{"reference":"sing:reference:wolfe-singing-mechanics","relation":"standard-model-subset","locator":"Prepublication PDF pages 1-3, especially the voice-source explanation on page 2"}]
---

# Respiratory phonatory system

## Key takeaway

Breath supply and vocal-fold vibration are coupled: available air, pressure, tissue configuration and acoustic loading constrain sound production together.

## Summary

This Model combines respiration and phonation for one question: how can respiratory energy support a continuing voiced sound, and why does more air alone not specify its pitch or quality? It distinguishes mean airflow from its rapid modulation by vibrating folds. A simple flow budget and a self-oscillation account explain different aspects; neither is a personalised breathing technique.

## Purpose and boundary

Respiration supplies pressure and flow. Phonation here means the generation of voiced sound through vocal-fold vibration. They share a flow path, so independent boxes with a one-way instruction to push more air would conceal important relationships. The Model covers initiation, continuation and ending only as physical coordination problems, not as instructions for a particular onset technique.

The scope is ordinary voiced sound. Detailed tissue simulation, clinical airway assessment, vocal registration and individual breath-control strategies are outside it. A learner needs no pressure or airflow instrument to read the explanation. All numerical values below belong to constructed examples, not targets to reproduce.

## Components and variables

| Component | Variables and meaning | Role in the representation |
|---|---|---|
| Respiratory system | Lung volume in litres; respiratory movement, recoil and muscular activity | Changes the pressure conditions and supplies an air volume over time |
| Pressure difference | Pressure below versus above the glottis, in pascals; the glottis is the opening between the folds | Helps drive airflow through the larynx; not the same quantity as airflow |
| Airflow | Volume passing a location per second, such as litres per second | Includes a mean flow and, during voicing, a rapidly varying component |
| Vocal folds and their configuration | Geometry, tissue mechanical properties, approximation and tension | Interact with airflow; muscles adjust conditions rather than contracting once per sound cycle |
| Oscillation | Repeating tissue motion and modulation of flow; repetition rate in hertz | Provides a voiced source, with energy received from the airflow and lost through damping and radiation |
| Vocal tract | Air passage and acoustic load above the folds | Shapes emitted sound and can also affect the source; it is not merely a passive downstream label |

A hertz is one cycle per second. Fundamental frequency, written f0, is the repetition rate of a roughly periodic source. It is a physical descriptor, not a guarantee of the pitch heard from every possible sound. See [Voice production](../concepts/voice-production.md) and [Pitch](../concepts/pitch.md) for the shared distinctions.

## Relationships and mechanisms

The respiratory account relates pressure difference, flow resistance and flow. In a deliberately simplified steady-flow approximation, **mean flow = pressure difference / effective resistance**. Effective resistance describes the selected flow path and operating condition; it is not a constant for an opening that changes during every vibration. The formula is not a complete glottal-flow simulation.

For volume bookkeeping, **air used = integral of flow over time**; with an assumed constant mean flow, this becomes **air used = mean flow × duration**. Use the same volume convention throughout. Air quantity and pressure therefore answer different questions: how much passes during a phrase, and what drives it.

The vocal folds can oscillate when their mechanical configuration and the aerodynamic/acoustic conditions permit energy transfer from the airflow that compensates for losses. Muscle activity establishes and changes those conditions; vibration is not a sequence of consciously commanded closures at f0. A continuing pressure-driven flow does not by itself prove that folds are oscillating. The [singing mechanics account](../references/wolfe-undated-singing-mechanics.md) supplies this bounded mechanism.

Starting a voiced sound involves establishing conditions for oscillation; sustaining it requires continuing coordination and energy transfer; ending it changes those conditions. This does not select a hard, breathy or balanced onset for a learner. Pressure, geometry and tissue properties can affect more than one aspect of the output, so a higher intended pitch cannot be translated into a universal instruction to breathe harder.

## Worked example of a duration constraint

Assume a fictional constant mean flow of 0.12 litres per second. A two-second sound then uses 0.24 litres, while four seconds uses 0.48 litres. Under that single assumption, doubling duration doubles the volume requirement. It does not follow that any singer should use that flow, inhale a specified volume or lengthen a note.

This arithmetic supports a limited decision: when comparing two phrase plans, duration is one demand to examine separately from pitch. It cannot establish which breath, pause or technique is comfortable. Changing flow, articulation or pauses changes the calculation; no actual learner measurement has been made.

## Worked example of an ambiguous observation

Suppose a recording contains a roughly periodic 200 Hz source. Its period is 1/200 second, or 5 milliseconds. The Model explains why this does not mean the singer deliberately contracted a muscle 200 times each second. It represents rapid self-oscillation under a maintained configuration.

Now suppose another attempt sounds louder and somewhat higher. The two observations do not identify a unique change in pressure, tension, tract configuration or recording conditions. A microphone does not supply the missing respiratory and tissue measurements. The sensible analytical step is to separate observed sound from proposed mechanism, rather than diagnose insufficient breath from the sound alone.

## Interfaces

| Connection | Direction and exchanged quantity or constraint | Interpretation boundary |
|---|---|---|
| [Source and filter](source-filter-voice-production.md) | Glottal flow waveform supplies excitation; acoustic load can act back on the source | A one-way filter is an approximation, not proof of physical independence |
| [Articulatory speech sounds](articulatory-speech-sounds.md) | Constrictions and oral/nasal routing alter the flow path and acoustic load | An intended vowel does not uniquely specify respiratory effort |
| [Auditory vocal pitch matching](auditory-vocal-pitch-matching.md) | A target informs motor planning; produced sound supplies sensory feedback | A target in hertz is not a direct muscle or pressure command |
| [Rhythm and meter](rhythm-and-meter.md) and [Phrasing](../docs/body-of-knowledge-outline.md#phrasing) | Planned timing constrains how long sound or silence is needed | A beat or bar line is not automatically a breathing instruction |
| [Vocal care](../docs/body-of-knowledge-outline.md#vocal-care-and-comfortable-use) | Comfort and voice-change observations constrain whether a Practice continues | Comfort is not clinical clearance; the Model adds no treatment |

## Assumptions and unresolved questions

The budget ignores changing flow, leakage and pressure-dependent volume corrections. The mechanism is qualitative and does not calculate an individual's onset threshold, tissue stress, range or optimal control. Age, anatomy, health, registration and source-tract coupling may matter without being estimated here.

Unresolved for a particular singer are the actual flow pattern, configuration and cause of an observed change. Those cannot be recovered from the toy budget. The [first session](../practices/first-singing-session.md) and [reference-pitch Practice](../practices/match-a-reference-pitch.md) retain their existing comfortable-use and stopping conditions; no new vocal experiment is prescribed.

## Interpretation check and source basis

Can equal-duration sounds use different air volumes? Yes, if mean flows differ. Does a louder note prove more air was used? No; that would require additional evidence. Can the budget alone predict a pitch? No: its variables do not determine the oscillation frequency.

[OpenStax Section 22.3](../references/betts-2022-process-of-breathing.md) supplies the selected respiratory relationships, and [Wolfe and colleagues](../references/wolfe-undated-singing-mechanics.md), PDF pages 1-3, supply the voice-source account. The bookkeeping examples and interface choices are authored applications. [NIDCD](../references/nidcd-2025-taking-care-of-your-voice.md) supports the retained general care boundary, not the example values or a clinical assessment.
