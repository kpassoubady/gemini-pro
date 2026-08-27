# Breakout Evaluation: The Workspace Sorcerer

## Final Result
- Calculated score: 78/100
- Applied cap: 59/100 — no deterministic Sheet/Docs artifact, formula test, or reproducible acceptance check; Workspace execution is live.
- Final score: 59/100
- Rating: Ineffective: does not yet provide a reliable learning experience
- Evidence confidence: high
- Delivery recommendation: redesign
- Strongest aspect: the tracker-to-announcement handoff and human approval gate directly match the catalog.
- Greatest learner risk: a Sheet can look complete while its dropdown range/formula or announcement facts are wrong.
- First correction: provide a copyable fixture/template and exact formula/dropdown/announcement acceptance checks.

## Evidence Reviewed
| Artifact | Path | Role | Verification status |
|---|---|---|---|
| Catalog | `/Users/kangs/code/github/gemini-pro/catalog/gemini-pro-sequential-outline.md:98-104,130` | objective/deliverable | inspected |
| Slides | `/Users/kangs/code/github/gemini-pro/day1/slides/124-178` | demos/lab/gate/fallback | inspected |
| Demos | `/Users/kangs/code/github/gemini-pro/day1/demos/11-sheets-project-tracker.md`, `12-docs-announcement-handoff.md` | native Workspace workflow | files inspected; live Workspace unavailable |
| Companion exercise | `/Users/kangs/code/github/gemini-pro-companion/day1/breakout-workspace-sorcerer/` | README/start/solution/verification | inspected |
| Concept | `/Users/kangs/code/github/gemini-pro-companion/day1/concepts/06-native-workspace-in-app-automation.md` | prerequisite reference | file exists; reviewed as source map |

## Catalog to Exercise Traceability
| Objective or promise | Catalog evidence | Slide preparation | Learner task | Verification | Status |
|---|---|---|---|---|---|
| Formula-driven tracker with required fields/statuses/date cases | outline:100-102,130 | slides:124-132,146-165; demo 11 | README:29-35; start:5-9 | known past/current/future tests | full/weak evidence |
| Announcement from confirmed tracker facts | outline:100-102 | slides:136-165; demo 12 | README:34-40; start:11-17 | compare every fact with Sheet | full/weak evidence |
| Human approval/reflection and feature fallback | outline:102 | slides:158-178 | README:21,27,38-50 | approval/unresolved item | full |

## Scorecard
| Dimension | Rating | Weight | Points | Evidence summary |
|---|---:|---:|---:|---|
| Catalog alignment and completeness | 4.5 | 15 | 13.5 | Exact tracker, announcement, verification, reflection promise. |
| Slide grounding and learning progression | 4.5 | 15 | 13.5 | Blank Sheet/Doc, formula/dropdown checks, handoff, approval, fallback taught. |
| Technology fidelity and relevance | 4.5 | 15 | 13.5 | Native Sheets/Docs are indispensable; manual fallback preserves fields. |
| Authentic hands-on problem solving | 4 | 15 | 12 | launch-readiness workflow is coherent and workplace relevant. |
| Executable contract and technical correctness | 2 | 15 | 6 | no actual Sheet/Doc fixture, formula test, or exportable acceptance artifact. |
| Engagement, collaboration, and feedback | 4.5 | 10 | 9 | prediction, rotating builder, verifier, fact/formula checks, reflection. |
| Scaffolding, timing, and participation access | 3.5 | 10 | 7 | fallback exists, but blank-artifact setup and two-app handoff are tight in 60 minutes. |
| Developer workflow and technical judgment | 3.5 | 5 | 3.5 | explicit inspection and approval; no exact failure-driven repair. |
| **Total** |  | **100** | **78** | |

## Critical Conditions and Caps
No deterministic verification exists for formulas, dropdown ranges, date cases, or cross-document fact fidelity. The artifacts are Markdown-only and live Workspace is unavailable here. Apply the 59 cap.

## Technical Verification
| Command or check | Expected | Actual | Result |
|---|---|---|---|
| `find .../day1 -maxdepth 4 -type f` | four exercise artifacts | present | pass |
| `git diff --check` | clean | no output | pass |
| Run start/solution/tests | runnable tracker/Doc and focused checks | prompts/examples only; no tests/runtime | unverified/not applicable |
| Build Sheet and Doc; test dates/dropdowns/facts | observable Workspace behavior | requires authorized account | unverified |

## Learner Workflow and Time Use
| Phase | Minutes | Learner action | Cognitive mode | Output/feedback |
|---|---:|---|---|---|
| Setup/predict | 10 | open blank artifacts; predict risk; assign roles | constructive | risk hypothesis |
| Tracker | 25 | create fields; test statuses/formula/date cases | active/constructive | verified Sheet |
| Announcement | 13 | draft and cross-check facts | constructive | reviewed Doc |
| Share/reflection | 12 | show control, trace fact, transfer workflow | interactive | feedback |

## Findings
### Blockers
None for live Workspace users with fallback; missing executable acceptance evidence blocks handoff.

### Major
1. **No reproducible Workspace acceptance artifact.** Affected `README.md:29-50`, `solution/verification.md:3-10`. The required formula, dropdown, date cases, and cross-document fact trace cannot be verified from Markdown. Add a copyable instructor template or synthetic fixture, exact expected date outputs relative to a fixed reference date, dropdown-range check, and announcement fact checklist.

### Moderate
1. **Two blank artifacts plus AI/manual creation are tight in 60 minutes.** `README.md:11-27`. Provide a pre-staged template as the basic path and creation-from-blank as intermediate/stretch.
2. **Formula semantics are underspecified.** `start/workflow.md:5-9` says “days from today” but does not define blank/invalid dates or timezone/reference behavior. State the expected formula behavior and edge cases.

### Minor
1. `solution/tracker-and-announcement.md:9-11` has date-dependent numeric outputs that will become stale; provide a fixed evaluation date or use formulas/relative expected values.

## What Works
Direct catalog match, actual native tools, manual fallback, three date cases, source-only announcement rule, human approval, and transfer reflection are strong.

## Prioritized Improvement Plan
1. Add a fixture/template and fixed-date acceptance checks.
2. Stage the basic path and define formula edge cases.
3. Make solution date outputs reproducible.

## Re-evaluation Checklist
- Create/copy the tracker and confirm all fields/status values.
- Test fixed past/current/future dates and formula range/blank behavior.
- Trace every announcement date/owner/status/action to the Sheet.
- Confirm approval/unresolved item and fallback behavior.

## Breakout Slide Handoff
- Status: blocked pending exercise repair
- Evaluation report: `/Users/kangs/code/github/gemini-pro/llm-context/issues/20260826-v1-day1-workspace-sorcerer-breakout-evaluation.md`
- Primary repository: `/Users/kangs/code/github/gemini-pro`
- Companion repository: `/Users/kangs/code/github/gemini-pro-companion`
- Companion README: `/Users/kangs/code/github/gemini-pro-companion/day1/breakout-workspace-sorcerer/README.md`
- Outline and placement: `/Users/kangs/code/github/gemini-pro/catalog/gemini-pro-sequential-outline.md`, Day 1 Session 6 / Lab 1.6
- Existing deck candidates: `/Users/kangs/code/github/gemini-pro/day1/slides/06-native-workspace-in-app-automation.md`
- Diagram candidates: none found
- Unresolved findings: Major — no reproducible Workspace acceptance artifact; Moderate — timing and formula semantics
