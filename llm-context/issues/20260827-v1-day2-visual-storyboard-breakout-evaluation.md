# Breakout Evaluation: The Visual Storyboard

## Final Result
- Calculated score: **79/100**
- Applied cap: **59/100 — no deterministic verification exists for generated frames and continuity behavior**; images are live Gemini operations and no captured frames are supplied.
- Final score: **59/100**
- Rating: **Ineffective: does not yet provide a reliable learning experience**
- Evidence confidence: **medium** for source mapping and exercise design; **low** for live image generation and visual verification
- Delivery recommendation: **redesign evidence layer before slide handoff**
- Strongest aspect: fixed campaign facts, continuity ledger, bounded repair, and rights/accessibility checkpoint.
- Greatest learner risk: learners can complete the ledger from fictional fallback prose without practicing image generation or seeing real drift.
- First correction: provide a bounded, non-sensitive image fixture/evidence capture and a repeatable visual acceptance record.

## Evidence Reviewed
| Artifact | Path | Role | Verification status |
|:---|:---|:---|:---|
| Outline | `/Users/kangs/code/github/gemini-pro/catalog/gemini-pro-sequential-outline.md:145-151,203,232` | objective, tool, timing, deliverable | inspected |
| Teaching deck | `/Users/kangs/code/github/gemini-pro/day2/slides/01-enterprise-multimedia-workflows.md:459-810` | preparation and Lab 2.1 handoff | inspected; no separate breakout deck |
| README | `/Users/kangs/code/github/gemini-pro-companion/day2/breakout-visual-storyboard/README.md:1-53` | authoritative learner workflow | inspected |
| Starter/solution | `.../start/storyboard-brief.md`, `.../start/continuity-ledger.md`, `.../solution/storyboard-brief.md`, `.../solution/continuity-ledger.md` | scaffold and worked evidence shape | inspected |
| Evaluator standard | `/Users/kangs/code/github/claude-personal-helper/skills/course-breakout-exercise-evaluator/SKILL.md:35-222` | rubric and handoff gate | inspected |

## Catalog to Exercise Traceability
| Objective or promise | Catalog evidence | Slide preparation | Learner task | Verification | Status |
|:---|:---|:---|:---|:---|:---|
| Generate anchor and second frame with continuity ledger | outline `:147-151` | deck 01 demo/section | README `:28-35` | ledger and worked example only; no generated frames | partial |
| Evaluate drift and bounded repair | outline `:151,232` | deck 01 review gate | README `:33-39` | fictional Output A/B plus solution ledger | partial |
| Govern rights, accessibility, disclosure | outline `:149-150` | deck 01 governance content | README `:37-39,47-53` | checklist, no actual asset review | partial |

## Scorecard
| Dimension | Rating | Weight | Points | Evidence summary |
|:---|---:|---:|---:|:---|
| Catalog alignment and completeness | 4.5 | 15 | 13.5 | Direct match to storyboard deliverable and 60-minute lab. |
| Slide grounding and learning progression | 4.5 | 15 | 13.5 | Image continuity and review are taught before the lab. |
| Technology fidelity and relevance | 4 | 15 | 12 | Gemini image generation is central, but live evidence is absent. |
| Authentic hands-on problem solving | 4.5 | 15 | 13.5 | Coherent fictional safety campaign with realistic governance. |
| Executable contract and technical correctness | 2 | 15 | 6 | Markdown scaffold and ledger; no image fixture/test. |
| Engagement, collaboration, and feedback | 4.5 | 10 | 9 | Roles, prediction, review, repair, and share-out are purposeful. |
| Scaffolding, timing, and participation access | 4 | 10 | 8 | Clear phases and fallback, but generation latency is uncontrolled. |
| Developer workflow and technical judgment | 3.5 | 5 | 3.5 | Bounded repair and evidence rules are strong. |
| **Total** |  | **100** | **76** |  |

## Critical Conditions and Caps
- Triggered cap 59: no deterministic verification of frame generation, drift, or repair; no actual image files are included.
- Not triggered: worksheet-only cap; the intended learner task does require image generation.
- Not triggered: unrelated starter/solution failure; artifacts are readable and structurally paired.

## Technical Verification
| Command or check | Expected | Actual | Result |
|:---|:---|:---|:---|
| Inventory breakout tree | README, start, solution present | Present | pass |
| `git diff --check` in primary | clean | clean | pass |
| Run image-generation task | two frames and visible continuity evidence | Requires authenticated Gemini Apps; no fixture/output | unverified |
| Compare starter and solution paths | required ledger parity | Present; solution is worked Markdown | pass for structure |
| Render/inspect image acceptance | visible rows independently checked | No image artifacts supplied | blocked/unverified |

## Learner Workflow and Time Use
| Phase | Minutes | Learner action | Cognitive mode | Output or feedback |
|:---|---:|:---|:---|:---|
| Brief/roles | 10 | predict drift and assign roles | individual/constructive | risk hypothesis |
| Story bible/anchor | 20 | complete contract and generate/select anchor | constructive | anchor image |
| Frame 2/review | 22 | generate, compare, repair | interactive/revision | ledger |
| Governance/share | 8 | rights/accessibility/disclosure and share-out | feedback | decision |

## Findings
### Blockers
1. **No observable generated-frame evidence.** `README.md:24-35`; starter has no images and solution contains only a worked ledger. Impact: core image-generation and continuity objective cannot be verified. Smallest correction: add approved non-sensitive reference/output evidence or a documented live capture procedure with pass/fail rows.
### Major
1. **No deterministic acceptance fixture for visual drift.** `start/continuity-ledger.md:3-18`; graders cannot distinguish a generated drift from an authored answer. Add a bounded fixture set and review protocol.
2. **Generation availability/latency fallback is discussion-only.** `README.md:24-26`; time risk in a 60-minute lab. Add tested account prerequisites and a timeboxed fallback that is explicitly non-product evidence.
### Moderate
1. The README says two frames while the instructor demo extends to four; keep the breakout scope distinct (`day2/demos/01:31-40`).
2. Accessibility review requires reviewed alt text but no template (`README.md:37-39`).
### Minor
1. Name the expected image file/capture convention for re-evaluation.

## What Works
The fixed brief is specific, the ledger exposes identity/prop/style/geography drift, repair is bounded, and the share-out asks for evidence rather than aesthetic preference.

## Prioritized Improvement Plan
1. Add bounded frame evidence and repeatable visual acceptance checks.
2. Add tested setup, latency, and fallback instructions.
3. Add alt-text/disclosure capture fields.

## Re-evaluation Checklist
Run image generation, preserve anchor and Frame 2 outputs, complete every ledger row from visible evidence, verify repair preserves passing rows, and record rights/accessibility results.

## Breakout Slide Handoff
- Status: **blocked pending exercise repair**
- Evaluation report: `/Users/kangs/code/github/gemini-pro/llm-context/issues/20260827-v1-day2-visual-storyboard-breakout-evaluation.md`
- Primary repository: `/Users/kangs/code/github/gemini-pro`
- Companion repository: `/Users/kangs/code/github/gemini-pro-companion`
- Companion README: `/Users/kangs/code/github/gemini-pro-companion/day2/breakout-visual-storyboard/README.md`
- Outline and placement: `catalog/gemini-pro-sequential-outline.md`, Day 2 Session 10 / Lab 2.1
- Existing deck candidates: none
- Diagram candidates: `/Users/kangs/code/github/gemini-pro/day2/diagrams/story-continuity-loop.{mmd,svg,png}`
- Unresolved findings: Blocker `README.md:24-35` no generated-frame evidence; Major `start/continuity-ledger.md:3-18` no deterministic visual acceptance.
