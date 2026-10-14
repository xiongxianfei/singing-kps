---
language: "KPS 9.x"
package_version: "0.3.0"
status: "draft"
reviewed: null
---

# Singing Model architecture

## Key takeaway

Use complementary Models to explain musical targets, physical production and perception, while preserving the language, performance, individual and learning questions they do not yet answer.

## Summary

This architecture connects the 24 directly named topics in the [Body of Knowledge Outline](body-of-knowledge-outline.md) to purposeful explanatory Models and explicit remaining gaps. The first implemented groups contain seven Models: the two existing pitch Models refined in place and five new explanations of production, articulation, time and major-scale context. The groups are cross-cutting development views, not a replacement hierarchy, a compulsory reading sequence or a claim that every topic needs its own file.

The integration is an authored KPS design. The disciplinary relationships within each Model have their own source records and limits. No single source establishes this complete architecture, and no institution is claimed to endorse it. The actual vocal activities remain the two existing [beginner Practices](../README.md#start-here), requiring only a phone or computer for reference playback where applicable.

## Purpose and explanatory boundaries

The learner should be able to separate several questions about a singing observation: which musical relationship was intended; what sound and timing occurred; what physical explanations are possible; what the comparison actually establishes; and what evidence is still missing. Those questions require different representations.

| Kind of explanation | Implemented representation | What its relationships mean |
|---|---|---|
| Physical production | Respiratory phonatory system; source and filter | Energy, flow and acoustic effects under stated approximations |
| Articulatory description | Articulatory speech sounds | Feature bundles and flow-path configurations, not a full language grammar |
| Musical coordinates | Pitch relationships; rhythm and meter; tonal organisation | Mathematical and conventional relationships, not physiological commands |
| Perception and action | Auditory vocal pitch matching | A published proposed functional account, not directly observed brain modules |
| Task choice | Existing Practices and comparison Method | Authored decisions constrained by evidence and comfort, not new scientific laws |

A full account of a singer would also need individual, linguistic, expressive, social and learning information. These are visible below without being promoted into unsupported Models. The architecture cannot diagnose a voice or reduce singing quality to one pitch score.

## Current Model collection and boundary decisions

| Model | Explanatory question | Why this boundary is useful |
|---|---|---|
| [Respiratory phonatory system](../models/respiratory-phonatory-system.md) | How do pressure, flow and tissue conditions support a continuing voiced source? | Respiration and phonation share the flow path and energy relationship; separating them into isolated instructions would hide coupling |
| [Source and filter](../models/source-filter-voice-production.md) | How can the same source be shaped into different spectral balances? | Acoustic transfer and the inverse-inference problem differ from how the source is generated |
| [Articulatory speech sounds](../models/articulatory-speech-sounds.md) | What configuration distinctions help explain a speech-sound contrast? | A descriptive feature space is useful independently of acoustic spectra, language meaning and musical placement |
| [Pitch relationships](../models/pitch-relationships.md) | What height, class, octave, interval or contour relationship is requested? | Target representation must remain distinct from the ability to hear and produce it; its existing identity and worked cases are retained |
| [Rhythm and meter](../models/rhythm-and-meter.md) | When do events occur, relative to which pulse and grouping? | Rhythm and metre are complementary views of one timeline; two disconnected files would duplicate the variables needed for comparison |
| [Tonal organisation](../models/tonal-organisation.md) | What role does a pitch have in a declared major-scale context? | Contextual degree and absolute height can vary independently; the present major-scale subset is not all tonal theory |
| [Auditory vocal pitch matching](../models/auditory-vocal-pitch-matching.md) | How are hearing, target interpretation, action and feedback related? | The refined existing framework connects acoustic and categorical information without treating an error as a diagnosis |

Overlap is deliberate. Vocal-fold vibration belongs in the production explanation and also matters to voicing in articulation. Pitch appears in a mathematical target representation, a tonal context and a proposed perceptual architecture. These uses must preserve meaning at their interfaces, not be forced into mutually exclusive folders.

The architecture itself stays in documentation because its grouping and navigation choices are local synthesis, not an independently established scientific Model. There is no file-count target and no one-to-one mapping from outline headings to Models.

## Interface register

An interface states what is exchanged, in which direction, and which inference would exceed it. A linked file alone is not an interface specification. The table gives the major connections; each owning Model explains its local variables and limitations.

| Connection | Type and direction | Information or effect | Boundary that must survive the connection |
|---|---|---|---|
| Respiration and folds within the production Model | Physical coupling | Pressure difference, flow and mechanically changing opening | Mean-flow bookkeeping is not a time-resolved tissue simulation |
| Production and source-filter Models | Physical, potentially reciprocal | Glottal-flow excitation goes to the tract; acoustic loading can act back | The linear independent-filter approximation is not universal independence |
| Articulation and acoustic shaping | Configuration to acoustic consequence, with coupled source context | Oral/nasal geometry and constrictions affect response | A vowel label does not determine one exact transfer function |
| Pitch and tonal Models | Mathematical/contextual mapping | Height, class and intervals combine with a declared tonic and scale degree | Class loses octave information; degree needs context and does not uniquely specify frequency |
| Pitch and rhythm Models | Event alignment | A pitch or interval sequence is assigned onset and duration | Shared contour says nothing about timing or interval size |
| Rhythm and physical production | Demand constraint | Duration and gaps delimit the requested sound | A metric boundary is not automatically a breath instruction |
| Musical targets and auditory matching | Representational input | Requested height, relation, time window and possibly learned tonal role | A target is not proof that it was perceived or translated accurately |
| Physical sound and auditory matching | Sensory information | Output contains pitch, spectral, temporal and loudness information | A perceived difference does not identify its unique physiological cause |
| Auditory matching and comparison Method | Evidence to authored decision | Reported discrepancy, confidence, tool limitations and comfort | Uncertain must not be silently converted into a pass or a forced correction |
| Articulation and text setting | Pending linguistic/timing integration | Syllables, stress and articulatory transitions need musical placement | Static features cannot decide consonant placement or word meaning |
| Musical demands and individual suitability | Pending constraint model | Repeated pitch placement, duration, dynamics and language interact with individual conditions | A reachable isolated note does not establish song suitability; no numerical safety model is supplied |
| Performance and learning over time | Pending explanatory account | Context, feedback, later observations and task changes | One successful attempt is not evidence of retained skill or transfer |

Interfaces describe different relation types. A musical coordinate can inform a goal without physically causing the required sound. Conversely, source-tract coupling can exist even when a score represents pitch and vowel as separate symbols. This prevents a convenient page layout from becoming an unsupported causal pipeline.

## Coverage of all outline topics

**Implemented subset** means a local Model can explain the stated introductory question using its representation and worked cases. It does not mean the full topic is covered or that a learner has demonstrated competence. **Pending account** means the question remains visible, with existing context or partial support but no sufficient local Model of that question. These descriptions supplement rather than erase the outline's finer-grained coverage rows.

| Outline topic | Current contribution | Remaining explanatory gap |
|---|---|---|
| [Respiration](body-of-knowledge-outline.md#respiration) | Production Model: pressure, flow and duration budget | Individual breath coordination and changing phrase demands |
| [Phonation](body-of-knowledge-outline.md#phonation) | Production Model: qualitative initiation, continuation and ending of self-oscillation | Detailed onset accounts, tissue dynamics and individual coordination |
| [Vocal tract resonance](body-of-knowledge-outline.md#vocal-tract-resonance) | Source-filter Model: excitation, response, spectrum and coupling limits | Detailed resonance measurement, nonlinear interactions and individual strategies |
| [Articulation](body-of-knowledge-outline.md#articulation) | Articulatory Model: selected consonant/vowel features and oral/nasal routing | Time-varying gestures, coarticulation and language-specific inventories |
| [Pitch relationships](body-of-knowledge-outline.md#pitch-relationships) | Refined pitch Model: height, class, octave, interval, contour and linked context | Full interval spelling, alternative tuning and perceptual discrimination |
| [Rhythmic organisation](body-of-knowledge-outline.md#rhythmic-organisation) | Rhythm/metre Model: events, durations, rests, pulse and constant-tempo mapping | Expressive microtiming, complex rhythms and broader traditions |
| [Metrical organisation](body-of-knowledge-outline.md#metrical-organisation) | Rhythm/metre Model: grouping and simple/compound distinction | Ambiguous and changing metres, beat perception and nonstandard organisations |
| [Tonal organisation](body-of-knowledge-outline.md#tonal-organisation) | Major-scale Model: tonic, degree and transposition | Minor/modal systems, tonal ambiguity, harmony and expectation mechanisms |
| [Text setting](body-of-knowledge-outline.md#text-setting) | Interface between articulatory and timing descriptions is specified | Pending account of syllables, stress, consonant/vowel placement and text-music conflicts |
| [Auditory vocal pitch matching](body-of-knowledge-outline.md#auditory-vocal-pitch-matching) | Refined proposed functional Model and existing single-reference Practice | Individual causal assessment, broader auditory feedback and song-level transfer |
| [Vocal instrument and individual variation](body-of-knowledge-outline.md#vocal-instrument-and-individual-variation) | Physical Models explain shared functions, not one standard instrument | Age, anatomy, development and between-person variability |
| [Vocal care and comfortable use](body-of-knowledge-outline.md#vocal-care-and-comfortable-use) | Existing care Reference and Practice stopping boundaries constrain use | No local mechanistic account of load/recovery or quantitative safety threshold |
| [Registration](body-of-knowledge-outline.md#registration) | Production/source-filter interfaces identify quantities that may matter | Pending comparison of sourced register accounts, transitions and terminology |
| [Range and tessitura](body-of-knowledge-outline.md#range-and-tessitura) | Pitch and tonal Models describe target height and transposition | Pending account of pitch span versus distribution and repeated demands |
| [Voice classification](body-of-knowledge-outline.md#voice-classification) | Not inferred from note labels or a small audio bank | Pending scoped comparison of classification systems and limits |
| [Diction and meaning](body-of-knowledge-outline.md#diction-and-meaning) | Articulatory categories provide one input | Language, pronunciation, stress, semantics and stylistic choices |
| [Dynamics and vibrato](body-of-knowledge-outline.md#dynamics-and-vibrato) | Source/filter distinctions identify amplitude and frequency as different variables | Time-varying expressive patterns and relevant perceptual/production accounts |
| [Repertoire selection](body-of-knowledge-outline.md#repertoire-selection) | Tonal transposition explains one change to demands | Pending demand-suitability representation; no automatic song recommendation |
| [Phrasing](body-of-knowledge-outline.md#phrasing) | Timing, text and respiratory interfaces are distinguished | Pending musical/linguistic grouping, emphasis, continuity and interpretation account |
| [Style and musical context](body-of-knowledge-outline.md#style-and-musical-context) | Every current Model states its tradition and scope limits | Tradition-specific evidence and multiple valid expressive conventions |
| [Singing with others and presenting](body-of-knowledge-outline.md#singing-with-others-and-presenting) | Shared pulse is representable | Interpersonal coordination, cues, accompaniment and communication |
| [Melody harmony and musical form](body-of-knowledge-outline.md#melody-harmony-and-musical-form) | Pitch, timing and major-scale roles describe selected ingredients | Harmonic function, larger structure, melodic grouping and their interaction |
| [Learning and feedback](body-of-knowledge-outline.md#learning-and-feedback) | Matching architecture separates functions; Method preserves uncertainty | Mechanisms of durable change, feedback scheduling, retention and transfer |
| [Notation and sight singing](body-of-knowledge-outline.md#notation-and-sight-singing) | Musical coordinates explain what a notation could represent | A complete reading/decoding Model and notation-to-action instruction; still optional |

## Worked trace across Models

Consider a constructed case, not a learner observation: a requested fragment has a declared major-scale context, three pitches and a four-beat timeline. The last beat is a rest. A listener says a second rendition sounds different.

The pitch Model asks whether heights, intervals and contour changed. The tonal Model asks whether the declared context changed: the same class can have a different degree without changing frequency. The rhythm/metre Model asks whether the sounds occurred at the intended positions and whether the rest retained its place in the pulse. These comparisons require specifying the target; different is not yet an error diagnosis.

Suppose the intended pitches and timing stayed fixed while a vowel changed. Articulatory features identify a possible configuration contrast. The source-filter representation shows that different spectral balances can follow from different responses even with the same source fundamental under its approximation. The production Model reminds us that actual source and tract can interact, so this does not prove that only the filter changed.

The auditory Model separates the returned sound, its perception and the comparison decision. If the listener cannot distinguish pitch from tone-colour differences, uncertainty is the correct evidence state. The existing comparison Method offers a bounded next action rather than inventing a physiological cause. If comfort or voice changes are a concern, the Practice's stopping boundary overrides pursuing a musical match.

Now add lyrics with a stress conflict, a difficult sustained register or an ensemble cue. The current Models identify interfaces where these demands enter, but do not solve them. The corresponding coverage remains pending. A useful architecture shows both the explanatory path and where it ends.

## Purposeful next development groups

These are scoped development questions, not scheduled work or promised completion. Inspect suitable accounts before deciding final file boundaries.

| Group | Questions that justify joint development | Boundary decision still to make |
|---|---|---|
| Words and musical phrasing | How do syllables, stress, articulatory timing and musical grouping interact? | Keep feature descriptions reusable; split text setting from phrasing only if each supports distinct cases without losing their connection |
| Individual instrument and task demands | How do variation, register accounts, range/tessitura and repeated song demands constrain a choice? | Do not turn voice-type labels or a range test into health clearance; classification may need several scoped accounts |
| Musical and social context | How do harmony, form, style, accompaniment and other performers shape an interpretation? | Multiple traditions and coordination accounts may be needed rather than one universal performance Model |
| Learning and representation | What distinguishes immediate performance from retained skill, and optional score decoding from auditory imitation? | Refine the existing matching architecture where appropriate; do not treat it as a complete motor-learning or reading theory |

The first groups were selected because they explain existing beginner tasks and create shared interfaces needed by later groups. This is not a requirement that all beginners study acoustics before singing or that later groups are less important.

## Sufficiency and review boundaries

For an implemented explanatory subset, a reader should be able to identify its variables, follow a relationship through a worked case, recognise at least one unsupported inference and state what additional information an interface needs. A list of components, a source citation or a passing parser does not meet that criterion alone.

Author paper walkthroughs used the following cases: changing duration under a fixed flow assumption; one spectrum with multiple source/filter explanations; lip closure with different nasal routing; the same pitch class in two tonal contexts; six subdivisions grouped into two versus three beats; and an octave-related attempt that a class-only display cannot resolve. Arithmetic checks and repository checks are reported separately in the PR. These are editorial self-checks, not independent reader trials, teacher approval or scientific validation.

Broader topic rows remain Partial or pending where the subset cannot answer their full question. No new vocal exercise, personal recording, clinical recommendation or observed learning result is introduced. Principles remain empty rather than manufacturing explanatory laws to complete a role inventory.

## Source alignment and maintenance

The physical group uses selected [respiratory mechanics](../references/betts-2022-process-of-breathing.md), [singing mechanics](../references/wolfe-undated-singing-mechanics.md) and a [measured source-filter experiment](../references/wolfe-2016-measured-source-filter.md). The articulatory group uses [phonetic descriptions](../references/anderson-2022-speech-articulation.md). The musical group uses the linked Open Music Theory and UNSW accounts. The matching group retains the [published proposed framework](../references/pfordresher-2015-singing-accuracy-framework.md).

The existing [NATS](../references/nats-undated-voice-pedagogy-syllabus.md) and [Trinity](../references/trinity-2026-singing-syllabus.md) records provide subject and assessment context, not evidence for the integration or for an exercise's effectiveness. Their retained inspection scopes are not extended by this architecture.

When a Model changes, inspect the other end of each affected interface and the summaries that rely on it. Update the outline's precise coverage cell, then review dependency fingerprints before refresh. Preserve the distinction between what the source establishes, what this architecture chooses and what a learner has actually demonstrated.
