# Breakout Evaluation: The Inbox Interrogation

## Final Result
- Calculated score: 77.5/100
- Applied cap: 59/100 — no deterministic acceptance test or reproducible source fixture; the core behavior depends on live Gemini/Gmail/Drive access.
- Final score: 59/100
- Rating: Ineffective: does not yet provide a reliable learning experience
- Evidence confidence: high
- Delivery recommendation: redesign
- Strongest aspect: the exercise tightly mirrors the catalog's Gmail-to-Drive evidence workflow.
- Greatest learner risk: a polished report can appear correct without a reproducible way to verify retrieval, recency, or source mapping.
- First correction: provide a prepared fixture/checkable acceptance rubric or instructor-run verification protocol with exact expected source identifiers.

## Evidence Reviewed
| Artifact | Path | Role | Verification status |
|---|---|---|---|
| Catalog | `/Users/kangs/code/github/gemini-pro/catalog/gemini-pro-sequential-outline.md:54-60,123-130` | objective, placement, deliverable | inspected |
| Teaching slide | `/Users/kangs/code/github/gemini-pro/day1/slides/01-connected-workspace-data-retrieval.md:200-239` | demos, lab, privacy | inspected |
| Demo | `/Users/kangs/code/github/gemini-pro/day1/demos/01-connected-retrieval-prompt.md:7-26` | prompt and source-check model | inspected |
| Demo | `/Users/kangs/code/github/gemini-pro/day1/demos/02-connected-retrieval-verification.md` | stale-source repair | file exists; not runnable without Workspace |
| Companion README/start/solution | `/Users/kangs/code/github/gemini-pro-companion/day1/breakout-inbox-interrogation/` | learner contract and example | inspected |
| Companion concept | `/Users/kangs/code/github/gemini-pro-companion/day1/concepts/01-connected-workspace-data-retrieval.md:6-32` | prerequisite reference | inspected |

## Catalog to Exercise Traceability
| Objective or promise | Catalog evidence | Slide preparation | Learner task | Verification | Status |
|---|---|---|---|---|---|
| Retrieve and cross-reference Gmail and Drive/Docs | outline:58-60; deliverable:125 | slides:200-231; demo:01 lines 9-22 | README:36-40; start:5-7 | open original sources; no executable test | partial |
| Distinguish evidence from inference and identify blockers | outline:58-60 | slides:176-194 | README:42-44,52-54 | required fields and verifier questions | full/weak evidence |
| Produce concise status report | outline:60,125 | slide:227 | README:7-9,34-40 | solution:5-14; instructor notes:5-13 | full |
| Correct stale/weak retrieval | outline:58 | slides:211-219 | README:15,39; solution:12-14 | observed learner correction only | partial |

## Scorecard
| Dimension | Rating | Weight | Points | Evidence summary |
|---|---:|---:|---:|---|
| Catalog alignment and completeness | 4.5 | 15 | 13.5 | Exact Lab 1.1 deliverable and 60-minute placement. |
| Slide grounding and learning progression | 4.5 | 15 | 13.5 | Retrieval, recency, evidence/inference, and privacy precede lab. |
| Technology fidelity and relevance | 4 | 15 | 12 | Actual `@Gmail` and `@Google Drive` are central, but live availability is assumed. |
| Authentic hands-on problem solving | 4 | 15 | 12 | Northstar catch-up scenario and source repair are authentic; no supplied fixture. |
| Executable contract and technical correctness | 2 | 15 | 6 | Detailed fields exist, but no deterministic test, command, or classroom source dataset. |
| Engagement, collaboration, and feedback | 4.5 | 10 | 9 | private prediction, rotating roles, verification checkpoint, share-out. |
| Scaffolding, timing, and participation access | 4 | 10 | 8 | Clear 60-minute phases and prepared-sample fallback; account access remains a risk. |
| Developer workflow and technical judgment | 3.5 | 5 | 3.5 | Prompt is bounded and asks for repair, but lacks reproducible failure evidence. |
| **Total** |  | **100** | **77.5** | The weighted points sum to 77.5 before cap. |

## Critical Conditions and Caps
The `no deterministic verification exists for the core behavior` condition is triggered: all companion artifacts are Markdown, there are no tests or fixtures, and Gmail/Drive retrieval requires a live account. The 59 cap is applied. No technical start/solution command exists; source inspection is not execution.

## Technical Verification
| Command or check | Expected | Actual | Result |
|---|---|---|---|
| `find /Users/kangs/code/github/gemini-pro-companion/day1 -maxdepth 4 -type f` | README, start, solution, verification present | all four present for this breakout | pass |
| `git diff --check` in primary repo | no whitespace errors | no output | pass |
| Run starter/solution/tests | runnable deterministic artifact and focused test | Markdown prompts/examples only; no tests or runtime | unverified/not applicable |
| Live `@Gmail`/`@Google Drive` retrieval | prepared sources resolve and dates match | cannot execute without authorized Workspace account | unverified |

## Learner Workflow and Time Use
| Phase | Estimated minutes | Learner action | Cognitive mode | Output or feedback |
|---|---:|---|---|---|
| Predict/setup | 10 | predict blocker; assign roles; open sample | constructive/interactive | initial hypothesis |
| Retrieval | 15 | run scoped cross-app prompt | active | candidate report |
| Inspect/repair | 15 | open sources; repair stale or generic result | interactive | corrected evidence |
| Report/check | 10 | fill fields and verify claims | constructive | status report |
| Share-out | 10 | show evidence, inference, next check | interactive | peer/instructor feedback |

## Findings
### Blockers
None that make the written activity impossible.

### Major
1. **Missing deterministic acceptance evidence.** Affected: `breakout-inbox-interrogation/README.md:34-54`, `solution/verification.md:5-13`. The exercise requires live retrieval but supplies no prepared Gmail/Drive fixture, expected thread/document identifiers, test harness, or instructor answer key. Learners and reviewers cannot distinguish a retrieval failure from a correct empty/older result. Add a non-sensitive fixture manifest with expected source dates/IDs and a repeatable instructor verification checklist; do not expose private data.

### Moderate
1. **Source setup is instructor-dependent.** Affected: `README.md:28-32`. “Instructor-provided” data is not linked or described enough to let a substitute instructor stage it. Add fixture naming, access preflight, and a no-live-service transcript fallback.
2. **Intermediate completion target is not operationalized.** Affected: `README.md:48-50`. “Two blockers” and “repaired prompt” have no scoring evidence. Add a small acceptance rubric.

### Minor
1. `solution/status-report.md:7-8` uses fictional dates that could be mistaken for literal expected output. Label them as illustrative in the heading/table or provide a fixture-specific answer key.

## What Works
Exact catalog deliverable, strong source/evidence/inference separation, privacy guidance, role rotation, source opening, stale-result repair, and a concise share-out all align with slides and engagement standards.

## Prioritized Improvement Plan
1. Add a prepared synthetic source manifest and expected identifiers plus a transcript fallback; this removes the verification cap and makes access failures diagnosable.
2. Add a 4-item acceptance rubric for source recency, field completeness, evidence/inference labels, and correction note.
3. Make the solution explicitly illustrative versus fixture-specific.

## Re-evaluation Checklist
- Run the documented fallback or prepared Workspace scenario.
- Confirm latest thread/document identifiers and expected Phase 1 mapping.
- Verify a deliberately stale result is corrected.
- Check a submission against the acceptance rubric and privacy boundary.

## Breakout Slide Handoff
- Status: blocked pending exercise repair
- Evaluation report: `/Users/kangs/code/github/gemini-pro/llm-context/issues/20260826-v1-day1-inbox-interrogation-breakout-evaluation.md`
- Primary repository: `/Users/kangs/code/github/gemini-pro`
- Companion repository: `/Users/kangs/code/github/gemini-pro-companion`
- Companion README: `/Users/kangs/code/github/gemini-pro-companion/day1/breakout-inbox-interrogation/README.md`
- Outline and placement: `/Users/kangs/code/github/gemini-pro/catalog/gemini-pro-sequential-outline.md`, Day 1 Session 1 / Lab 1.1
- Existing deck candidates: `/Users/kangs/code/github/gemini-pro/day1/slides/01-connected-workspace-data-retrieval.md`
- Diagram candidates: none found
- Unresolved findings: Major — missing deterministic acceptance evidence; Moderate — instructor-dependent fixture and unoperationalized completion target
