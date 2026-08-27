# Breakout Evaluation: The Data Miner

## Final Result
- Calculated score: 75.5/100
- Applied cap: 59/100 — no deterministic extraction fixture/test; PDF upload and Gemini extraction are live operations.
- Final score: 59/100
- Rating: Ineffective: does not yet provide a reliable learning experience
- Evidence confidence: high
- Delivery recommendation: redesign
- Strongest aspect: the prompt and review workflow correctly prioritize exact claims, page references, denominators, and uncertainty.
- Greatest learner risk: “every statistical claim” cannot be judged for recall without a known report and expected claim inventory.
- First correction: provide a bounded non-sensitive PDF fixture with an instructor claim inventory and page-check answer key.

## Evidence Reviewed
| Artifact | Path | Role | Verification status |
|---|---|---|---|
| Catalog | `/Users/kangs/code/github/gemini-pro/catalog/gemini-pro-sequential-outline.md:72-76,127` | objective/deliverable | inspected |
| Slides | `/Users/kangs/code/github/gemini-pro/day1/slides/03-agentic-workflows-deep-synthesis.md:137-178` | prerequisite/demo/lab | inspected |
| Demos | `/Users/kangs/code/github/gemini-pro/day1/demos/05-pdf-statistical-extraction.md`, `06-pdf-export-review.md` | extraction/review | files inspected; live upload/export unavailable |
| Companion exercise | `/Users/kangs/code/github/gemini-pro-companion/day1/breakout-data-miner/` | README/start/solution/verification | inspected |
| Concept | `/Users/kangs/code/github/gemini-pro-companion/day1/concepts/03-agentic-workflows-deep-synthesis.md` | prerequisite reference | file exists; reviewed as source map |

## Catalog to Exercise Traceability
| Objective or promise | Catalog evidence | Slide preparation | Learner task | Verification | Status |
|---|---|---|---|---|---|
| Extract statistical claims from dense report without summarizing | outline:74-76 | slides:137-143,170-178; demo 05 | README:26-31; start:5-7 | source-page sampling | full |
| Preserve page, context, denominator, methodology question | outline:74; deliverable:127 | slides:130-133,147-166 | README:28-32; solution:5-15 | five checks and review flags | full/weak evidence |
| Export reviewed findings to Sheets | outline:76,127 | slides:147-166 | README:32; solution:16 | export is live, no file/test | partial |

## Scorecard
| Dimension | Rating | Weight | Points | Evidence summary |
|---|---:|---:|---:|---|
| Catalog alignment and completeness | 4.5 | 15 | 13.5 | Direct match to extraction and cited Sheet deliverable. |
| Slide grounding and learning progression | 4.5 | 15 | 13.5 | Extraction-before-export and candidate-vs-verified distinction taught. |
| Technology fidelity and relevance | 4 | 15 | 12 | PDF upload, Gemini, and Sheets are central; all are account/live dependent. |
| Authentic hands-on problem solving | 4 | 15 | 12 | Dense-report briefing is authentic and reviewable. |
| Executable contract and technical correctness | 1.5 | 15 | 4.5 | No PDF fixture, expected inventory, spreadsheet artifact, or automated check. |
| Engagement, collaboration, and feedback | 4.5 | 10 | 9 | prediction, five-row source sample, corrections, verifier, share-out. |
| Scaffolding, timing, and participation access | 3.5 | 10 | 7 | clear phases, but “every claim” and export can exceed 60 minutes. |
| Developer workflow and technical judgment | 3.5 | 5 | 3.5 | uncertainty and no-guessing rules are strong; exact repair loop is underspecified. |
| **Total** |  | **100** | **75.5** | Rounded presentation score: 76/100. |

## Critical Conditions and Caps
No deterministic verification exists for extraction completeness, page correctness, or export fidelity. The repo is Markdown-only and has no report fixture/tests. Apply the 59 cap. Source inspection cannot substitute for execution.

## Technical Verification
| Command or check | Expected | Actual | Result |
|---|---|---|---|
| `find .../day1 -maxdepth 4 -type f` | four exercise artifacts | present | pass |
| `git diff --check` | clean | no output | pass |
| Run start/solution/tests | runnable extraction and focused test | prompt/example only; no tests/runtime/PDF | unverified/not applicable |
| Upload PDF, sample five rows, Export to Sheets | live generated table/export | requires Gemini/PDF/Sheets account | unverified |

## Learner Workflow and Time Use
| Phase | Minutes | Learner action | Cognitive mode | Output/feedback |
|---|---:|---|---|---|
| Predict/setup | 10 | predict claims; assign roles; open report | constructive | hypotheses |
| Extract | 15 | run prompt | active | candidate rows |
| Source review | 15 | check five pages and repair flags | interactive | corrected table |
| Export/check | 10 | export and inspect headers/units/duplicates | constructive | cited Sheet |
| Share-out | 10 | show pass, flag, limitation | interactive | feedback |

## Findings
### Blockers
None for a prepared live lab; the technical evidence gap blocks slide handoff, not learner activity.

### Major
1. **Extraction completeness and export are not deterministically assessable.** Affected `README.md:26-46`, `solution/verification.md:3-10`. No supplied PDF, expected claim inventory, page-answer key, or exported Sheet means “every claim” and preserved references cannot be verified. Add a bounded synthetic PDF, instructor inventory, and a CSV/Sheet acceptance checklist.

### Moderate
1. **“Every statistical claim” is unbounded for a 60-minute lab.** `README.md:5,28-32`. Define a report length/claim count or make completeness stretch-only.
2. **Repair evidence is too open-ended.** `README.md:29-31`; require one exact before/after row and reason for correction.

### Minor
1. `solution/extraction-review.md:7-9` has only three example rows while the basic completion level requires five checked claims; mark it clearly as a shape example.

## What Works
Excellent no-summary prompt, exact-number rule, unresolved flags, methodology-question boundary, source sampling, export review, and strong share-out.

## Prioritized Improvement Plan
1. Add a bounded fixture and expected claim/page inventory plus export acceptance checks.
2. Bound report size and require a before/after correction record.
3. Clarify that the three-row solution is illustrative.

## Re-evaluation Checklist
- Upload the supplied PDF and compare extracted inventory against expected claims.
- Verify five exact page/number/context checks, including an ambiguous case.
- Confirm flags survive export and duplicates/units are visible.
- Confirm the task fits 60 minutes.

## Breakout Slide Handoff
- Status: blocked pending exercise repair
- Evaluation report: `/Users/kangs/code/github/gemini-pro/llm-context/issues/20260826-v1-day1-data-miner-breakout-evaluation.md`
- Primary repository: `/Users/kangs/code/github/gemini-pro`
- Companion repository: `/Users/kangs/code/github/gemini-pro-companion`
- Companion README: `/Users/kangs/code/github/gemini-pro-companion/day1/breakout-data-miner/README.md`
- Outline and placement: `/Users/kangs/code/github/gemini-pro/catalog/gemini-pro-sequential-outline.md`, Day 1 Session 3 / Lab 1.3
- Existing deck candidates: `/Users/kangs/code/github/gemini-pro/day1/slides/03-agentic-workflows-deep-synthesis.md`
- Diagram candidates: none found
- Unresolved findings: Major — missing bounded PDF/claim inventory/export acceptance; Moderate — unbounded scope and repair evidence
