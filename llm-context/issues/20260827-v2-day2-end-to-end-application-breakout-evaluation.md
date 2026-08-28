# Breakout Evaluation: End-to-End Application

## Final Result
- Calculated score: 74/100
- Applied cap: 59/100 — live end-to-end Notebook and multimedia execution remain unverified; fixed pilot fallback is now bounded and deterministic at the record-contract level.
- Final score: 59/100
- Rating: Ineffective: live end-to-end evidence is not verified
- Evidence confidence: medium for fixed pilot scope and local contract; low for live workflow
- Delivery recommendation: revise before delivery
- Strongest aspect: fixed pilot path, governance, correction, and maintenance contract.
- Greatest learner risk: attempting own-topic or all outputs within 60 minutes.
- First correction: use fixed pilot pack for basic path and capture actual live outputs.

## Evidence Reviewed
| Artifact | Path | Role | Verification status |
|---|---|---|---|
| README | `day2/breakout-end-to-end-application/README.md` | Student contract | Repaired/read |
| Source pack/record | `start/`, `solution/` | Fixed acceptance path | Read |
| Verifier | `day2/breakout-end-to-end-application/verify_offline.py` | Local acceptance | Executed |
| Prior report | `llm-context/issues/20260827-v1-day2-end-to-end-application-breakout-evaluation.md` | Baseline | Read |

## Catalog to Exercise Traceability
| Objective or promise | Catalog evidence | Slide preparation | Learner task | Verification | Status |
|---|---|---|---|---|---|
| Fresh source-grounded workflow | Day 2 Session 17 | Capstone workflow | Fixed pilot import and claim check | Local record contract; live Notebook absent | Partial |
| One reviewed artifact and governance | Session 17 | Integration | Produce artifact, permissions, maintenance | Local markers; live artifact absent | Partial |

## Scorecard
| Dimension | Rating | Weight | Points | Evidence summary |
|---|---:|---:|---:|---|
| Catalog alignment | 3.5 | 15 | 10.5 | Scope tightened |
| Slide grounding | 4 | 15 | 12 | Existing |
| Technology fidelity | 2 | 15 | 6 | Live Notebook/media unavailable |
| Hands-on problem | 4 | 15 | 12 | Fixed pilot is coherent |
| Executable contract | 4 | 15 | 12 | Local verifier pass |
| Engagement/feedback | 4 | 10 | 8 | Peer review/correction |
| Timing/access | 3.5 | 10 | 7 | Fixed basic path; stretch remains optional |
| Developer judgment | 3 | 5 | 3 | Governance and correction |
| **Total** |  | **100** | **70.5** |  |

## Critical Conditions and Caps
Live end-to-end product evidence cap applies. The prior open-topic timing major is reduced by the fixed pilot basic path.

## Technical Verification
| Command or check | Expected | Actual | Result |
|---|---|---|---|
| `python3 verify_offline.py solution/capstone-record.md` | PASS | Fixed pilot, citation, artifact, maintenance markers found | PASS |
| `python3 verify_offline.py start/capstone-record.md` | Expected incomplete failure | Missing markers reported | PASS (expected red) |
| Live Notebook/media run | Captured outputs and permissions | Not available | UNVERIFIED |

## Learner Workflow and Time Use
| Phase | Minutes | Learner action | Cognitive mode | Output or feedback |
|---|---:|---|---|---|
| Fixed setup | 15 | Import pilot pack and classify | Commit/create | Source register |
| Evidence/artifact | 32 | Verify claim, notes, guide, one artifact | Create/revise | Evidence bundle |
| Governance/share | 13 | Peer review and maintenance | Feedback | Handoff decision |

## Findings
### Blockers
1. Live end-to-end Notebook/media evidence absent; capture under `evidence/<run-id>/`.
### Major
1. Local verifier validates the fixed record contract, not product generation or permissions.
### Moderate
1. Own-topic work remains stretch only; do not let it displace the fixed basic path.
### Minor
None.

## What Works
Fixed pilot source pack, timeboxed minimum path, and explicit judgment/governance requirements.

## Prioritized Improvement Plan
1. Capture live evidence for each required output and permission boundary.

## Re-evaluation Checklist
Run local verifier on start/solution; verify fixed-path timing; inspect live Notebook/media evidence when available.

## Breakout Slide Handoff
- Status: blocked pending exercise repair
- Evaluation report: `llm-context/issues/20260827-v2-day2-end-to-end-application-breakout-evaluation.md`
- Primary repository: `/Users/kangs/code/github/gemini-pro`
- Companion repository: `/Users/kangs/code/github/gemini-pro-companion`
- Companion README: `day2/breakout-end-to-end-application/README.md`
- Outline and placement: Day 2, Session 17
- Existing deck candidates: none identified
- Diagram candidates: Day 2 capstone assets
- Unresolved findings: blocker, live end-to-end product evidence
