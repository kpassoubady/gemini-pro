# Breakout Evaluation: The Workspace Builder

## Final Result
- Calculated score: **79/100**
- Applied cap: **59/100 — no deterministic verification of Notebook import, source selection, citations, or controlled answer**; all core operations require a live account.
- Final score: **59/100**
- Rating: **Ineffective: does not yet provide a reliable learning experience**
- Evidence confidence: **medium** for mapping and scaffold; **low** for live Notebook behavior
- Delivery recommendation: **redesign evidence layer before slide handoff**
- Strongest aspect: four-source authority/freshness model and controlled two-source query.
- Greatest learner risk: import success and citation fidelity can be assumed from a completed worksheet.
- First correction: add an instructor-controlled fixture and captured import/citation acceptance record.

## Evidence Reviewed
| Artifact | Path | Role | Verification status |
|:---|:---|:---|:---|
| Outline | `/Users/kangs/code/github/gemini-pro/catalog/gemini-pro-sequential-outline.md:167-172,203,234` | objective/tool/deliverable | inspected |
| Teaching deck | `/Users/kangs/code/github/gemini-pro/day2/slides/03-gemini-notebook-foundation-data-sourcing.md:229-405` | preparation and handoff | inspected; no separate breakout deck |
| README | `/Users/kangs/code/github/gemini-pro-companion/day2/breakout-workspace-builder/README.md:1-53` | learner workflow | inspected |
| Start/solution/source pack | `.../breakout-workspace-builder/{start,solution}/` | source register and worked record | inspected; four fictional files present |

## Catalog to Exercise Traceability
| Objective or promise | Catalog evidence | Slide preparation | Learner task | Verification | Status |
|:---|:---|:---|:---|:---|:---|
| Create populated Notebook with diverse sources | outline `:167-172,234` | deck 03 imports/sync | README `:24-35` | source register; no Notebook | partial |
| Select sources and ground answer | outline `:169-172` | deck 03 grounding boundary | README `:30-39` | expected worked answer; no citations | partial |
| Verify permissions and sharing | outline `:169-172` | deck 03 governance | README `:35-49` | governance fields; no live setting | partial |

## Scorecard
| Dimension | Rating | Weight | Points | Evidence summary |
|:---|---:|---:|---:|:---|
| Catalog alignment and completeness | 4.5 | 15 | 13.5 | Exact Notebook/source-ingestion outcome. |
| Slide grounding and learning progression | 4.5 | 15 | 13.5 | Imports, source quality, and boundaries precede lab. |
| Technology fidelity and relevance | 4.5 | 15 | 13.5 | Notebook is the central tool, but unexecuted. |
| Authentic hands-on problem solving | 4 | 15 | 12 | Coherent policy-governance scenario. |
| Executable contract and technical correctness | 2 | 15 | 6 | Markdown records and source pack, no live acceptance test. |
| Engagement, collaboration, and feedback | 4.5 | 10 | 9 | Ranking, roles, comparison, and share-out. |
| Scaffolding, timing, and participation access | 4 | 10 | 8 | Clear timeboxes and fictional sources. |
| Developer workflow and technical judgment | 3.5 | 5 | 3.5 | Authority/freshness and citation judgment are explicit. |
| **Total** |  | **100** | **78** |  |

## Critical Conditions and Caps
- Triggered cap 59: no deterministic core Notebook verification.
- Not triggered: worksheet-only cap; the intended task requires creating and querying a Notebook.
- Not triggered: broken source tree; all four fictional source files and records are present.

## Technical Verification
| Command or check | Expected | Actual | Result |
|:---|:---|:---|:---|
| Inventory source pack and records | four sources plus starter/solution | Present | pass |
| `git diff --check` in primary | clean | clean | pass |
| Import/query/deselect task | citations and changed answer | Requires authenticated Gemini Notebook; no captured notebook | unverified |
| Compare start/solution structure | register and governance parity | Present | pass for structure |

## Learner Workflow and Time Use
| Phase | Minutes | Learner action | Cognitive mode | Output or feedback |
|:---|---:|:---|:---|:---|
| Brief/roles | 10 | rank authority and assign roles | individual/constructive | authority hypothesis |
| Build/register | 22 | create Notebook, import, inspect | constructive | source register |
| Queries | 18 | baseline then controlled query | interactive/revision | cited answers |
| Governance/share | 10 | permissions and changed claim | feedback | evidence handoff |

## Findings
### Blockers
1. **No live Notebook, import state, citations, or before/after answers are supplied.** `README.md:24-39`; this blocks verification of the promised core behavior. Correction: capture a non-sensitive fixture run or tested live evidence record.
### Major
1. **Import fidelity and source-selection claims are not deterministic.** `start/workspace-record.md:3-41`; no acceptance key checks every imported passage. Add an import checklist with expected source markers and three required citation passages.
2. **Account/synchronization/permission availability is not tested.** `README.md:24-26`; add setup matrix and timeboxed fallback.
### Moderate
1. The basic completion level asks for one citation while the definition of done requires all three facts (`README.md:41-49`); make the distinction explicit in evidence records.
2. The solution says the baseline response “may” repeat an incorrect date, which is useful as a risk but not a reproducible expected result (`solution/workspace-record.md:12-23`).
### Minor
1. Add a stable notebook export or screenshot naming convention.

## What Works
The scenario, source pack, authority classification, controlled boundary, governance check, and share-out all support careful evidence reasoning.

## Prioritized Improvement Plan
1. Add deterministic import/citation fixture and capture.
2. Test Notebook synchronization and permissions with a fallback.
3. Align basic/intermediate evidence requirements.

## Re-evaluation Checklist
Import all four sources, inspect expected passages, record baseline and controlled answers with citations, verify all three facts, and record sharing/export permissions.

## Breakout Slide Handoff
- Status: **blocked pending exercise repair**
- Evaluation report: `/Users/kangs/code/github/gemini-pro/llm-context/issues/20260827-v1-day2-workspace-builder-breakout-evaluation.md`
- Primary repository: `/Users/kangs/code/github/gemini-pro`
- Companion repository: `/Users/kangs/code/github/gemini-pro-companion`
- Companion README: `/Users/kangs/code/github/gemini-pro-companion/day2/breakout-workspace-builder/README.md`
- Outline and placement: `catalog/gemini-pro-sequential-outline.md`, Day 2 Session 13 / Lab 2.3
- Existing deck candidates: none
- Diagram candidates: `/Users/kangs/code/github/gemini-pro/day2/diagrams/notebook-grounding-surfaces.{mmd,svg,png}`, `notebook-source-ingestion.{mmd,svg,png}`
- Unresolved findings: Blocker `README.md:24-39` no Notebook evidence; Major `start/workspace-record.md:3-41` no deterministic import/citation acceptance.
