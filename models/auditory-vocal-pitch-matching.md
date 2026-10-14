---
id: "sing:model:auditory-vocal-pitch-matching"
type: "model"
version: "0.2.0"
language: "KPS 9.x"
status: "draft"
reviewed: null
references: ["sing:reference:pfordresher-2015-framework"]
uses_concepts: ["sing:concept:pitch", "sing:concept:intonation"]
uses_models: ["sing:model:pitch-relationships", "sing:model:tonal-organisation", "sing:model:respiratory-phonatory-system", "sing:model:source-filter-voice-production"]
uses_methods: ["sing:method:reference-pitch-comparison"]
basis_kind: "Selected subset of a published proposed functional architecture with explicit interfaces; not a diagnosis or a complete learning theory"
source_alignment: [{"reference":"sing:reference:pfordresher-2015-framework","relation":"standard-model-subset","locator":"Figure 1 and Structural and functional mechanisms in singing, printed pages 228-229"}]
---

# Auditory vocal pitch matching

## Key takeaway

Hearing a target, organising a vocal action and interpreting the resulting sound are related but distinct functions; a mismatch does not reveal which function caused it.

## Summary

This beginner-facing representation retains the core architecture proposed by Pfordresher and colleagues (2015), Figure 1, and makes its acoustic, categorical and motor interfaces explicit. It explains why detecting a difference need not imply being able to correct it. The boxes represent proposed functions and information flows, not directly observed modules in this learner's brain or a proven single cause of inaccurate singing.

## Purpose and boundary

Use the Model to distinguish the reference, the perceived goal, the vocal attempt and the evidence used to compare them. It supports reasoning about the existing [comparison Method](../methods/reference-pitch-comparison.md) without requiring a microphone, tuner or notation.

The earlier core chain is retained: **external sound -> perception -> sensorimotor translation -> motor planning and output -> auditory feedback -> perception**. These arrows denote proposed functional connections. They do not guarantee improvement each time the loop is repeated.

## Components and represented information

| Part | Relevant information or variables | Observation boundary |
|---|---|---|
| External reference | Played pitch, duration, loudness and tone colour | File identity may be known; actual playback may still differ |
| Low-level perceptual representation | Heard sound properties distinguished from one another | A verbal report is evidence about perception, not direct access to its mechanism |
| Sensorimotor translation | Associations relating heard results to ways of producing them | Cannot be measured from one unsuccessful note |
| Categorical representation | Pitch and tonal relationships interpreted using learned categories | Does not require conscious note naming; may differ with experience and context |
| Stored knowledge | Long-term information involved in categorisation and planning | Not a quantity established by confidence or an app score |
| Motor planning and output | Coordination involving respiration, phonation and articulation; resulting sound | Sound can be observed, while a unique plan cannot be inferred from it |
| Auditory feedback | Heard consequences of the vocal action | Re-enters perception but is not automatically a reliable correctness label |

The source's Figure 1 includes a categorical pathway and long-term memory alongside sound-based translation. Categorical pitch and tonal information can contribute to motor planning, with stored knowledge influencing the transformations. This refinement makes that interface visible rather than treating an absolute reference and a note's musical role as the same object. It does not add a newly validated module or a complete memory mechanism.

## Relationships and mechanisms

There are three explanatory levels to keep separate. The reference and returned sound are acoustic inputs. Perception and translation describe proposed information processing. The vocal output is produced by a physical system with its own constraints. An intended pitch in hertz is not a direct pressure or muscle command.

For a short reference-replay task, the learner must also retain enough of the target across a pause to compare it with an attempt. Replaying can make the reference available again, but an improvement after replay would not isolate memory as the original cause. This is a task-level application, not a measured memory diagnosis.

The architecture permits multiple explanations for the same apparent error: an unclear reference, uncertain perception, a changed target representation, translation difficulty, execution, or comparison could contribute. Naming these alternatives is not evidence that any one occurred. The source proposes an organising framework rather than testing every pathway causally.

## Worked example of detecting without correcting

In a constructed case, a learner reports that their voice was lower than the reference but cannot produce a closer attempt. The report concerns discrepancy detection; the unsuccessful adjustment concerns the action and its outcome. The Model keeps those functions separate, so the combination is not logically contradictory.

A useful next decision in the [matching Practice](../practices/match-a-reference-pitch.md) is to retain uncertainty and its stopping or reference-check options. Repeatedly commanding higher is not guaranteed to solve the difficulty, and the Model does not justify increasing effort or diagnosing a defective component. No learner trial is asserted by this example.

## Worked example of the right class but wrong height

Suppose a specified reference is A3 at 220 Hz and a constructed stable output is A4 at 440 Hz. The [pitch representation](pitch-relationships.md) identifies a shared class and a one-octave height difference. A class-only display could report A for both. The functional Model explains why the information used for comparison must be identified: class agreement and unison agreement are different target representations.

It does not establish whether the octave difference arose in hearing, categorisation, planning, execution or measurement. An optional tool may also misidentify an octave. If all that is available is a related-sounding tone, the ear-based report may remain uncertain. The mathematical example is not a measurement of the user's voice.

## Worked example of changed sound colour

A person intends the same pitch on two vowels and hears a different tone colour. The [source-filter Model](source-filter-voice-production.md) shows how spectral balance can change without a different source fundamental in its approximation. The feedback architecture explains why perception has multiple sound properties to distinguish before deciding whether a pitch correction is needed.

That does not prove the pitches actually matched or that only the tract changed. The observation calls for a correctly framed comparison, not an automatic instruction to modify the voice until it resembles the electronic reference.

## Interfaces

| Connected explanation | Direction and information exchanged | What the link does not claim |
|---|---|---|
| [Pitch relationships](pitch-relationships.md) | Defines the requested relationship, such as unison, octave or interval | A representation of the target is not a model of the ability to hear or produce it |
| [Tonal organisation](tonal-organisation.md) | Supplies a selected account of categorical musical context | A major-scale table does not prove an individual's learned expectations |
| [Respiratory phonatory system](respiratory-phonatory-system.md) | A motor plan is realised through a constrained physical instrument; sound returns as feedback | No direct conversion from target frequency to a unique tissue or pressure state |
| [Source and filter](source-filter-voice-production.md) | Acoustic output contains frequency and spectral information available to perception | The listener need not recover the source/filter decomposition, and may confuse properties |
| [Rhythm and meter](rhythm-and-meter.md) | Event timing delimits target and attempt and separates onset from a steadier portion | This is not a full model of vocal rhythm learning or synchronisation |
| [Comparison Method](../methods/reference-pitch-comparison.md) | Observations and confidence inform an authored next-step decision | Approximately matching is not a universal measured pass; uncertain remains a legitimate outcome |
| [Learning and feedback](../docs/body-of-knowledge-outline.md#learning-and-feedback) | Repeated observations could support a later account of change | One successful loop proves neither retention nor transfer to songs |

## Assumptions and unresolved questions

The subset omits detailed neural, developmental and non-auditory feedback accounts. The represented functions are not independently measured here. Their ordering is explanatory, not a compulsory conscious sequence. Timbral differences, recording conditions, range suitability and health can constrain a task without being diagnosed by the diagram.

Which function or connection contributed to a particular mismatch, how stored knowledge changes, and what practice generalises remain unresolved without relevant evidence. Clinical assessment and singing instruction answer different questions; the Model replaces neither. Existing comfortable-use boundaries remain unchanged.

## Interpretation check and source alignment

Could someone hear a difference yet have trouble changing their voice? Yes. Does an A-only result prove the reference was matched? No. Does one unsuccessful attempt identify a defective component? No. Does the broader tonal path make notation a prerequisite? No.

[Pfordresher and colleagues 2015](../references/pfordresher-2015-singing-accuracy-framework.md), Figure 1 and printed pages 228-229, was re-inspected for the functional and categorical paths. The relation label records a Model subset, not a certified standard. The figure is not copied. The octave, colour and next-decision cases are authored applications, not experimental results or an independent validation of the framework.
