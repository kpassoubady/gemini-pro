# Breakout Evaluation: Workspace Builder

## Final Result
- Calculated score: 76/100
- Applied cap: 59/100 — live Notebook import, selection, citations, and answer comparison remain unverified; local contract does not claim Notebook execution.
- Final score: 59/100
- Rating: Ineffective: does not yet provide reliable live-product evidence
- Evidence confidence: medium for bounded offline contract; low for live Notebook behavior
- Delivery recommendation: revise before delivery
- Strongest aspect: source authority and controlled boundary are explicit.
- Greatest learner risk: confusing the worked record with Notebook output.
- First correction: capture live import, selection, citations, and both answers.

## Evidence Reviewed
| Artifact | Path | Role | Verification status |
|---|---|---|---|
| README | `day2/breakout-workspace-builder/README.md` | Student contract | Repaired/read |
| Records | `start/workspace-record.md`, `solution/workspace-record.md` | Learner/worked evidence | Read |
| Verifier | `day2/breakout-workspace-builder/verify_offline.py` | Offline acceptance | Executed |
| Prior report | `llm-context/issues/20260827-v1-day2-workspace-builder-breakout-evaluation.md` | Baseline | Read |

## Catalog to Exercise Traceability
| Objective or promise | Catalog evidence | Slide preparation | Learner task | Verification | Status |
|---|---|---|---|---|---|
| Import and classify four sources | Day 2 Session 13 | Notebook foundation | Source register | Local record markers; live import unverified | Partial |
| Compare selected boundary | Session 13 | Source selection | Baseline/controlled question | Local contract; live citations unverified | Partial |

## Scorecard
| Dimension | Rating | Weight | Points | Evidence summary |
|---|---:|---:|---:|---|
| Catalog alignment | 4 | 15 | 12 | Scope preserved |
| Slide grounding | 4 | 15 | 12 | Existing placement |
| Technology fidelity | 2 | 15 | 6 | Live Notebook unavailable |
| Hands-on problem | 4 | 15 | 12 | Authentic policy pack |
| Executable contract | 4 | 15 | 12 | Local verifier passes solution |
| Engagement/feedback | 4 | 10 | 8 | Compare/review workflow |
| Timing/access | 4 | 10 | 8 | 60-minute sequence |
| Developer judgment | 2 | 5 | 2 | Non-coding tool workflow |
| **Total** |  | **100** | **72** |  |

## Critical Conditions and Caps
Live Notebook behavior remains unverified; cap applied. Offline output is explicitly labeled as fictional/local.

## Technical Verification
| Command or check | Expected | Actual | Result |
|---|---|---|---|
| `python3 verify_offline.py solution/workspace-record.md` | PASS | Required markers found; structured result printed | PASS |
| `python3 verify_offline.py start/workspace-record.md` | Intended incomplete record failure | Missing markers reported | PASS (expected red) |
| Live Notebook run | Captured state/citations | Not available | UNVERIFIED |

## Learner Workflow and Time Use
| Phase | Minutes | Learner action | Cognitive mode | Output or feedback |
|---|---:|---|---|---|
| Setup/local contract | 5 | Import/inspect or run fallback | Commit | Baseline |
| Compare | 30 | Ask twice, inspect citations | Create/compare | Two records |
| Governance/share | 25 | Review authority and permissions | Revise/feedback | Decision |

## Findings
### Blockers
1. Live Notebook evidence absent; capture under `evidence/<run-id>/`.
### Major
1. Local verifier cannot prove Notebook citations; preserve label and require live capture when claiming product behavior.
### Moderate
None.
### Minor
None.

## What Works
Bounded four-source fixture, controlled question, and explicit local/live boundary.

## Prioritized Improvement Plan
1. Capture live Notebook state and citation passages.

## Re-evaluation Checklist
Run local verifier in start/solution; verify parity; capture live evidence if available.

## Breakout Slide Handoff
- Status: blocked pending exercise repair
- Evaluation report: `llm-context/issues/20260827-v2-day2-workspace-builder-breakout-evaluation.md`
- Primary repository: `/Users/kangs/code/github/gemini-pro`
- Companion repository: `/Users/kangs/code/github/gemini-pro-companion`
- Companion README: `day2/breakout-workspace-builder/README.md`
- Outline and placement: Day 2, Session 13
- Existing deck candidates: none identified
- Diagram candidates: existing Day 2 concept assets
- Unresolved findings: blocker, live Notebook evidence, README/setup contract
