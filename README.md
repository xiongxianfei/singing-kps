---
language: "KPS 9.x"
package_version: "0.4.0"
status: "draft"
---

# Singing KPS

## Key takeaway

Begin with one comfortable, observable singing task rather than memorising an entire singing curriculum.

## Summary

Singing KPS is an independent, source-linked beginner learning package using the Knowledge Practice System authoring language 9.x and the inspected Core 11.0.0 conventions. It offers a first humming and rhythm exercise, an ear-first reference-pitch task and a whole-song preparation Practice. No musical notation, prior training, fixed vocal range or performance experience is assumed.

![Direct singing topics include respiration, pitch relationships, registration, phrasing, repertoire and learning, with selected interfaces; notation and sight singing is optional.](diagrams/body-of-knowledge-overview.png)

The overview summarises the [Body of Knowledge Outline](docs/body-of-knowledge-outline.md). Start with the [complete topic outline](docs/body-of-knowledge-outline.md#overall-outline) to find directly named topics and their subsystem boundaries and interfaces, then follow the coverage tables for required understanding, intended capabilities and gaps. The existing [detailed topic pictures](docs/body-of-knowledge-outline.md#optional-detailed-illustrations) remain optional supporting views. The three Practices support initial exploration, single-note comparison and preparing a suitable song; the outline defines the broader knowledge to develop.

## Start here

Read [First singing session](practices/first-singing-session.md). It offers a gentle three-note contour over four beats, with explicit stop conditions and a simple way to decide what to practise next. An optional voice recorder may help you listen back; the exercise does not require a keyboard or an app.

For an external target, use [Match a reference pitch](practices/match-a-reference-pitch.md): choose a comfortable bundled tone, listen, attempt, compare and decide. Only audio playback is required; recording and tuning tools are optional. Start with [the reference bank](media/reference-pitches/README.md) when checking playback. An uncertain comparison is a valid result, not a reason to keep guessing.

For a complete musical task, use [Learn and perform a song](practices/learn-and-perform-a-song.md). Stand by Me supplies the worked example: select a suitable version, learn phrases, address observed difficulties, connect a verse and chorus, and extend to the whole arrangement. The earlier tasks are optional support, not compulsory prerequisites.

Do not practise through pain, hoarseness, illness-related voice changes or persistent vocal fatigue. The [NIDCD voice care guidance](references/nidcd-2025-taking-care-of-your-voice.md) identifies warning signs and when to seek professional help.

## Model architecture

The [Singing Model architecture](docs/model-architecture.md) connects all 24 outline topics while distinguishing implemented explanations from remaining gaps. Seven Models form the first groups: physical production and acoustic shaping; speech-sound articulation; pitch, rhythm/metre and major-scale context; and auditory-vocal matching. The [collection and boundary decisions](docs/model-architecture.md#current-model-collection-and-boundary-decisions) give each entry point and explain why topics are combined or separated.

The two existing pitch Models are refined rather than replaced. Worked cases connect quantities and decisions without prescribing new vocal exercises. The song Practice adds introductory application for selection, words, phrasing and performance. Detailed explanatory accounts of text setting, individual/register and song demands, broader performance, and durable learning remain incomplete. A beginner does not have to study every Model before using the existing Practices.

## Knowledge coverage

Use the [Body of Knowledge Outline](docs/body-of-knowledge-outline.md) to understand what this subject needs to cover and how deeply. Required topics stay visible even when no local explanation exists. Each Practice supplies its own activity order and entry conditions. The package currently includes:

- [Voice production](concepts/voice-production.md) explains how voiced sound is generated and shaped.
- [Pitch](concepts/pitch.md) distinguishes matching, contour and octave placement without requiring note naming.
- [Pitch relationships](models/pitch-relationships.md) connects pitch height, pitch class, octave and interval in worked comparisons; it separates a matching target from a contour.
- [Intonation](concepts/intonation.md) explains accuracy relative to a target and uncertainty in judging it.
- [Beat and rhythm](concepts/beat-and-rhythm.md) separates the pulse from durations and silence.
- [Verse and chorus](concepts/verse-and-chorus.md) explains section roles, recurring words and music, and why a repeated title alone does not identify a chorus.
- [First singing session](practices/first-singing-session.md) integrates these ideas into a small task.
- [Match a reference pitch](practices/match-a-reference-pitch.md) supplies a selectable audio reference and an observation loop.
- [Learn and perform a song](practices/learn-and-perform-a-song.md) connects component work to a chosen arrangement and a complete-performance review.
- [Reference pitch comparison](methods/reference-pitch-comparison.md) explains replay, direction, optional feedback and uncertainty.
- [Auditory vocal pitch matching](models/auditory-vocal-pitch-matching.md) presents a limited, proposed functional model, not an individual diagnosis.

The Principles directory remains intentionally empty. KPS does not require manufacturing one object per role.

## Evidence and limits

The external References record what was inspected and what the sources do not establish. The exercise order, patterns, reference selection and qualitative reporting are authored KPS applications; they are not a clinically validated protocol or a guarantee of singing improvement. This repo does not assess voice disorders or replace personalised instruction.

## Compatibility

For repository work, follow [Agent guidance](AGENTS.md), including the shared Core Engineering Principles and the pinned validation procedure.

The package targets [KPS Core 11.0.0](https://github.com/xiongxianfei/knowledge-practice-system) and the KPS 9.x authoring format. Its metadata is in [publication.json](publication.json). GitHub Actions runs the structural KPS 9.1.0 validator from a pinned upstream commit. The audio check additionally verifies generated file integrity and pitch, not user playback or singing. A passing structural check does not establish medical safety, factual correctness or learning effectiveness.
