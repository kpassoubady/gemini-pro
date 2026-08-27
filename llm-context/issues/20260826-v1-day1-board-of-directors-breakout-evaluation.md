# Breakout Evaluation: The Board of Directors

## Final Result
- Calculated score: 79/100
- Applied cap: 59/100 — no deterministic acceptance test or reproducible decision fixture; core output is live Gemini generation.
- Final score: 59/100
- Rating: Ineffective: does not yet provide a reliable learning experience
- Evidence confidence: high
- Delivery recommendation: redesign
- Strongest aspect: three lenses, constraints, evidence-needed fields, and human judgment are unusually well aligned.
- Greatest learner risk: persona prose may be accepted as evidence despite the explicit warning.
- First correction: add a deterministic claim-check worksheet/fixture and a scoring rubric for the final table.

## Evidence Reviewed
| Artifact | Path | Role | Verification status |
|---|---|---|---|
| Catalog | `/Users/kangs/code/github/gemini-pro/catalog/gemini-pro-sequential-outline.md:62-66,126` | objective/deliverable | inspected |
| Slides | `/Users/kangs/code/github/gemini-pro/day1/slides/02-cognitive-frameworks.md:136-188` | prerequisite/demo/lab | inspected |
| Demos | `/Users/kangs/code/github/gemini-pro/day1/demos/03-multi-perspective-decision.md`, `04-multi-perspective-revision.md` | prompt and repair | files inspected; live Gemini unavailable |
| Companion exercise | `/Users/kangs/code/github/gemini-pro-companion/day1/breakout-board-of-directors/` | README/start/solution/verification | inspected |
| Concept | `/Users/kangs/code/github/gemini-pro-companion/day1/concepts/02-cognitive-frameworks.md:6-30` | prerequisite reference | inspected |

## Catalog to Exercise Traceability
| Objective or promise | Catalog evidence | Slide preparation | Learner task | Verification | Status |
|---|---|---|---|---|---|
| Multi-persona decision analysis | outline:64-66 | slides:136-177; demo 03 | README:26-32; start:5-7 | three-role output and consensus table | full |
| Verify factual claims and revise generic advice | outline:64-66 | slides:146-165,181-188; demo 04 | README:31,34-36 | human checkpoint; no deterministic fact set | partial |
| Risks, rewards, recommendation table | outline:66,126 | slide:173-177 | README:7-9,44-46; solution:7-16 | instructor notes:3-11 | full/weak evidence |

## Scorecard
| Dimension | Rating | Weight | Points | Evidence summary |
|---|---:|---:|---:|---|
| Catalog alignment and completeness | 4.5 | 15 | 13.5 | Exact Lab 1.2 promise and decision-table deliverable. |
| Slide grounding and learning progression | 5 | 15 | 15 | Roles, constraints, consensus-not-vote, repair, and verification taught first. |
| Technology fidelity and relevance | 4 | 15 | 12 | Gemini prompt is the mechanism; account feature/source checking is live. |
| Authentic hands-on problem solving | 4 | 15 | 12 | Low-risk workplace decision with meaningful constraints and rejected alternative. |
| Executable contract and technical correctness | 2 | 15 | 6 | Strong written acceptance fields, no deterministic test or authoritative fixture. |
| Engagement, collaboration, and feedback | 4.5 | 10 | 9 | private prediction, rotating roles, revision, checkpoint, share-out. |
| Scaffolding, timing, and participation access | 4 | 10 | 8 | clear phases and safe scope; decision selection may consume time. |
| Developer workflow and technical judgment | 3.5 | 5 | 3.5 | bounded prompt and critique, but no exact evidence-based repair input. |
| **Total** |  | **100** | **79** | |

## Critical Conditions and Caps
The no-deterministic-verification condition applies: Markdown-only artifacts contain no tests, source set, or reproducible expected claims. The live model is explicitly not independent evidence. Apply the 59 cap; no starter/solution command exists.

## Technical Verification
| Command or check | Expected | Actual | Result |
|---|---|---|---|
| `find .../day1 -maxdepth 4 -type f` | four exercise artifacts | README, start, solution, verification present | pass |
| `git diff --check` | clean | no output | pass |
| Run start/solution/tests | runnable artifact and focused test | prompts and Markdown example only; no tests/runtime | unverified/not applicable |
| Run multi-persona prompt and fact check | reproducible role output and authoritative claim check | requires live Gemini and user-selected external sources | unverified |

## Learner Workflow and Time Use
| Phase | Minutes | Learner action | Cognitive mode | Output/feedback |
|---|---:|---|---|---|
| Predict/define | 10 | choose decision; predict risk; set constraints | constructive | individual hypothesis |
| First prompt | 15 | run three lenses | active | candidate analyses |
| Repair | 15 | check claims; differentiate generic roles | interactive | revised prompt |
| Synthesis | 10 | complete consensus table | constructive | recommendation/caveats |
| Share-out | 10 | defend tradeoff/rejected option | interactive | feedback |

## Findings
### Blockers
None for a live classroom session.

### Major
1. **No reproducible claim-verification contract.** Affected `README.md:26-46`, `solution/verification.md:3-11`. “At least one factual claim” is not tied to a supplied authoritative source or expected answer, so a reviewer cannot reliably assess verification. Add a synthetic decision packet with 2–3 checkable facts and an answer key, while keeping learner judgment open for the recommendation.

### Moderate
1. **Decision setup can overrun the 60-minute budget.** `README.md:22-32` leaves decision, context, and three constraints entirely to groups; provide a fallback menu with prewritten scenario cards.
2. **Completion levels lack observable scoring.** `README.md:40-46` should specify required evidence for distinct lenses, revision, and rejected alternative.

### Minor
1. `solution/consensus-table.md:3-5` says fictional but should repeat “illustrative, not expected literal output” next to the table.

## What Works
Excellent alignment with the outline and slides; explicit non-independence warning, safety boundary, role differentiation, assumptions, confidence, unresolved questions, rejected alternative, and useful share-out.

## Prioritized Improvement Plan
1. Add a small synthetic evidence packet and claim-check key.
2. Add scenario cards and a lightweight acceptance rubric.
3. Clarify illustrative status of the solution.

## Re-evaluation Checklist
- Run a supplied low-risk scenario with three constraints.
- Confirm roles produce distinct concerns and a revised prompt addresses generic output.
- Verify one factual claim against the supplied authoritative source.
- Check recommendation, confidence, unresolved question, and rejected alternative.

## Breakout Slide Handoff
- Status: blocked pending exercise repair
- Evaluation report: `/Users/kangs/code/github/gemini-pro/llm-context/issues/20260826-v1-day1-board-of-directors-breakout-evaluation.md`
- Primary repository: `/Users/kangs/code/github/gemini-pro`
- Companion repository: `/Users/kangs/code/github/gemini-pro-companion`
- Companion README: `/Users/kangs/code/github/gemini-pro-companion/day1/breakout-board-of-directors/README.md`
- Outline and placement: `/Users/kangs/code/github/gemini-pro/catalog/gemini-pro-sequential-outline.md`, Day 1 Session 2 / Lab 1.2
- Existing deck candidates: `/Users/kangs/code/github/gemini-pro/day1/slides/02-cognitive-frameworks.md`
- Diagram candidates: none found
- Unresolved findings: Major — no reproducible claim-verification contract; Moderate — scenario setup/timing and scoring rubric
