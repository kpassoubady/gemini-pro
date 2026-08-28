# Breakout Evaluation: The Presentation Architect

## Final Result
- Calculated score: **77.5/100**
- Applied cap: **59/100 — no deterministic verification of editable slide generation/repair**; the exercise relies on live Slides/Gemini and fictional text sources.
- Final score: **59/100**
- Rating: **Ineffective: does not yet provide a reliable learning experience**
- Evidence confidence: **medium** for alignment and scaffolding; **low** for live editable-slide behavior
- Delivery recommendation: **redesign evidence layer before slide handoff**
- Strongest aspect: precise source boundary, five-slide plan, bounded repair prompt, and acceptance criteria.
- Greatest learner risk: a polished flattened image or invented source claim may be accepted without inspectable Slides state.
- First correction: provide a bounded source fixture and captured editable before/after slide evidence.

## Evidence Reviewed
| Artifact | Path | Role | Verification status |
|:---|:---|:---|:---|
| Outline | `/Users/kangs/code/github/gemini-pro/catalog/gemini-pro-sequential-outline.md:153-157,203,233` | objective and deliverable | inspected |
| Teaching deck | `/Users/kangs/code/github/gemini-pro/day2/slides/02-advanced-presentation-workflows.md:279-632` | preparation and lab handoff | inspected; no separate breakout deck |
| README | `/Users/kangs/code/github/gemini-pro-companion/day2/breakout-presentation-architect/README.md:1-53` | learner contract | inspected |
| Start/solution | `.../start/presentation-plan.md`, `.../solution/presentation-plan.md`, `.../start/source-extract.md`, `.../solution/source-extract.md` | source and worked plan | inspected |

## Catalog to Exercise Traceability
| Objective or promise | Catalog evidence | Slide preparation | Learner task | Verification | Status |
|:---|:---|:---|:---|:---|:---|
| Source-grounded five-slide plan | outline `:153-157,233` | deck 02 source review | README `:28-35` | plan worksheet and solution; no live source state | partial |
| Repair one editable slide preserving facts | outline `:155-157` | deck 02 repair demo | README `:33-39` | acceptance checklist; no editable slide artifact | partial |
| Distinguish evidence, action, style | outline `:155-157` | deck 02 source/style distinction | README `:30-39` | fictional source extract and worked plan | partial |

## Scorecard
| Dimension | Rating | Weight | Points | Evidence summary |
|:---|---:|---:|---:|:---|
| Catalog alignment and completeness | 4.5 | 15 | 13.5 | Direct match to plan and repair deliverable. |
| Slide grounding and learning progression | 4.5 | 15 | 13.5 | Prerequisite concepts and demos precede lab. |
| Technology fidelity and relevance | 4 | 15 | 12 | Slides/Gemini are appropriate but unexecuted. |
| Authentic hands-on problem solving | 4 | 15 | 12 | Realistic leadership update and evidence repair. |
| Executable contract and technical correctness | 2 | 15 | 6 | Worksheets provide shape, not a deterministic editable-slide check. |
| Engagement, collaboration, and feedback | 4.5 | 10 | 9 | Roles, review, rejection, and share-out are strong. |
| Scaffolding, timing, and participation access | 4 | 10 | 8 | Clear 60-minute phases and fallback. |
| Developer workflow and technical judgment | 3.5 | 5 | 3.5 | Bounded prompt and prohibited claims are explicit. |
| **Total** |  | **100** | **78** |  |

## Critical Conditions and Caps
- Triggered cap 59: no deterministic verification for source selection, editability, reading order, or repair.
- Not triggered: worksheet-only cap; learners are expected to change a Slides artifact.
- Not triggered: starter/solution structural failure.

## Technical Verification
| Command or check | Expected | Actual | Result |
|:---|:---|:---|:---|
| Inventory README/start/solution | complete exercise tree | Present | pass |
| `git diff --check` in primary | clean | clean | pass |
| Run Slides source/repair task | editable plan and repaired slide | Requires authenticated Google Slides/Gemini; no captured deck | unverified |
| Compare starter and solution | scaffold/answer parity | Present as Markdown worksheets | pass for structure |

## Learner Workflow and Time Use
| Phase | Minutes | Learner action | Cognitive mode | Output or feedback |
|:---|---:|:---|:---|:---|
| Brief/roles | 10 | identify decision and roles | individual/constructive | decision hypothesis |
| Source/plan | 22 | inspect sources and revise five-slide plan | interactive | grounded plan |
| Repair | 20 | assemble, prompt, preview, compare | revision | editable slide |
| Governance/share | 8 | verify and share rejected claim/repair | feedback | evidence explanation |

## Findings
### Blockers
1. **No editable Slides artifact or before/after preview is included.** `README.md:24-39`; the core repair can only be verified live. Impact: editability and fact preservation are not provable. Smallest correction: capture a non-sensitive starter and repaired slide, or document a live run with element-level acceptance evidence.
### Major
1. **No deterministic source/claim acceptance fixture.** `start/presentation-plan.md:9-38`; the plan can be filled without proving source inspection. Add a fixed source extract with expected rows and a slide acceptance record.
2. **Live account and feature availability are not tested.** `README.md:24-26`; add prerequisite and fallback steps that preserve the concept without presenting a flattened image as editable.
### Moderate
1. The worked repair embeds dates that should be checked against the authoritative source extract (`solution/presentation-plan.md:22-30`).
2. Stretch alternative-text review has no concrete evidence template (`README.md:43-45`).
### Minor
1. Record the exact deck name and slide number in the learner worksheet.

## What Works
The exercise protects factual integrity, separates style from evidence, bounds the change to one slide, and gives reviewers clear rejection criteria.

## Prioritized Improvement Plan
1. Add deterministic source extract and editable-slide evidence.
2. Test account/setup and flattened-image fallback wording.
3. Add alternative-text and slide-location evidence fields.

## Re-evaluation Checklist
Run the plan and repair in Slides, capture source list, editable element state, before/after preview, fact parity, reading order, and rejected-claim evidence.

## Breakout Slide Handoff
- Status: **blocked pending exercise repair**
- Evaluation report: `/Users/kangs/code/github/gemini-pro/llm-context/issues/20260827-v1-day2-presentation-architect-breakout-evaluation.md`
- Primary repository: `/Users/kangs/code/github/gemini-pro`
- Companion repository: `/Users/kangs/code/github/gemini-pro-companion`
- Companion README: `/Users/kangs/code/github/gemini-pro-companion/day2/breakout-presentation-architect/README.md`
- Outline and placement: `catalog/gemini-pro-sequential-outline.md`, Day 2 Session 11 / Lab 2.2
- Existing deck candidates: none
- Diagram candidates: `/Users/kangs/code/github/gemini-pro/day2/diagrams/presentation-plan-review.{mmd,svg,png}` and `presentation-surface-choice.{mmd,svg,png}`
- Unresolved findings: Blocker `README.md:24-39` no editable artifact; Major `start/presentation-plan.md:9-38` no deterministic source/claim check.
