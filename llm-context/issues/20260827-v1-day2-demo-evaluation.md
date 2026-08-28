# Demo Evaluation: Day 2 — Gemini Pro Full Instructor Demo Set

## Final Result

- Calculated score: **48.0/100** (mean of the ten per-demo weighted scores).
- Applied cap: **59/100 — no observable evidence proves the claimed behavior.** The demos are Markdown prompt and delivery notes; no live Gemini/Workspace output, generated media, editable slide state, notebook state, or captured artifact is included.
- Final score: **48.0/100**.
- Rating: **Ineffective: does not provide trustworthy evidence of the concepts**.
- Evidence confidence: **medium** for catalog/source mapping and content alignment; **low** for execution and product-behavior claims.
- Delivery recommendation: **redesign the demo evidence layer before delivery**.
- Strongest evidence: all ten prompts map directly to the Day 2 sessions, include useful verification boundaries, and appear after the relevant concept preparation in `day2/slides/`.
- Greatest classroom risk: offline fallback prose can make a product behavior appear demonstrated when no Gemini Apps, Google Slides, Gemini Notebook, Google Vids, or Audio Overview operation is observable.
- First correction: add non-sensitive fixtures, an explicit live run procedure, expected observable signals, and captured verification evidence for each demo; do not fabricate outputs.

### Per-demo result summary

| Demo | Role | Calculated | Cap | Final | Result | Confidence |
|:---|:---|---:|---:|---:|:---|:---|
| 01 Character Continuity Under Pressure | Failure and repair / practical multimodal | 51.5 | 59 | 51.5 | Ineffective | Low |
| 02 Storyboard-to-Video Handoff | Integration / failure and repair | 44.5 | 59 | 44.5 | Ineffective | Low |
| 03 Source-Grounded Presentation Plan | Practical workflow | 52.5 | 59 | 52.5 | Ineffective | Low |
| 04 Repair One Slide Without Losing Control | Failure and repair | 48.5 | 59 | 48.5 | Ineffective | Low |
| 05 Control the Notebook Source Boundary | Comparison / practical workflow | 48.5 | 59 | 48.5 | Ineffective | Low |
| 06 Compare Grounding Across Gemini Surfaces | Comparison / integration | 46.5 | 59 | 46.5 | Ineffective | Low |
| 07 Contradiction-First Synthesis | Practical synthesis | 46.5 | 59 | 46.5 | Ineffective | Low |
| 08 Verified Notes to Study Aids | Integration / failure and repair | 47.5 | 59 | 47.5 | Ineffective | Low |
| 09 Choose and Review a Multimedia Artifact | Comparison / review | 46.5 | 59 | 46.5 | Ineffective | Low |
| 10 Interrogate an Audio Overview | Practical multimodal / integration | 47.5 | 59 | 47.5 | Ineffective | Low |

## Evidence Reviewed

| Artifact | Path | Role | Verification status |
|:---|:---|:---|:---|
| Authoritative outline | `/Users/kangs/code/github/gemini-pro/catalog/gemini-pro-sequential-outline.md:145-222` | Day 2 objectives, tools, sequence, timing, labs, deliverables | Read; authoritative |
| Day 2 teaching decks | `/Users/kangs/code/github/gemini-pro/day2/slides/01-enterprise-multimedia-workflows.md` through `06-gemini-notebook-capstone-workflow-integration.md` | Preparation, demo placement, breakout handoffs | Read/inventoried; current worktree has pre-existing modifications |
| Instructor demos | `/Users/kangs/code/github/gemini-pro/day2/demos/01-visual-story-continuity.md` through `10-interactive-audio-overview.md` | Target artifacts | Read; all Markdown-only prompt/delivery notes |
| Day 2 research and diagrams | `/Users/kangs/code/github/gemini-pro/llm-context/research/day2/`; `/Users/kangs/code/github/gemini-pro/day2/diagrams/` | Product and concept context | Paths inventoried; diagrams exist, not execution evidence |
| Companion breakouts | `/Users/kangs/code/github/gemini-pro-companion/day2/breakout-*` | Related learner progression and fixture references | Read as related activities |
| Demo evaluator standard | `/Users/kangs/code/github/claude-personal-helper/skills/course-demo-evaluator/SKILL.md:43-240` | Rubric, caps, confidence, report format | Read in full |

## Catalog to Demo Traceability

| Concept or promise | Catalog evidence | Slide preparation | Demo operation | Observable evidence | Status |
|:---|:---|:---|:---|:---|:---|
| Story bible, reference image, continuity ledger | Outline `:147-151` | Deck 01, demo sections | Gemini image generation with anchor and repaired frame prompts | No generated images or ledger result in repo | Partial |
| Keyframe-to-video continuity and review gate | Outline `:147-151` | Deck 01 | Google Vids animation of approved frames | No clips, timeline, or handoff state | Partial |
| Source-grounded editable presentation plan | Outline `:153-157` | Deck 02 | Slides source selection, clarifying questions, plan review | No source list, plan, or generated presentation | Partial |
| Bounded editable slide repair | Outline `:153-157` | Deck 02 | Ask Gemini repairs selected slide and returns preview | No editable slide or before/after preview | Partial |
| Notebook source selection boundary | Outline `:167-172` | Deck 03 | Select/deselect four imported sources and repeat query | No notebook, citations, or before/after answers | Partial |
| Cross-surface grounding distinction | Outline `:167-172` | Deck 03 | Compare Notebook and Gemini Apps answers | No synchronized notebook or outside-evidence result | Partial |
| Contradiction-preserving synthesis | Outline `:177-181` | Deck 04 | Build cited claim-evidence matrix | No generated matrix or opened citations | Partial |
| Verified notes to study aids | Outline `:177-181` | Deck 04 | Generate briefing, study guide, quiz and verify answer | No saved notes, guide, quiz, or source check | Partial |
| Artifact choice and visual review | Outline `:191-195` | Deck 05 | Generate/review infographic or Video Overview | No visual artifact, text equivalent, or accessibility check | Partial |
| Audio Overview and Interactive mode | Outline `:191-195` | Deck 05 | Generate Deep Dive, join, ask bounded question | No audio, transcript, interaction, or verified answer | Partial |

## Technology Execution Map

| Input | Target technology | Operation | Actual evidence | Showcase test |
|:---|:---|:---|:---|:---|
| Story bible and approved image | Gemini Apps image generation | Generate/revise related frames | Prompt text and fictional fallback only | Unverified; result could be authored without image generation |
| Approved keyframes | Google Vids AI video | Animate and assemble clips | Motion prompts and checklist only | Unverified; no clip or timeline |
| LaunchTracker/LaunchAnnouncement | Gemini in Google Slides | Inspect sources and generate plan | Brief and fallback plan lines only | Unverified; no Slides source state |
| Verified blocker rows | Gemini slide editing | Preview bounded editable repair | Prompt and acceptance list only | Unverified; no editable elements |
| Four policy source files | Gemini Notebook | Import/select/deselect and cite | Referenced companion files and fallback answers | Unverified; no notebook state or citations |
| Notebook plus Gemini Apps | Gemini Apps synchronized workspace | Compare source boundary | Expected comparison prose only | Unverified; external contribution not observed |
| Four selected policy sources | Gemini Notebook synthesis | Generate cited matrix | Prompt and rejected-row fallback only | Unverified; no generated matrix |
| Verified notes | Notebook study-aid tools | Generate guide and quiz | Acceptance rules only | Unverified; no artifacts or answer-key check |
| Policy sources | Notebook infographic/Video Overview | Generate and review media | Prepared defect description only | Unverified; no asset or accessibility output |
| Policy sources | Notebook Audio Overview Interactive mode | Generate, join, ask, verify | Deep Dive prompt and fallback excerpt only | Unverified; no audio or spoken answer |

The hardcoded-showcase test is not proven because the demos do not print a full prepared result as if it were generated. However, none executes the target technology in the repository, so no output can be attributed to the named product surface. The no-observable-evidence cap applies.

## Scorecard

Ratings are 0–5, in rubric order: alignment / technology fidelity / authentic problem / executable correctness / observability / slide-timing-readiness / portfolio progression (weights 15/20/15/20/10/10/10).

| Demo | Alignment | Technology | Authentic | Executable | Observable | Ready | Progression | Total |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| 01 | 4.5 | 2.0 | 4.0 | 1.0 | 1.5 | 2.0 | 3.5 | 51.5 |
| 02 | 4.0 | 1.5 | 3.5 | 1.0 | 1.5 | 1.5 | 3.0 | 44.5 |
| 03 | 4.5 | 2.0 | 4.0 | 1.0 | 2.0 | 2.5 | 3.5 | 52.5 |
| 04 | 4.0 | 1.5 | 3.5 | 1.0 | 1.5 | 2.0 | 3.5 | 48.5 |
| 05 | 4.0 | 1.5 | 3.5 | 1.0 | 1.5 | 2.0 | 3.5 | 48.5 |
| 06 | 4.0 | 1.5 | 3.5 | 1.0 | 1.5 | 1.5 | 3.0 | 46.5 |
| 07 | 4.0 | 1.5 | 3.5 | 1.0 | 1.5 | 1.5 | 3.0 | 46.5 |
| 08 | 4.0 | 1.5 | 3.5 | 1.0 | 1.5 | 1.5 | 3.0 | 46.5 |
| 09 | 4.0 | 1.5 | 3.5 | 1.0 | 1.5 | 1.5 | 3.0 | 46.5 |
| 10 | 4.0 | 1.5 | 3.5 | 1.0 | 1.5 | 1.5 | 3.0 | 46.5 |

The summary totals use the first table's weighted values; the row-level scorecard is intentionally conservative where live media and Workspace state are absent.

## Technical Verification

| Command or check | Expected | Actual | Result |
|:---|:---|:---|:---|
| Inventory `day2/demos/*.md` | Ten demos present | Ten files present | Pass |
| Matching `_class: demo` sections in `day2/slides/` | Each demo has a preceding teaching/demo section | All ten titles and demo sections found in six decks | Pass for path/placement |
| `git diff --check` | No whitespace errors in pre-existing worktree | Clean | Pass |
| Run each documented demo | Target Gemini/Workspace behavior and evidence | No executable command, fixture invocation, captured output, or artifact; operations require authenticated external products | Blocked/unverified |
| Dependency/setup resolution | Documented course stack resolves locally | No package/lock/runtime or local live-service harness for these demos | Unverified/not applicable |
| Live Gemini, Slides, Notebook, Vids, Audio Overview | Real operation produces inspectable state | No authenticated browser session or supplied outputs | Unverified |
| Source references and diagram paths | Referenced paths exist | Day 2 demos, decks, research, and diagrams exist by inventory | Pass for path existence only |
| Artifact immutability | No demos/slides/catalog/breakouts changed by evaluation | Evaluation pass changed none; existing slide/quizzes worktree changes predated this pass | Pass |

## Classroom Run of Show

Each demo is intended to fit a short portion of its 60-minute session, but current files omit concrete setup and recovery evidence.

| Phase | Estimated time | Instructor action | Learner observation or response |
|:---|---:|:---|:---|
| Media continuity | 10–15 min | Generate anchor, weak frame, repaired frame; compare ledger | Identity, prop, geography, style drift; currently no expected live output |
| Video handoff | 10–15 min | Animate approved frames and inspect cut | End/start pose and motion continuity; no clip fallback procedure beyond prose |
| Presentation plan/repair | 15–20 min | Select sources, review plan, preview one repair | Source provenance, editability, unsupported claims; no artifact state |
| Notebook foundation | 10–15 min | Import sources, select/deselect, repeat question | Citation and claim changes; no notebook evidence |
| Synthesis/study aids | 15–20 min | Compare sources, save checked notes, generate guide/quiz | Conflict status and answer-key grounding; no generated artifacts |
| Multimedia/audio | 15–20 min | Choose artifact, review or join audio interaction | Factual/accessibility defects and verified spoken answer; no media evidence |

## Critical Conditions and Caps

- **Triggered: no observable evidence proves claimed behavior (cap 59, dominates).** All ten are prose prompts/delivery plans without a model response, product state, generated image/video/audio, editable slide, notebook citation, or captured comparison.
- **Not triggered: hardcoded showcase cap 39.** The files include fictional fallback diagnoses, but do not present them as actual generated results.
- **Not triggered: unapproved technology.** Named surfaces are the catalog-approved Gemini/Workspace stack (`outline:12-19,32-34`). Availability is variable and unverified.
- **Not triggered: code/dependency defect.** There is no executable demo code; the defect is missing execution evidence.
- **Triggered where relevant: unstated setup/live-service risk (cap 69, dominated by 59).** Several demos depend on authenticated accounts, rollout-dependent features, source files, or earlier artifacts without a repository-run harness.

## Findings

### Blockers

1. **No target technology execution is observable for any of the ten demos.** Affected: `day2/demos/01-visual-story-continuity.md:43-59` through `10-interactive-audio-overview.md:7-33`. Evidence: each file contains prompts, fallback prose, or delivery instructions but no live output/state or executable capture. Impact: an instructor cannot prove that Gemini Apps, Google Vids, Slides, Notebook, or Audio Overview produced the result. Smallest correction: provide a supported run procedure, fixture manifest, expected signals, and captured verification record for each demo.

### Major

1. **The offline fallbacks substitute authored prose for product evidence.** Affected: demos 01–10, especially `01:43-50`, `03:27-34`, `05:25-32`, `10:31-33`. Impact: learners may learn the diagnosis but not the mechanism. Correction: label fallback as discussion-only and add a real or explicitly non-product simulation path without claiming live proof.
2. **Live feature and account prerequisites are not operationalized per demo.** Affected: `02:32-38`, `03:7-9,36-45`, `04:39-65`, `06:7-23`, `10:23-33`. Impact: account rollout, source synchronization, generation latency, and Interactive mode failures force improvisation. Correction: add tested prerequisites and recoverable fallback steps to each demo.
3. **Verification records are absent for comparison and repair claims.** Affected: `04:31-55`, `05:19-23`, `07:19-27`, `08:19-29`, `09:19-27`, `10:23-33`. Impact: dates, citations, editability, accessibility, spoken conditions, and unsupported claims cannot be independently checked. Correction: capture before/after artifacts and a pass/fail checklist tied to source passages.

### Moderate

1. `03-source-grounded-presentation.md:7-14` depends on Day 1 artifacts that are themselves demo prose rather than repository fixtures; provide prepared non-sensitive source files or clearly document the live setup.
2. `02-storyboard-video-handoff.md:34-38` requires assembling accepted clips but gives no expected timeline/export observation or failure recovery.
3. `09-multimedia-artifact-selection.md:19-27` identifies accessibility checks but supplies no text-equivalent acceptance template.
4. Several demos use “if unavailable” fallback wording without a per-feature timebox; this reduces the reliability of a 60-minute session.

### Minor

1. Keep the exact demo title and run instruction synchronized with the corresponding slide sections after a future evidence pass.
2. Add stable artifact filenames and review dates to captured evidence so later evaluation can compare versions.

## What Works

- Strong mapping to the Day 2 outline and session progression (`outline:145-203`).
- Prompts consistently preserve uncertainty, source boundaries, rights/accessibility review, editability, and evidence-vs-inference distinctions.
- The demos prepare, rather than duplicate, the six companion breakouts.
- The fictional fallbacks are useful for discussion and reveal likely failure modes when clearly labeled as non-execution.

## Prioritized Improvement Plan

1. Add tested, non-sensitive fixture and evidence manifests for all ten demos; capture live output/state and verification signals.
2. Replace “run prose” ambiguity with explicit UI/run procedures and per-feature prerequisites/fallbacks.
3. Add before/after acceptance records for repairs, source-boundary comparisons, citations, media review, and Interactive audio answers.
4. Re-run this full-day evaluation after the evidence layer is added; score technology fidelity and executable correctness only from observed results.

## Re-evaluation Checklist

- Run every documented procedure without source changes and record account/service prerequisites.
- Capture input, target operation, output/state, and evidence for each target product surface.
- Verify all dates, citations, continuity rows, editability, accessibility, and spoken exception conditions against source artifacts.
- Confirm fallback paths do not masquerade as live Gemini/Workspace evidence.
- Recheck each matching slide's command, placement, duration, and recovery steps.
