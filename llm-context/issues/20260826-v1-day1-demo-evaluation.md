# Demo Evaluation: Day 1 — Gemini Pro Full Instructor Demo Set

## Final Result

- Calculated score: **46.5/100** (mean of the twelve per-demo weighted scores; equal weighting because the catalog defines six co-equal sessions and the twelve files are paired demonstrations within those sessions)
- Applied cap: **59/100 maximum — no observable evidence proves the claimed behavior.** Every demo is a Markdown prompt/delivery note, not an executable artifact, and no live Gemini/Workspace execution, output, fixture, or generated artifact is included.
- Final score: **46.5/100**
- Rating: **Ineffective: does not provide trustworthy runnable evidence of the concepts**
- Evidence confidence: **medium** for source mapping and content alignment; **low** for execution and technology claims
- Delivery recommendation: **redesign the demo evidence layer before delivery**. The prompts are generally well aligned, but the instructor cannot run or rehearse the demos from the repository and learners cannot inspect mechanism-produced results.
- Strongest evidence: the twelve prompts consistently mirror the catalog's six workflows, include verification language, and are placed in the corresponding Day 1 slide sections (catalog lines 56–104; slides 01–06 demo sections).
- Greatest classroom risk: the slide command `Run day1/demos/<file>.md` points at prose, not an executable command (for example `day1/slides/01-connected-workspace-data-retrieval.md:200-219` and `day1/slides/06-native-workspace-in-app-automation.md:124-144`). A clean-looking response may therefore be presented without reproducible source, output, or feature-state evidence.
- First correction: provide prepared, non-sensitive fixtures plus an explicit live run procedure and captured expected observations for each demo, then execute each once on the supported Gemini/Workspace account before teaching.

### Per-demo result summary

| Demo | Role | Calculated | Cap | Final | Result | Confidence |
|:---|:---|---:|:---:|---:|:---|:---|
| 01 Connected Workspace Retrieval | Practical integration | 49.0 | 59 | 49.0 | Ineffective | Low |
| 02 Verify a Connected-App Answer | Failure and repair | 48.0 | 59 | 48.0 | Ineffective | Low |
| 03 Board of Three Experts | Conceptual | 51.0 | 59 | 51.0 | Ineffective | Medium |
| 04 Repair a Generic Recommendation | Failure and repair | 48.0 | 59 | 48.0 | Ineffective | Low |
| 05 Extract Statistical Claims from a PDF | Practical workflow | 47.0 | 59 | 47.0 | Ineffective | Low |
| 06 Review Before Export to Sheets | Failure and repair/integration | 45.0 | 59 | 45.0 | Ineffective | Low |
| 07 Timestamped Video Analysis | Practical multimodal | 44.0 | 59 | 44.0 | Ineffective | Low |
| 08 Screenshot Flow Critique | Practical multimodal | 45.0 | 59 | 45.0 | Ineffective | Low |
| 09 Create the Relentless Editor Gem | Practical product workflow | 44.0 | 59 | 44.0 | Ineffective | Low |
| 10 Selective Editing in Canvas | Practical product workflow | 43.0 | 59 | 43.0 | Ineffective | Low |
| 11 Build and Verify a Sheets Tracker | Practical integration | 45.0 | 59 | 45.0 | Ineffective | Low |
| 12 Docs Announcement Handoff | Integration | 43.0 | 59 | 43.0 | Ineffective | Low |

## Evidence Reviewed

| Artifact | Path | Role | Verification status |
|:---|:---|:---|:---|
| Course-demo-evaluator | `/Users/kangs/code/github/claude-personal-helper/skills/course-demo-evaluator/SKILL.md:6-240` | Required workflow, hardcoded-showcase test, rubric, caps, confidence, and report format | Read in full |
| Catalog and detailed outline | `catalog/gemini-pro-sequential-outline.md:1-134` | Authority for outcomes, tools, sequence, timing, labs, and deliverables | Read in full |
| Course overview | `README.md:1-127` | Project context and related companion/setup repositories | Read in full |
| Session slides | `day1/slides/01-connected-workspace-data-retrieval.md:38-249`; `02-cognitive-frameworks.md:38-197`; `03-agentic-workflows-deep-synthesis.md:38-199`; `04-multimodal-analysis.md:38-183`; `05-persistent-personas.md:38-184`; `06-native-workspace-in-app-automation.md:38-187` | Preparation, demo placement, prompts, lab handoff, guardrails | Read in full |
| Instructor demos | `day1/demos/01-connected-retrieval-prompt.md` through `12-docs-announcement-handoff.md` | Target artifacts | Read in full; all are Markdown-only instructions with no run command, fixture, output, or executable code |
| Day 1 research | `llm-context/research/day1/{connected-workspace-data-retrieval,cognitive-frameworks,agentic-workflows-deep-synthesis,multimodal-analysis,persistent-personas,native-workspace-in-app-automation}-research.md` | Current product behavior, sources, risks, industry context | Read in full |
| Project/setup evidence | Referenced `gemini-pro-companion` and `gemini-pro-setup` repositories (`README.md:124-127`; catalog `:32-34`) | Learner labs and pre-class account verification | Not present in this checkout; no local fixtures, dependency/lock files, setup instructions, or generated artifacts were available to run |
| Quizzes and diagrams | `day1/quizzes/*`; `day1/diagrams/*` | Related activities and explanatory visuals | Paths inventoried; not treated as demo execution evidence |

No course artifact was modified. A shell execution attempt was unavailable in this background evaluation context; more importantly, the demo files themselves expose no executable command to run. This report therefore records execution as **not possible/unverified**, never as a pass.

## Catalog to Demo Traceability

| Concept or promise | Catalog evidence | Slide preparation | Demo operation | Observable evidence | Status |
|:---|:---|:---|:---|:---|:---|
| Gmail + Drive retrieval and evidence/inference status report | Outline `:56-60`, deliverable `:125` | Slide 01 `:112-194` | Prompt 01 requests `@Gmail` and `@Google Drive`; Prompt 02 requests recency repair | None: no live response, source citation, prepared email, or Drive document | Partial; operation specified, evidence missing |
| Verification and prompt refinement | Outline `:58-60` | Slide 01 `:188-219` | Demo 02 asks to inspect old/new threads and refine query | None: no old/new fixture or before/after output | Partial |
| Three cognitive lenses and inspectable consensus | Outline `:62-66`, deliverable `:126` | Slide 02 `:57-132` | Demo 03 requests three roles, debate, consensus table, verification flags | None: generated output is not included or observed | Partial |
| Repair generic persona output with concrete criteria | Outline `:64-66` | Slide 02 `:146-188` | Demo 04 applies rollout/export/audit/training criteria | None: no generic baseline or revised comparison | Partial |
| Agentic PDF extraction with claim/page/context/methodology fields | Outline `:72-76`, deliverable `:127` | Slide 03 `:57-133` | Demo 05 asks Gemini to extract every claim; Demo 06 reviews rows | None: no PDF, extracted table, flags, or Sheets export | Partial |
| Review before Sheets handoff | Outline `:74-76` | Slide 03 `:147-179` | Demo 06 asks for PASS/CHECK/UNRESOLVED review | None: no candidate table or export artifact | Partial |
| Video timestamps, counterpoints, and replay verification | Outline `:82-86`, deliverable `:128` | Slide 04 `:57-92`, `:124-166` | Demo 07 asks for three timestamped points and detractor responses | None: no video URL, transcript, timestamps, or replay result | Partial |
| Screenshot observation versus friction hypothesis | Outline `:84-86` | Slide 04 `:83-92`, `:124-183` | Demo 08 asks for visible controls, flow, and two friction hypotheses | None: no screenshot or visual model output | Partial |
| Saved Gem with tested instruction contract | Outline `:92-96`, deliverable `:129` | Slide 05 `:57-80`, `:112-143` | Demo 09 supplies instructions and two-draft test plan | None: no Gem, preview, drafts, response, or saved state | Partial |
| Selective Canvas edit preserving meaning | Outline `:94-96` | Slide 05 `:123-153` | Demo 10 requests one selected-paragraph edit and comparison | None: no draft, Canvas state, original/revised text, or version evidence | Partial |
| Formula-driven Sheets tracker | Outline `:98-102`, deliverable `:130` | Slide 06 `:57-78`, `:124-134` | Demo 11 requests columns, dropdown, formula, and known-date tests | None: no Sheet, formula, dropdown state, or test values | Partial |
| Confirmed-facts Docs handoff and approval gate | Outline `:100-104`, deliverable `:130` | Slide 06 `:110-187` | Demo 12 requests a fact-constrained announcement | None: no source Sheet, generated Doc, comparison, or approval state | Partial |

All twelve are after their conceptual preparation and before the corresponding lab in the slide sequence. The sequence is sound; the execution trace is not.

## Technology Execution Map

| Input | Target technology | Operation | Actual evidence | Showcase test |
|:---|:---|:---|:---|:---|
| Prepared Gmail thread + Drive specification | Gemini web app connected apps | Retrieve latest thread and compare sources | Prompt text only (`01:7-22`, `02:7-22`) | Unverified; without a live account, the same visible result could be typed or fabricated |
| Decision context and constraints | Gemini web app | Generate three role lenses and consensus | Prompt text only (`03:7-22`, `04:7-22`) | Unverified; no model response demonstrates operation |
| Dense PDF | Gemini file upload/document understanding | Extract and review claims; export to Sheets | Prompt text only (`05:7-21`, `06:7-21`) | Unverified; no PDF parsing, table, review, or export occurs in repository |
| Public YouTube video | Gemini video understanding | Identify claims and timestamps | Prompt text only (`07:7-21`) | Unverified; no URL/video request or timestamp output |
| Prepared screenshot | Gemini image understanding | Read visible controls and infer flow hypotheses | Prompt text only (`08:7-21`) | Unverified; no image upload or vision result |
| Two drafts and Gem instructions | Gemini Gems and Canvas | Save/test Gem and apply selective edit | Prompt/delivery plan only (`09:7-21`, `10:7-21`) | Unverified; no persistent state or Canvas edit |
| Blank native Google Sheet | Help Me Organize / Gemini in Sheets | Create tracker, dropdowns, formula, and test dates | Prompt text only (`11:7-21`) | Unverified; no native Sheet state change |
| Confirmed tracker facts | Help Me Write / Google Docs | Draft controlled announcement | Prompt text only (`12:7-21`) | Unverified; no cross-surface handoff |

The hardcoded-showcase test does not establish a hardcoded implementation: these files do not print prepared results. However, they also do not run the target technology, so no result can be attributed to Gemini, Connected Apps, file understanding, video/image understanding, Gems, Canvas, Sheets, or Docs. The evaluator's “no observable evidence” cap applies.

## Scorecard

Ratings are 0–5; points are `rating / 5 × weight`. The compact per-demo rows below score every rubric dimension in this order: **alignment / technology fidelity / authentic problem / executable correctness / observability / slide-timing-readiness / portfolio progression** (weights 15/20/15/20/10/10/10).

| Demo | Alignment | Technology | Authentic | Executable | Observable | Ready | Progression | Total |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| 01 | 4.5 | 2.0 | 4.0 | 1.0 | 1.5 | 2.0 | 3.5 | 51.5 |
| 02 | 4.0 | 1.5 | 3.5 | 1.0 | 1.5 | 2.0 | 3.5 | 46.5 |
| 03 | 4.5 | 2.0 | 4.0 | 1.0 | 2.0 | 2.5 | 3.5 | 53.5 |
| 04 | 4.0 | 1.5 | 3.5 | 1.0 | 1.5 | 2.0 | 3.5 | 46.5 |
| 05 | 4.0 | 1.5 | 3.5 | 1.0 | 1.5 | 2.0 | 3.5 | 46.5 |
| 06 | 4.0 | 1.5 | 3.0 | 1.0 | 1.5 | 2.0 | 3.0 | 44.0 |
| 07 | 4.0 | 1.5 | 3.5 | 1.0 | 1.5 | 1.5 | 3.0 | 44.5 |
| 08 | 4.0 | 1.5 | 3.5 | 1.0 | 1.5 | 2.0 | 3.0 | 45.5 |
| 09 | 4.0 | 1.5 | 3.5 | 1.0 | 1.5 | 1.5 | 3.0 | 44.5 |
| 10 | 4.0 | 1.5 | 3.5 | 1.0 | 1.5 | 1.5 | 3.0 | 44.5 |
| 11 | 4.0 | 1.5 | 3.5 | 1.0 | 1.5 | 2.0 | 3.0 | 45.5 |
| 12 | 4.0 | 1.5 | 3.5 | 1.0 | 1.5 | 1.5 | 3.0 | 44.5 |

The strongest scores are alignment and authentic prompt shape. Executable correctness is 1.0 for all because no documented command, fixture, or artifact can be run; this is not a claim that the underlying Gemini product is broken.

## Technical Verification

| Command or check | Expected | Actual | Result |
|:---|:---|:---|:---|
| `day1/demos/01-connected-retrieval-prompt.md` through `12-docs-announcement-handoff.md` | Each demo can be run/rehearsed from its documented instructions | Each file is 22–26 lines of Markdown containing purpose/setup or prompt/delivery/takeaway; none contains an executable command, fixture path, expected output, or captured artifact | **Blocked / unverified** |
| Matching slide run references | Exact runnable command and observable signals | Slides say `Run day1/demos/*.md` (e.g. slide 01 `:200-219`, slide 02 `:136-166`, slide 03 `:137-168`, slide 04 `:134-154`, slide 05 `:135-153`, slide 06 `:124-144`); `.md` is prose, not a runnable command | **Blocked** |
| Dependency/setup resolution | Resolve the documented course stack | No dependency or lock files, local setup instructions, account matrix, fixture set, or generated artifacts exist in this checkout; companion/setup repos are only links (`README.md:124-127`) | **Not verifiable** |
| Live Gemini connected apps, uploads, YouTube, Gems, Canvas, Sheets, Docs | Real operation produces inspectable output/state | No authenticated browser session, inputs, outputs, or Workspace artifacts supplied; execution is unavailable and must not be represented as passed | **Unverified** |
| Slide source references | Referenced diagrams and slide Markdown paths exist | All six slide files and referenced Day 1 diagram files are present by inventory; this validates paths only, not demos | **Pass for path existence** |
| Course artifact immutability | No demos/slides/quizzes/catalogs modified | Report-only review; no source edits made | **Pass** |

## Classroom Run of Show

The catalog allocates 60 minutes to each instructional block (`catalog/gemini-pro-sequential-outline.md:106-121`). The intended demo moments are visible, but the current materials do not provide enough run/recovery detail for a reliable classroom show.

| Phase | Estimated time | Instructor action | Learner observation or response |
|:---|---:|:---|:---|
| Sessions 1–2 retrieval/decision | 10–15 min demo time each | Instructor must manually authenticate, select connected apps, provide fixtures, run prompts, and capture before/after responses | Predict sources/role output, then compare actual citations and assumptions; currently no expected output is supplied |
| Session 3 PDF extraction/review | 10–15 min demo time | Upload a prepared PDF, inspect rows, review flags, export only after sampling | Compare page/denominator/footnote evidence; currently no PDF or expected rows exist |
| Session 4 video/image | 10–15 min demo time | Supply a public video and cropped screenshot, replay timestamps, inspect visual claims | Separate timestamp/observation from interpretation; timing and fallback are not operationalized in demos |
| Session 5 Gem/Canvas | 10–15 min demo time | Create and test Gem, move draft to Canvas, compare selected edit | Observe persistence and meaning preservation; no account fallback or expected output is provided in demo files |
| Session 6 Sheets/Docs | 10–15 min demo time | Create tracker, test three dates/statuses, hand confirmed rows to Docs, review approval gate | Inspect formula/dropdown/fact parity; no sample tracker or known expected values is supplied |

## Critical Conditions and Caps

- **Triggered: no observable evidence proves claimed behavior (cap 59).** Every demo contains a useful prompt and delivery script but no model-produced response, source citation, file state, spreadsheet, document, Gem, Canvas version, or screenshot/video result.
- **Triggered: matching demo slide materially inaccurate as a run instruction (cap 69, dominated by 59).** “Run `<path>.md`” is not executable. The slides do list useful observation signals, but cannot provide a runnable command (`slides/01:200-219`, `02:136-166`, `03:137-168`, `04:134-154`, `05:135-153`, `06:124-144`).
- **Not triggered: hardcoded showcase.** No prepared output is printed, so the narrower hardcoded-output condition is not proven. The absence of actual execution still blocks a pass.
- **Not triggered: unapproved technology.** The target tools are the catalog-approved Gemini/Workspace stack (`catalog:12-19`, `:32-34`). Their availability is documented as variable, but no account test exists.
- **Not triggered: code/dependency defect.** There is no executable demo code to diagnose; the defect is missing executable evidence, not a failed runtime.

## Findings

### Blockers

1. **All 12 demos are non-runnable artifacts.** Locations: `day1/demos/01-connected-retrieval-prompt.md:7-26` through `12-docs-announcement-handoff.md:7-22`. Evidence: Markdown prompts and delivery steps contain no command, fixture, expected output, or artifact. Classroom impact: instructor cannot rehearse the claimed behavior from source control, and the reviewer cannot verify it. Smallest useful correction: add a documented live run procedure, supported account prerequisites, prepared fixture identifiers, expected observable signals, and a captured verification checklist for each demo; do not fake outputs.

2. **Every matching slide instructs the instructor to run prose as if it were a command.** Locations: `day1/slides/01-connected-workspace-data-retrieval.md:200-219`, `02-cognitive-frameworks.md:136-166`, `03-agentic-workflows-deep-synthesis.md:137-168`, `04-multimodal-analysis.md:134-154`, `05-persistent-personas.md:135-153`, `06-native-workspace-in-app-automation.md:124-144`. Evidence: each says `Run day1/demos/<name>.md`. Classroom impact: predictable launch failure and improvisation. Smallest useful correction: replace with explicit UI steps or an executable launcher only if it genuinely invokes the target mechanism; keep the exact same command in the demo artifact and slide.

3. **No local project/setup evidence or prepared inputs is available.** Locations: catalog `:32-34`, README `:124-127`; absent local `day1/breakout-*`, fixture, setup, dependency, and lock-file paths. Evidence: repository inventory contains only primary catalog/slides/demos/research/diagrams/quizzes. Classroom impact: account entitlement, connected-app access, sample data, upload limits, and fallback paths cannot be validated before class. Smallest useful correction: link or provide the approved companion/setup evidence and a non-sensitive fixture manifest; do not add confidential data to this authoring repo.

### Major

1. **Technology fidelity is asserted but not evidenced.** All demos name Gemini features (`@Gmail`, `@Google Drive`, PDF upload, YouTube, image upload, Gems, Canvas, Help Me Organize, Help Me Write), but none records an input reaching the operation or a state/output produced by it. This directly conflicts with evaluator requirements `SKILL.md:70-109`.
2. **No reproducible verification record exists.** Demos 02, 04, 06, 07, 08, 10, 11, and 12 specifically require comparison or checking, but provide no baseline, expected result, source, test cases, or pass/fail record (`02:17-22`, `04:13-21`, `06:13-21`, `07:13-21`, `08:13-21`, `10:13-21`, `11:13-21`, `12:13-21`).
3. **The setup risk is under-specified for variable product surfaces.** Research repeatedly says account, plan, admin, location, and product-surface availability varies (`connected...research.md:13`, `multimodal...research.md:11`, `persistent...research.md:9`, `native...research.md:9`). The slides mention fallbacks in Session 6 (`06:170-177`) but the individual demos do not specify an actionable fallback.
4. **The portfolio has no offline risk-balanced rehearsal path.** The evaluator expects sensible offline/live balance (`SKILL.md:139-150`); all twelve demos depend on live Gemini or Workspace state, while no deterministic substitute preserves the mechanism for rehearsal.

### Moderate

1. **Expected outputs are too implicit for instructional observability.** Prompts specify fields, but no sample output shape, known-good/known-bad row, or stop condition is included. This weakens cause/effect even when an instructor has a working account.
2. **Timing and recovery are absent from demo artifacts.** The catalog gives 60-minute blocks, but no demo states duration, failure recovery, or transition budget (`catalog:106-121`; evaluator `SKILL.md:126-137`).
3. **Several demos require an unstated handoff state.** Demo 06 assumes an extracted table; Demo 10 assumes a draft already in Canvas; Demo 12 assumes a verified tracker. The dependency is described in prose but not delivered as a fixture or artifact.

### Minor

1. **Naming is understandable but asymmetric.** Paired titles vary between “prompt,” “verification,” “review,” “handoff,” and product action without a shared fixture/run convention, making a future automation or rehearsal matrix harder to build.
2. **The demos do not identify an account/feature availability check at the point of use.** The research and Session 6 slides do state availability variability, so this is a local delivery-readiness gap rather than a catalog alignment problem.

## What Works

- The six-session progression is coherent and matches the catalog's stated path from connected retrieval through decision framing, document evidence, multimodal analysis, reusable assistants, and Workspace automation (`catalog:10-19`, `:54-104`).
- Prompts are bounded and generally authentic: source scope and evidence/inference separation in 01 (`:13-15`), recency and no-inference guard in 02 (`:13-15`), concrete constraints in 03/04, exact-copy and unresolved handling in 05, and fact-preserving handoff in 12.
- Verification is treated as part of the lesson rather than an afterthought. Slides explicitly teach source inspection, sampling, replay, human review, and approval gates (`slides/01:188-194`, `03:123-168`, `04:168-183`, `06:158-187`).
- Privacy and product limitations are acknowledged in the catalog, research, and slides: prepared/non-sensitive data, account-dependent availability, timestamp uncertainty, human approval, and manual fallback.
- The paired-demo structure is pedagogically promising: retrieval then repair, persona generation then revision, extraction then review, and tracker creation then controlled Docs handoff. Preserve this progression when adding executable evidence.

## Prioritized Improvement Plan

1. **P0 — Make each demo honestly runnable and verifiable.** Affected: all `day1/demos/*.md` and matching six slide files. Add exact UI/run steps, fixture IDs or URLs, prerequisite/account checks, expected signals, fallback, and a verification record. Expected impact: removes the all-demo execution blocker and permits a high-confidence re-evaluation.
2. **P0 — Supply approved setup and fixtures.** Affected: companion/setup integration referenced by `README.md:124-127` and catalog `:32-34`; at minimum prepare Northstar email/spec, old/new threads, dense PDF, public video, cropped screenshot, two drafts, and a tracker fact set. Keep data fictional/non-sensitive and document permissions. Expected impact: makes connected, upload, multimodal, and cross-surface claims testable.
3. **P1 — Correct slide commands and preserve exact traceability.** Affected: slide demo blocks listed above. Replace `Run ...md` with an actual browser/UI procedure or a real launcher. Add duration, expected output, recovery, and feature-unavailable fallback. Expected impact: prevents classroom launch failure and improvisation.
4. **P1 — Record actual technology execution evidence.** For each demo capture input, target feature, operation, output/state, and showcase-test result. For Sheets explicitly record formula text and past/today/future values; for Docs compare every fact; for Gems/Canvas record preview, saved state, original, and revised text. Expected impact: raises technology fidelity, correctness, and confidence without changing objectives.
5. **P1 — Add an offline rehearsal path that does not pretend to prove live behavior.** Use screenshots/transcripts/manual templates only as clearly labeled fallback orientation; retain at least one live run per technology claim. Expected impact: improves classroom risk balance while preserving technology fidelity.
6. **P2 — Add concise instructor timing and recovery notes.** Pair each demo with a 5–15 minute run-of-show and a stop/retry rule, then verify the full 435-minute schedule. Expected impact: improves readiness and protects lab time.

## Re-evaluation Checklist

- [ ] Read the highest prior report for this exact scope before a future re-evaluation; this is `20260826-v1-day1-demo-evaluation.md` for today.
- [ ] Confirm all six authoritative slide files, catalog, research files, demo files, and approved companion/setup artifacts are present.
- [ ] Run every documented demo from the documented working directory/account with no source edits.
- [ ] Record exact commands or UI actions, feature/account prerequisites, inputs, outputs/state changes, exit/result status, and repeated-run behavior where meaningful.
- [ ] Prove each target mechanism with the technology execution map and apply the showcase test; do not count labels or narrated expected output as evidence.
- [ ] Verify each source citation/date, PDF row, video timestamp, image observation, Gem preview/save state, Canvas meaning preservation, Sheets formula/dropdowns/date cases, and Docs fact parity.
- [ ] Confirm matching slide title, exact run instruction, placement, observable signals, duration, recovery, and fallback.
- [ ] Re-score all seven dimensions for all twelve demos, show caps, update confidence, and write a new same-scope version rather than overwriting this report.
- [ ] Confirm `git diff` shows no changes to demos, slides, quizzes, catalogs, or setup artifacts during the evaluation pass.
