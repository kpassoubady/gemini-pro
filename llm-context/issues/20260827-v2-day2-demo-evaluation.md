# Demo Evaluation: Day 2 — Gemini Pro Full Instructor Demo Set

## Final Result
- Calculated score: 67/100 (local evidence layer improved executable correctness and observability).
- Applied cap: 59/100 — live Gemini/Workspace execution and product-generated artifacts remain unavailable; local checks explicitly do not claim product execution.
- Final score: 59/100.
- Rating: Ineffective: does not provide trustworthy live-product evidence.
- Evidence confidence: medium for offline contract and source mapping; low for live product behavior.
- Delivery recommendation: revise evidence capture before delivery.
- Strongest aspect: every demo now has a runnable, deterministic local check and an explicit live evidence boundary.
- Greatest classroom risk: treating `product_execution=NOT_CLAIMED` output as generated Gemini evidence.
- First correction: run the named live surface and capture actual UI/output under the documented evidence path.

## Evidence Reviewed
| Artifact | Path | Role | Verification status |
|---|---|---|---|
| Demos | `day2/demos/01-*.md` through `10-*.md` | Instructor procedures and bounded fallbacks | Read; repaired |
| Local verifier | `day2/demos/verify_offline_evidence.py` | Deterministic offline signal check | Executed for all ten cases; pass |
| Demo index | `day2/demos/README.md` | Evidence boundary and live capture contract | Read; repaired |
| Prior report | `llm-context/issues/20260827-v1-day2-demo-evaluation.md` | Comparison baseline | Read |
| Evaluator/creator standards | `course-demo-evaluator/SKILL.md`, `course-demo-creator/SKILL.md` | Rubric and repair rules | Read |

## Catalog to Demo Traceability
All ten prior mappings remain intact. Each offline fallback now maps to a named local check; target-product generation, editing, Notebook state, media, and Interactive state remain live-only and unverified.

## Technology Execution Map
| Input | Target technology | Operation | Actual evidence | Showcase test |
|---|---|---|---|---|
| Authored fixture signals | Local Python verifier | Deterministic case signal check | PASS output with explicit non-claim | Does not prove Gemini; correctly labeled |
| Story/source/policy prompts | Gemini Apps, Slides, Notebook, Vids, Audio Overview | Live UI operations | No live capture supplied | Unverified; contract documented |

## Scorecard
| Dimension | Rating | Weight | Points | Evidence summary |
|---|---:|---:|---:|---|
| Catalog and slide alignment | 4 | 15 | 12 | Existing mappings and commands preserved |
| Technology fidelity | 1.5 | 20 | 6 | Live target operations not run |
| Authentic problem and mechanism | 4 | 15 | 12 | Realistic bounded scenarios preserved |
| Executable correctness and reliability | 4 | 20 | 16 | Ten local cases run successfully |
| Instructional observability | 3.5 | 10 | 7 | Signals and boundary are explicit |
| Slide, timing, and instructor readiness | 3 | 10 | 6 | Delivery contract improved; live capture still missing |
| Portfolio progression and engagement handoff | 4 | 10 | 8 | Existing sequence preserved |
| **Total** |  | **100** | **67** |  |

## Technical Verification
| Command or check | Expected | Actual | Result |
|---|---|---|---|
| `python3 day2/demos/verify_offline_evidence.py --case <each of 10 cases>` | Labeled deterministic PASS | All ten printed `status=PASS; ... product_execution=NOT_CLAIMED` | PASS |
| Live product run | Captured product output/state | Not available in this environment | UNVERIFIED |

## Classroom Run of Show
| Phase | Estimated time | Instructor action | Learner observation or response |
|---|---:|---|---|
| Local fallback | 1–3 min | Run case and show labeled signals | Distinguish fixture evidence from product evidence |
| Live contract | section allocation | Run named surface if available and capture evidence | Inspect actual state/output and citations |
| Debrief | 2–5 min | Explain boundary and review gate | State what is proven and what remains unverified |

## Critical Conditions and Caps
The no-observable-live-evidence cap remains triggered. The prior hardcoded-showcase concern is reduced for offline claims because the verifier genuinely executes, but the verifier is not the target Gemini mechanism.

## Findings
### Blockers
1. Live target execution evidence is still absent for demos 01–10. Impact: product behavior cannot be claimed. Smallest correction: capture actual output/state under `evidence/<YYYYMMDD>-<demo-slug>/`.
### Major
1. Offline checks validate authored teaching signals, not image/video/slide/Notebook/audio generation. Keep the explicit labels and report live runs as unverified when unavailable.
2. Matching deck demo slides should be synchronized with the new local commands and live evidence path in a separate approved slide pass.
### Moderate
1. Live account, feature rollout, and permission prerequisites remain instructor-run checks.
### Minor
1. Add dated captured artifacts after a real live run.

## What Works
- No fabricated live outputs were added.
- All ten demos have deterministic local commands and clear evidence boundaries.
- Existing titles, scenarios, and sequence were preserved.

## Prioritized Improvement Plan
1. Capture real live evidence for each named product surface; do not replace local labels.
2. Synchronize matching demo slides with exact commands and signals.

## Re-evaluation Checklist
Run all ten local cases; then, where available, capture product output/state, source/citation panels, editable state, media/transcript, and review timestamps.
