# Breakout Evaluation: Knowledge Synthesizer

## Final Result
- Calculated score: 77/100
- Applied cap: 59/100 — live Notebook synthesis, saved notes, study guide, quiz, and citations remain unverified.
- Final score: 59/100
- Rating: Ineffective: live synthesis evidence is not verified
- Evidence confidence: medium offline; low live
- Delivery recommendation: revise before delivery
- Strongest aspect: statuses preserve contradiction and uncertainty.
- Greatest learner risk: authored worked record mistaken for generated Notebook artifacts.
- First correction: capture generated artifacts and checked citations.

## Evidence Reviewed
| Artifact | Path | Role | Verification status |
|---|---|---|---|
| README | `day2/breakout-knowledge-synthesizer/README.md` | Student contract | Repaired/read |
| Records | `start/`, `solution/` | Synthesis/study-aid contract | Read |
| Verifier | `day2/breakout-knowledge-synthesizer/verify_offline.py` | Local acceptance | Executed |
| Prior report | `llm-context/issues/20260827-v1-day2-knowledge-synthesizer-breakout-evaluation.md` | Baseline | Read |

## Catalog to Exercise Traceability
| Objective or promise | Catalog evidence | Slide preparation | Learner task | Verification | Status |
|---|---|---|---|---|---|
| Produce checked matrix | Day 2 Session 15 | Notebook synthesis | Cite/status rows | Local markers pass; live matrix absent | Partial |
| Produce grounded study aids | Session 15 | Active interrogation | Guide and five quiz items | Worked record only; live artifacts absent | Partial |

## Scorecard
| Dimension | Rating | Weight | Points | Evidence summary |
|---|---:|---:|---:|---|
| Catalog alignment | 4 | 15 | 12 | Direct |
| Slide grounding | 4 | 15 | 12 | Existing |
| Technology fidelity | 2 | 15 | 6 | Live Notebook unavailable |
| Hands-on problem | 4 | 15 | 12 | Policy scenario |
| Executable contract | 4 | 15 | 12 | Local verifier pass |
| Engagement/feedback | 4 | 10 | 8 | Review/rewrite |
| Timing/access | 4 | 10 | 8 | 60 minutes |
| Developer judgment | 2 | 5 | 2 | Tool workflow |
| **Total** |  | **100** | **72** |  |

## Critical Conditions and Caps
Live generated-artifact cap applies; local record check is not Notebook execution.

## Technical Verification
| Command or check | Expected | Actual | Result |
|---|---|---|---|
| `python3 verify_offline.py solution/synthesis-record.md` | PASS | All markers found | PASS |
| `python3 verify_offline.py start/synthesis-record.md` | Expected incomplete failure | Missing markers reported | PASS (expected red) |
| Live Notebook run | Matrix/artifacts/citations | Not available | UNVERIFIED |

## Learner Workflow and Time Use
| Phase | Minutes | Learner action | Cognitive mode | Output or feedback |
|---|---:|---|---|---|
| Matrix | 22 | Generate and classify claims | Create/compare | Matrix |
| Evidence | 20 | Open citations and correct rows | Revise | Checked notes |
| Study aids/share | 18 | Generate/check guide and quiz | Feedback | Artifacts |

## Findings
### Blockers
1. Live generated artifacts and citations absent; capture under `evidence/<run-id>/`.
### Major
1. Local verifier validates record labels, not Notebook generation or grounding.
### Moderate
None.
### Minor
None.

## What Works
Explicit four statuses, answer-key review, and unresolved owner question.

## Prioritized Improvement Plan
1. Capture live matrix, notes, study guide, quiz, and citations.

## Re-evaluation Checklist
Run local verifier and independently inspect each live citation/artifact.

## Breakout Slide Handoff
- Status: blocked pending exercise repair
- Evaluation report: `llm-context/issues/20260827-v2-day2-knowledge-synthesizer-breakout-evaluation.md`
- Primary repository: `/Users/kangs/code/github/gemini-pro`
- Companion repository: `/Users/kangs/code/github/gemini-pro-companion`
- Companion README: `day2/breakout-knowledge-synthesizer/README.md`
- Outline and placement: Day 2, Session 15
- Existing deck candidates: none identified
- Diagram candidates: Day 2 synthesis assets
- Unresolved findings: blocker, live Notebook artifacts/citations
