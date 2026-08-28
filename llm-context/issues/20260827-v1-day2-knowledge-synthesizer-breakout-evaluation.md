# Breakout Evaluation: The Knowledge Synthesizer

## Final Result
- Calculated score: **78/100**
- Applied cap: **59/100 — no deterministic verification of generated synthesis, saved notes, study guide, or quiz grounding**; Notebook generation is live and no generated artifacts are supplied.
- Final score: **59/100**
- Rating: **Ineffective: does not yet provide a reliable learning experience**
- Evidence confidence: **medium** for alignment and records; **low** for live synthesis/study-aid generation
- Delivery recommendation: **redesign evidence layer before slide handoff**
- Strongest aspect: explicit statuses, citation verification, unresolved-owner question, and answer-key review.
- Greatest learner risk: a fluent but unsupported synthesis or quiz can be accepted without source-level proof.
- First correction: add a bounded source/claim fixture and captured generated-artifact review.

## Evidence Reviewed
| Artifact | Path | Role | Verification status |
|:---|:---|:---|:---|
| Outline | `/Users/kangs/code/github/gemini-pro/catalog/gemini-pro-sequential-outline.md:177-181,203,235` | objective/deliverable | inspected |
| Teaching deck | `/Users/kangs/code/github/gemini-pro/day2/slides/04-gemini-notebook-synthesis-active-interrogation.md:179-431` | prerequisite and handoff | inspected; no separate breakout deck |
| README | `/Users/kangs/code/github/gemini-pro-companion/day2/breakout-knowledge-synthesizer/README.md:1-53` | learner contract | inspected |
| Start/solution | `.../start/synthesis-record.md`, `.../solution/synthesis-record.md` | matrix, notes, quiz review | inspected |

## Catalog to Exercise Traceability
| Objective or promise | Catalog evidence | Slide preparation | Learner task | Verification | Status |
|:---|:---|:---|:---|:---|:---|
| Comparative questions and claim-evidence matrix | outline `:177-181` | deck 04 synthesis | README `:28-32` | record and worked rows; no generated matrix | partial |
| Save checked notes and preserve uncertainty | outline `:179-181` | deck 04 notes | README `:32-35` | worksheet fields; no Notebook notes | partial |
| Generate study guide and five quiz questions | outline `:179-181,235` | deck 04 study aids | README `:33-35` | worked quiz review; no generated artifacts | partial |

## Scorecard
| Dimension | Rating | Weight | Points | Evidence summary |
|:---|---:|---:|---:|:---|
| Catalog alignment and completeness | 4.5 | 15 | 13.5 | Directly matches Notebook synthesis deliverables. |
| Slide grounding and learning progression | 4.5 | 15 | 13.5 | Citation and study-aid concepts precede lab. |
| Technology fidelity and relevance | 4 | 15 | 12 | Notebook tools are central but unexecuted. |
| Authentic hands-on problem solving | 4 | 15 | 12 | Manager policy enablement is coherent and authentic. |
| Executable contract and technical correctness | 2 | 15 | 6 | Records are strong scaffolds but no generated artifact/test. |
| Engagement, collaboration, and feedback | 4.5 | 10 | 9 | Roles, correction, quiz editing, share-out. |
| Scaffolding, timing, and participation access | 4 | 10 | 8 | Detailed 60-minute sequence. |
| Developer workflow and technical judgment | 4 | 5 | 4 | Strong statuses and source judgment. |
| **Total** |  | **100** | **79** |  |

## Critical Conditions and Caps
- Triggered cap 59: no deterministic verification of synthesis or study-aid artifacts.
- Not triggered: worksheet-only cap; learners must use Notebook generation and saved notes.
- Not triggered: broken starter/solution structure.

## Technical Verification
| Command or check | Expected | Actual | Result |
|:---|:---|:---|:---|
| Inventory records | starter and worked record present | Present | pass |
| `git diff --check` in primary | clean | clean | pass |
| Run matrix/notes/study-aid workflow | generated artifacts with checked citations | Requires live Notebook; none captured | unverified |
| Compare start/solution parity | all record sections represented | Present | pass for structure |

## Learner Workflow and Time Use
| Phase | Minutes | Learner action | Cognitive mode | Output or feedback |
|:---|---:|:---|:---|:---|
| Brief/roles | 10 | predict conflict and assign roles | individual/constructive | conflict hypothesis |
| Matrix/review | 24 | generate and open citations | interactive/revision | checked matrix |
| Notes/aids | 18 | save verified rows and generate guide/quiz | constructive | study aids |
| QA/share | 8 | check keys and explain correction | feedback | evidence share |

## Findings
### Blockers
1. **No generated matrix, saved Notebook notes, study guide, or quiz is included.** `README.md:28-39`; core output and grounding cannot be verified. Correction: capture generated artifacts and source-check evidence from a bounded fixture.
### Major
1. **No deterministic answer-key/source acceptance set.** `start/synthesis-record.md:9-46`; add expected claim statuses, five answer checks, and one intentionally invalid question.
2. **Live Notebook feature availability and export permissions are not tested.** `README.md:24-26`; add a tested fallback and access-control evidence.
### Moderate
1. Basic completion allows three verified claims while the definition of done requires every retained claim (`README.md:41-49`); clarify minimum evidence.
2. Derived-source stretch could amplify errors unless the “not primary evidence” label is mandatory (`README.md:43-45`).
### Minor
1. Add timestamps or artifact IDs for each saved note and quiz revision.

## What Works
The exercise makes disagreement visible, requires passage-level checking, distinguishes derived notes from primary evidence, and gives a meaningful assessment-editor share-out.

## Prioritized Improvement Plan
1. Add bounded expected matrix and answer-key evidence.
2. Capture actual Notebook notes/study aids and permission checks.
3. Clarify basic versus definition-of-done thresholds.

## Re-evaluation Checklist
Run the matrix, open every required citation, save only checked rows, generate guide and five questions, verify one answer per item, and preserve the unresolved rollout question.

## Breakout Slide Handoff
- Status: **blocked pending exercise repair**
- Evaluation report: `/Users/kangs/code/github/gemini-pro/llm-context/issues/20260827-v1-day2-knowledge-synthesizer-breakout-evaluation.md`
- Primary repository: `/Users/kangs/code/github/gemini-pro`
- Companion repository: `/Users/kangs/code/github/gemini-pro-companion`
- Companion README: `/Users/kangs/code/github/gemini-pro-companion/day2/breakout-knowledge-synthesizer/README.md`
- Outline and placement: `catalog/gemini-pro-sequential-outline.md`, Day 2 Session 15 / Lab 2.4
- Existing deck candidates: none
- Diagram candidates: `/Users/kangs/code/github/gemini-pro/day2/diagrams/contradiction-first-synthesis.{mmd,svg,png}`, `verified-notes-study-aids.{mmd,svg,png}`
- Unresolved findings: Blocker `README.md:28-39` no generated artifacts; Major `start/synthesis-record.md:9-46` no deterministic acceptance set.
