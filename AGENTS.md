---
language: "KPS 9.x"
package_version: "0.1.0"
status: "draft"
reviewed: null
---

# Agent guidance

## Key takeaway

Apply the shared Core Engineering Principles with this package's beginner scope, evidence boundaries and declared KPS compatibility.

## Summary

These instructions apply repository-wide to knowledge, code, tools and workflows. The nine Core Engineering Principles are maintained verbatim across the knowledge projects; propose shared revisions together and keep singing-specific guidance below. This local copy supports independent use. These are working agreements, not scientific KPS Principle objects or a second authoring specification.

## Project purpose

Help beginners understand singing and undertake comfortable, observable tasks, from initial sounds to preparing a suitable song. Use the [Body of Knowledge Outline](docs/body-of-knowledge-outline.md) for required topics, depth, relationships and coverage gaps; use [First singing session](practices/first-singing-session.md) or [Learn and perform a song](practices/learn-and-perform-a-song.md) for the selected task's activity order and entry conditions. The wider outline does not expand the implemented beginner scope or certify a singer's competence.

## Core Engineering Principles

1. **Self-contained knowledge.** Make each substantive document understandable on its own: explain the problem, essential terms, prerequisites, mechanisms, examples, and boundaries. Link to deeper material without requiring readers to follow links to understand the core argument. Keep canonical definitions in one place; avoid needless duplication.

2. **Reader-centered quality.** Evaluate whether a reader can explain *what happens, how, why, and when*; apply the knowledge to a realistic problem; predict likely outcomes and failure modes; and recognize opportunities to improve results. Correctness and clear reasoning matter more than polished prose.

3. **Goal-oriented work.** Identify the intended reader outcome before substantial work. Choose the smallest sufficient change; prioritize important knowledge gaps and useful results. Avoid speculative infrastructure, redundant research, unnecessary documentation, and rituals that do not advance the goal. Do not skip essential verification to save effort.

4. **Reuse before invention.** Look for established theory, standards, sources, methods, libraries, and tools before building alternatives. Prefer suitable, proven approaches; weigh fitness, reliability, cost, maintenance, and lock-in. Create custom solutions only when a material requirement justifies them.

5. **Mechanisms before memorization.** Explain causal relationships, relevant variables, assumptions, boundary conditions, and trade-offs. Show how the mechanism informs decisions and practical action. Surface possible improvements and testable hypotheses, clearly separating proposed innovations from demonstrated results.

6. **Delete obsolete internal compatibility.** When replacing internal code, paths, workflows, or knowledge structures, migrate affected uses and remove superseded implementations. Do not add internal legacy shims, deprecated aliases, dual-write logic, or competing canonical documents. Assess *external* contracts separately and honor actual obligations. Preserve unique evidence, provenance, and historically useful knowledge; remove obsolete representations, not valuable facts.

7. **Fix the problem class.** For defects or inconsistencies, identify the underlying cause and check for related instances. Make the smallest coherent change that addresses the confirmed class; add proportionate checks or regression coverage where useful. Do not turn isolated issues into speculative redesigns.

8. **Think before acting.** Before substantive work, clarify the intended outcome, inspect relevant context, challenge important assumptions, and consider dependencies, risks, and the simplest sound approach. Scale planning to the task: small, reversible changes need no formal plan; consequential or hard-to-reverse changes deserve more analysis. Avoid analysis that does not improve the decision.

9. **Test the core first; validate by risk.** First verify the main outcome: for software, the changed behavior; for knowledge, whether a reader can use it to reason through a representative problem. Expand to affected dependencies, contracts, edge cases, or regressions when the likelihood and impact of failure justify it. Prefer focused checks over redundant tests or unrelated full suites; never omit essential verification merely to save time.

## Project guidance

- Follow the [pinned Core authoring contract](https://github.com/xiongxianfei/knowledge-practice-system/blob/6a6e7aedc24581769fad435f4943856c1060e02a/docs/authoring.md), [README](README.md) and [publication metadata](publication.json). Retain KPS 9.x, the declared steps-first format and the current checker pin unless a compatibility change is explicitly part of the task.
- Reuse established subject structure for the target Practice. Preserve the five primary knowledge roles and useful explanatory overlap. References are publication records. Empty role folders are acceptable; do not manufacture objects to fill them.
- Maintain the authored Body of Knowledge Outline from established accounts and intended Practices. Define required coverage and expected depth before mapping existing explanations and gaps. Retain required topics without local documents and explain important connections. Practices own their learning activities and prerequisites. A syllabus is evidence for an outline, not proof of an exercise's effectiveness.
- Inspect sources for changed claims and record the exact passage and access extent. Separate source statements, authored adaptations, synthetic examples and actual learner observations. Preserve terminology, musical tradition and style limits; Western notation is not universal. Do not invent source inspection, recording analysis, session results, clinical clearance or independent review.
- Preserve the [Practice starting conditions](practices/first-singing-session.md#starting-conditions) and [voice-care evidence](references/nidcd-2025-taking-care-of-your-voice.md). Do not diagnose disorders, prescribe rehabilitation or encourage singing through pain, hoarseness or fatigue. Comfort observations do not establish medical safety. Changes to vocal procedures need evidence and appropriate human judgment; structural checks do not supply it.
- Keep essential rationale, action, observation and fallback inline in `StageN` stages. A contour task is not an assessment of accurate pitch matching. Preserve an explicitly blank current summary until a real session supplies observations.
- Keep personal recordings, health information and identifiable learner records outside the public repository unless their publication is explicitly authorized. Do not copy restricted scores, lyrics, recordings, figures or full publications. A citation does not grant reuse rights.

## Verification

Use the same pinned KPS 9.1.0 validator as the existing [CI workflow](.github/workflows/validate.yml). From the repository root, obtain a temporary copy and run it:

```bash
singing_validator="$(mktemp)"
curl --fail --location --silent --show-error --retry 3 \
  https://raw.githubusercontent.com/xiongxianfei/knowledge-practice-system/6a6e7aedc24581769fad435f4943856c1060e02a/validate.py \
  --output "$singing_validator" && python3 "$singing_validator" .
```

The initial fetch requires network access; a previously verified copy can be reused offline. Ordinary reading needs no script or sibling checkout. There is no local test suite to invoke. The checker verifies structure, links and declared dependencies, not voice health, singing quality or learning effectiveness.

For guidance and navigation edits, also check local link targets, heading fragments and exact equality of the shared principles. For knowledge or Practice edits, inspect source meaning, local explanations and affected receiving summaries before accepting new dependency fingerprints. Do not run `--accept-reviewed-summaries` merely to silence a failure. Distinguish actual local results, remote CI and human review.

## Contribution workflow

Inspect branch, status and existing work before editing. Keep a change focused and reviewable; use one branch and one PR to `main` for a requested publication. Follow the user's existing authorization without inventing approval, merges or releases. Preserve unrelated work and avoid force-rewriting shared history. Write new text in LF and keep unrelated line-ending changes out of the patch. Do not change knowledge, checker pins or dependency snapshots as a side effect of a navigation update. Keep the coverage outline and this file as maintained Markdown; no generator is needed.
