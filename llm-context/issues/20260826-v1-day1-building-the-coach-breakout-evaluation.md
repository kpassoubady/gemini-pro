# Breakout Evaluation: Building the Coach

## Final Result
- Calculated score: 79.5/100
- Applied cap: 59/100 — no deterministic Gem/Canvas behavior test or reproducible draft fixture; core work requires live Gemini features.
- Final score: 59/100
- Rating: Ineffective: does not yet provide a reliable learning experience
- Evidence confidence: high
- Delivery recommendation: redesign
- Strongest aspect: the contract, varied-draft test, selective edit, and writer approval form a coherent human-control loop.
- Greatest learner risk: “tested” Gem behavior and meaning preservation are judged without a supplied pair of drafts or observable acceptance criteria.
- First correction: add two synthetic draft fixtures, expected contract checks, and a Canvas review rubric.

## Evidence Reviewed
| Artifact | Path | Role | Verification status |
|---|---|---|---|
| Catalog | `/Users/kangs/code/github/gemini-pro/catalog/gemini-pro-sequential-outline.md:92-96,129` | objective/deliverable | inspected |
| Slides | `/Users/kangs/code/github/gemini-pro/day1/slides/05-persistent-personas.md:135-175` | demo/lab/human control | inspected |
| Demos | `/Users/kangs/code/github/gemini-pro/day1/demos/09-relentless-editor-gem.md`, `10-canvas-selective-edit.md` | Gem and Canvas workflow | files inspected; live features unavailable |
| Companion exercise | `/Users/kangs/code/github/gemini-pro-companion/day1/breakout-building-the-coach/` | README/start/solution/verification | inspected |
| Concept | `/Users/kangs/code/github/gemini-pro-companion/day1/concepts/05-persistent-personas.md` | prerequisite reference | file exists; reviewed as source map |

## Catalog to Exercise Traceability
| Objective or promise | Catalog evidence | Slide preparation | Learner task | Verification | Status |
|---|---|---|---|---|---|
| Create reusable Gem with role and working style | outline:94-96 | slides:135-141,155-163; demo 09 | README:26-31; start:5-11 | saved Gem and two tests | full |
| Refine selected paragraph in Canvas while preserving meaning | outline:94-96 | slides:145-151,167-175; demo 10 | README:32-37; solution:18-20 | original/revised and human decision | full/weak evidence |
| Saved Gem plus polished draft | outline:129 | slide:159-163 | README:7-9,45-47 | instructor notes:3-9 | full |

## Scorecard
| Dimension | Rating | Weight | Points | Evidence summary |
|---|---:|---:|---:|---|
| Catalog alignment and completeness | 4.5 | 15 | 13.5 | Direct match to Gem and Canvas deliverable. |
| Slide grounding and learning progression | 5 | 15 | 15 | Gem contract, varied tests, Canvas selection, and human control taught first. |
| Technology fidelity and relevance | 4 | 15 | 12 | Gems/Canvas are the actual tools; availability varies by account. |
| Authentic hands-on problem solving | 4 | 15 | 12 | recurring editing/coaching task with meaning/voice constraint. |
| Executable contract and technical correctness | 2 | 15 | 6 | Markdown contract and example; no fixtures, runnable test, or Canvas artifact. |
| Engagement, collaboration, and feedback | 4.5 | 10 | 9 | failure-mode prediction, roles, revision, review, share-out. |
| Scaffolding, timing, and participation access | 4 | 10 | 8 | flexible task choice and 60-minute phases; feature access risk remains. |
| Developer workflow and technical judgment | 4 | 5 | 4 | bounded behavior, review-before-save, and rejection of unsupported rewrite. |
| **Total** |  | **100** | **79.5** | The weighted points sum to 79.5 before cap. |

## Critical Conditions and Caps
No deterministic verification exists for Gem response behavior, save state, or Canvas meaning preservation. No draft fixtures or tests are supplied. Apply the 59 cap.

## Technical Verification
| Command or check | Expected | Actual | Result |
|---|---|---|---|
| `find .../day1 -maxdepth 4 -type f` | four exercise artifacts | present | pass |
| `git diff --check` | clean | no output | pass |
| Run start/solution/tests | runnable Gem/Canvas test | Markdown only; no tests/runtime | unverified/not applicable |
| Preview two drafts and Canvas edit | behavior and version evidence | requires live Gemini account/features | unverified |

## Learner Workflow and Time Use
| Phase | Minutes | Learner action | Cognitive mode | Output/feedback |
|---|---:|---|---|---|
| Contract/setup | 15 | select recurring task; define contract | constructive | Gem instructions |
| Test/revise/save | 25 | test two drafts; repair weak behavior | interactive | revised saved Gem |
| Canvas edit | 12 | select paragraph; compare versions | constructive | reviewed edit |
| Review/share | 8 | approve/reject and explain change | interactive | feedback |

## Findings
### Blockers
None for live Gemini users; technical reproducibility gap blocks handoff.

### Major
1. **No deterministic behavior or meaning-preservation contract.** Affected `README.md:26-47`, `solution/verification.md:3-9`. “Tested” and “preserves meaning” cannot be independently assessed without draft fixtures, expected observations, or a Canvas review rubric. Add two non-sensitive drafts (cliché and missing premise), required response signals, and a before/after approval checklist.

### Moderate
1. **Feature availability fallback is absent from companion README.** `README.md:22-24` assumes Gems/Canvas; primary slides:170-175 provide no explicit fallback either. Add a documented manual contract/side-by-side editing fallback and state what it cannot prove.
2. **Task choice can dilute the target editor concept.** `README.md:3-5,24,28` allows code review/client communication/other tasks. Provide a default editing scenario before stretch variants.

### Minor
1. `solution/gem-and-edit.md:3-20` is clearly fictional but should label the Gem as illustrative and distinguish preview from saved state.

## What Works
Strong contract fields, failure-mode testing, meaning/voice boundary, original retention, human approval, role rotation, and share-out.

## Prioritized Improvement Plan
1. Add draft fixtures and a response/Canvas acceptance rubric.
2. Add a fallback path and default scenario.
3. Clarify illustrative solution status.

## Re-evaluation Checklist
- Test the contract against two supplied drafts and record weak response plus revision.
- Confirm save occurs only after preview.
- Compare original and selected Canvas paragraph; document keep/reject/revise decision.
- Run documented fallback if features unavailable.

## Breakout Slide Handoff
- Status: blocked pending exercise repair
- Evaluation report: `/Users/kangs/code/github/gemini-pro/llm-context/issues/20260826-v1-day1-building-the-coach-breakout-evaluation.md`
- Primary repository: `/Users/kangs/code/github/gemini-pro`
- Companion repository: `/Users/kangs/code/github/gemini-pro-companion`
- Companion README: `/Users/kangs/code/github/gemini-pro-companion/day1/breakout-building-the-coach/README.md`
- Outline and placement: `/Users/kangs/code/github/gemini-pro/catalog/gemini-pro-sequential-outline.md`, Day 1 Session 5 / Lab 1.5
- Existing deck candidates: `/Users/kangs/code/github/gemini-pro/day1/slides/05-persistent-personas.md`
- Diagram candidates: none found
- Unresolved findings: Major — no deterministic Gem/Canvas acceptance contract; Moderate — missing fallback and diffuse task choice
