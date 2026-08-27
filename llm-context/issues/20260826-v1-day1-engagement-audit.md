# Engagement Audit: Gemini Pro Day 1

## Executive Assessment

Day 1 has a strong **instructional arc**: connected retrieval → inspectable decisions → cited synthesis → multimodal verification → reusable assistance → Workspace artifacts. The catalog explicitly expects each session to combine a short demonstration with a usable learner artifact (`catalog/gemini-pro-sequential-outline.md:10-10,54-104`). The companion breakouts also contain unusually good engagement mechanics: private prediction, rotating roles, a verifier, human-review checkpoints, and short share-outs.

The principal engagement risk is not a lack of activities; it is **too much live work inside six one-hour sessions and too little reliable feedback evidence**. The six breakout evaluation reports all apply a 59/100 cap because the core behavior has no deterministic fixture/acceptance evidence and every launch handoff is marked `blocked pending exercise repair`. The demo evaluation likewise scores the twelve Markdown-only demos 46.5/100 and finds the “Run `day1/demos/*.md`” instructions non-runnable (`20260826-v1-day1-demo-evaluation.md:5-13,107-130`). A polished but wrong retrieval, timestamp, formula, or announcement can therefore pass as success.

Highest-value move: **repair and stage one bounded, checkable path for each companion breakout and demo before changing engagement wording**. Do not inject generic engagement into the breakout launch decks: all six launch handoffs are blocked, and the existing decks already have relevant prediction/check/share mechanics. After repair, trim repeated knowledge checks and use the recovered minutes for delayed retrieval and feedback.

Evidence confidence is high for source mapping and engagement design, but low for live product behavior: no authenticated Gemini/Workspace execution, generated artifact, media package, fixture, or test is included in the reviewed repositories.

## Current Inventory

### Scope and artifact inventory

| Source | Count | Coverage / finding |
|---|---:|---|
| Catalog / sequential outline | 1 | Six 60-minute instructional sessions; 360 instructional minutes in 435 elapsed minutes (`catalog/gemini-pro-sequential-outline.md:36-52,106-121`). |
| Marp slide decks | 6 | One per session; two demo handoffs and one breakout launch per deck (`day1/slides/01...md:200-225`, `02...md:136-171`, `03...md:137-172`, `04...md:134-158`, `05...md:135-157`, `06...md:124-148`). |
| Instructor demos | 12 | Two per session, all Markdown prompts/delivery notes; no executable run, fixture, output, or generated artifact (demo evaluation `:39-45`). |
| Kahoot files | 11 | Six session banks × 12 questions = 72 questions, plus five cumulative review banks × 6 questions = 30; 102 total question records. The six core banks are `day1-kahoot-1-connected-workspace.md` through `6-workspace-automation.md`; review banks are `1-2`, `1-3`, `1-4`, `1-5`, `1-6`. |
| Companion breakouts | 6 | Each has README, `start/`, `solution/`, and `solution/verification.md`: Inbox Interrogation, Board of Directors, Data Miner, X-Ray Vision Test, Building the Coach, Workspace Sorcerer. |
| Breaks / lunch | 3 | 15-minute morning break, 45-minute lunch, 15-minute afternoon break; no instructional engagement budget. |

### Activity counts by engagement type

| Type | Count in delivery materials | Cognitive profile | Assessment |
|---|---:|---|---|
| Chat waterfall | 2, both Session 1 introduction (`01...md:48-87`) | Active/constructive when learners write; limited feedback beyond an answer slide | Keep one; the second is useful orientation but should not consume lab-critical time. |
| Demo blocks | 12, two per session | Mostly passive unless the instructor actually pauses for the listed prediction/inspection | Keep the workflow, upgrade evidence and observation; do not count prose files as executed demos. |
| Demo predictions / source or output inspections | 12 stated opportunities, mainly around the demo blocks (`01...md:200-219`; analogous sections in decks 02–06) | Active → constructive | Strong design intent, inconsistent operational closure. |
| Kahoot | 6 core banks (scheduled status not stated) + 5 cumulative banks | Active recall, mostly recognition; no learner explanation or revision | Keep selectively; do not run every bank plus every breakout. Review banks are a reserve, not additional mandatory blocks. |
| Lab / breakout | 6 × 60 minutes in companion READMEs | Constructive/interactive/application | Keep as the main practice; repair acceptance evidence first. |
| Structured discussion / share-out | 6 breakout share-outs plus deck discussion prompts (e.g. `06...md:178`) | Interactive if reasons and artifact are collected | Keep embedded in labs; remove standalone generic discussion if it has no output. |
| Reflection / transfer | Explicit in Workspace Sorcerer (`README.md:48-54`) and implied in final share-outs | Constructive | Extend to a day-level if-then transfer plan; currently uneven. |
| Retrieval reset | 0 explicit delayed no-notes resets across Day 1 | Missing | Add one only after replacing/reducing a cumulative Kahoot or recap. |

The materials contain essentially no standalone teach-back, flawed-artifact review, confidence check, or scenario simulation. The strongest substitutes are the verifier roles, source critique, repair loops, and share-outs inside the breakouts.

## Engagement Ledger

| Location | Concept / learner output | Activity; response mode; cognitive mode | Feedback / delay / access | Timing; duplication judgment |
|---|---|---|---|---|
| S1, deck 01 “Introduce Yourself” (`:48-63`) | Prior experience and learning need | Chat waterfall; public chat; active | Answer slide follows; written/private draft is available | 4–6 min; unique orientation |
| S1, deck 01 “Your Gemini Experience” (`:64-87`) | Challenge/question for the day | Chat waterfall; public chat; constructive | Instructor synthesis; no later return specified | 4–6 min; benign overlap with intro, but costly beside lab |
| S1, demos 01–02 (`01...:7-26`, `02...`) | Retrieve latest Gmail/Drive evidence; repair stale/generic result | Predict → observe → explain; chat/whole group; constructive | Source opening and before/after comparison intended; live evidence missing | 10–16 min beyond runtime; same retrieval concept progresses usefully |
| S1, Inbox Interrogation README (`:11-63`) | Status report with evidence, inference, blockers | Breakout; group artifact; interactive | Verifier and share-out; no deterministic fixture; private prediction and roles support access | 60 min; main application, not additive to a full 60-min lecture |
| S2, demos 03–04 (`02...:136-165`) | Distinct lenses; repair generic recommendation | Demo prediction/repair; whole group; constructive | Human judgment checkpoint; no claim fixture | 10–16 min beyond runtime; useful progression into lab |
| S2, Board of Directors README (`:11-61`) | Risks/rewards/recommendation and rejected alternative | Breakout; group table; interactive | Claim check, reviewer, share-out; no authoritative facts | 60 min; decision setup may overrun (evaluation `:70-75`) |
| S3, demos 05–06 (`03...:137-166`) | Extract claims, inspect page/context/methodology, export reviewed table | Prediction + artifact review; group; constructive/interactive | PASS/CHECK/UNRESOLVED intended; no PDF or Sheet evidence | 12–18 min beyond runtime; review adds value but overlaps Kahoot questions heavily |
| S3, Data Miner README (`:11-50`) | Cited claim table and limitation | Breakout; artifact; interactive | Five source checks and verifier; “every claim” unbounded and no claim inventory | 60 min; export plus extraction is tight (evaluation `:67-75`) |
| S4, demos 07–08 (`04...:134-153`) | Timestamped arguments; visible observation vs friction hypothesis | Predict/replay/critique; group; constructive | Replay and visible-evidence check; media package missing | 10–16 min beyond runtime; useful modality progression |
| S4, X-Ray Vision README (`:11-50`) | Timestamped notes + visual critique | Breakout; artifact; interactive | Original-media replay, uncertainty, share-out; media is learner-selected | 60 min; selection/cropping consumes practice time (evaluation `:67-74`) |
| S5, demos 09–10 (`05...:135-153`) | Gem contract, two tests, selective Canvas edit | Predict/test/compare; group; constructive | Human approval and original retention; no draft/Canvas evidence | 10–16 min beyond runtime; useful progression, but same review principle recurs |
| S5, Building the Coach README (`:11-60`) | Saved tested Gem + meaning-preserving edit | Breakout; artifact; interactive | Reviewer approval/share-out; no draft fixtures or Canvas rubric | 60 min; task choice and feature access risk (evaluation `:66-74`) |
| S6, demos 11–12 (`06...:124-144`) | Formula tracker and fact-constrained announcement | Predict/inspect/approve; group; constructive | Formula/date/fact checks intended; no live artifacts | 10–16 min beyond runtime; handoff is a strong distinct capstone |
| S6, Workspace Sorcerer README (`:11-54`) | Verified Sheet + reviewed Docs announcement + transfer reflection | Breakout; two artifacts; interactive | Verifier, approval gate, reflection; no deterministic acceptance artifact | 60 min; two blank artifacts are tight (evaluation `:67-75`) |
| S1–S6 core Kahoot banks | Concept recognition and misconceptions | Kahoot; anonymous poll; active | Correct answer is supplied; reasoning/debrief not specified | Likely 4–8 min per 6–12-question bank; duplicates demo/lab checks |
| S1–S6 cumulative review banks | Delayed recall across prior sessions | Kahoot; active | Correct answers only; no scheduled placement or explanation | Reserve only; valuable delayed retrieval, but redundant if run adjacent to core Kahoot |

**Option-length check:** the six core Kahoot files and review files use short answer lines in the inspected question records; no clear >85-character option was identified in the inventory pass. Recheck automatically before delivery if question wording changes.

## Session Rhythm

The catalog allocates 60 minutes to each session but does not allocate minutes among explanation, two demos, Kahoot, and breakout (`catalog/...:106-121`). The decks show the sequence “concept → two demos → breakout,” with no explicit timing markers. A realistic 60-minute session cannot contain a full 60-minute breakout plus meaningful concept teaching and two live demonstrations. The companion README budgets demonstrate that each breakout alone consumes the whole hour (`.../breakout-*/README.md`), so the catalog should be interpreted as either a teach-then-lab schedule needing additional time or a session where demos are very short and embedded in the lab launch.

| Session | Current rhythm / risk | Engagement budget judgment |
|---|---|---|
| 1 | Two chat waterfalls, explanation, two demos, then a 60-min lab. Strong opening but highest setup pressure; retrieval activity is repeated immediately in demo, breakout, and Kahoot 1. | Keep one waterfall; cap live demo to one representative run + repair; use lab as the substantial activity. |
| 2 | Framework explanation, two persona demos, 60-min decision breakout, core Kahoot likely adjacent if scheduled. | Good constructive/interactive arc, but choice of decision and fact verification can overrun. Use a prewritten scenario card. |
| 3 | Dense synthesis explanation, extraction and export demos, 60-min PDF lab. | Highest technical/setup risk; bounded report and staged claim sample are required. Do not add another activity. |
| 4 | Two multimodal demos plus learner-selected media/image lab. | Selection and cropping consume the application window; pre-stage media. Keep replay as feedback, not another quiz. |
| 5 | Gem contract, two test demos, Canvas demo, 60-min lab. | Strong human-control loop but feature access and task choice threaten completion. Provide a default draft path. |
| 6 | Two Workspace demos, two blank artifacts, approval gate, reflection, 60-min lab. | Strongest transfer and closure, but most artifact/setup overhead. Stage a template; make creation-from-blank stretch. |

Across the day, there are no explicit long passive stretches measured by minutes, but the deck structure puts explanation plus two demo scripts before each practice block. There are also likely back-to-back activities if a core Kahoot is run immediately before/after a demo or lab; the standards explicitly advise avoiding this (`engagement-standards.md:83-90`). Kahoot scheduling is absent, so it must not be assumed as free time.

## Concept Duplication Map

| Concept | Repeated locations | Classification | Action |
|---|---|---|---|
| Evidence vs inference / verify before sharing | S1 slides, demos 01–02, Inbox lab, Kahoot 1, review banks, later decks | Useful progression in source inspection; redundant when restated as MCQ after the lab | Keep one live source-check; use a later review question as delayed retrieval only. |
| Persona output is not independent evidence | S2 slides, demos 03–04, Board lab, Kahoot 2, review banks | Useful progression from misconception → repair → application; 3–4 immediate recognitions compete | Keep lab checkpoint; remove one same-format quiz item from a selected bank. |
| Page references / claim verification | S3 slides, demos 05–06, Data Miner lab, Kahoot 3 and cumulative banks | Mostly benign reinforcement, but 12-question Kahoot repeats fields already being checked in the artifact | Keep source review; reserve Kahoot 3 or cut to 3 diagnostic questions. |
| Timestamp replay and observation vs interpretation | S4 slides, demos 07–08, X-Ray lab, Kahoot 4/reviews | Useful progression because replay is authentic; quiz repetition is redundant | Keep replay and visual evidence; use one delayed item, not the full bank. |
| Human approval / meaning preservation | S5 slides, demos 09–10, Coach lab, Kahoot 5/reviews | Useful progression if learners compare versions; recognition questions are weaker than artifact decision | Keep original-vs-revised approval; replace duplicate recognition with one critique prompt. |
| Formula/date/fact checks and approval | S6 slides, demos 11–12, Sorcerer lab, Kahoot 6/reviews | Useful progression; full Kahoot beside a two-artifact lab competes for scarce time | Keep the handoff and reflection; make Kahoot 6 optional diagnostic. |
| Verification mindset across all six sessions | Every deck takeaway, all 12 demos, six labs, 11 quiz files | Theme is coherent but over-repeated as slogans | Convert one end-of-day recap into no-notes retrieval + if-then transfer plan. |

## Gaps

1. **Delayed retrieval:** No explicit no-notes retrieval reset revisits a key concept at the start of a later session. Cumulative review banks could fill this gap, but their placement is unspecified and they should not be run adjacent to a core quiz.
2. **Feedback closure:** Most quiz files provide a correct letter but not a required explanation, confidence response, or revision. Demo observation bullets specify what to look for, but no captured output exists. Companion share-outs provide the best closure, yet six reports identify missing deterministic acceptance evidence.
3. **Evidence layer / execution:** All twelve demos are Markdown-only; “Run `<file>.md`” is not executable. All six breakout reports are blocked pending exercise repair. Risks are documented as: missing Gmail/Drive fixtures; no checkable persona claims; no bounded PDF/claim inventory; no approved video/transcript/image key; no draft/Canvas rubric; and no Sheet/Docs formula/fact acceptance artifact.
4. **Timing feasibility:** Each breakout is budgeted at 60 minutes, while each session is also only 60 minutes and includes teaching plus two demos. There is no honest per-session allocation or transition/setup buffer.
5. **Participation equity:** Breakouts have private prediction, role rotation, written artifacts, and fallback language in several cases. Deck-level chat relies on fast typing and public response; there is no consistent anonymous/private alternative. Cameras are not required, which is good.
6. **Access and fallback:** Inbox, PDF, media, Gems/Canvas, and Workspace features depend on accounts or live services. Fallbacks are strongest in S1/S4/S6 but weak or absent for Coach; reports specifically flag feature availability and instructor-dependent setup.
7. **Transfer:** Workspace Sorcerer has an explicit reflection; other sessions mostly end with share-out rather than an if-then workplace plan. A single day-level transfer artifact would be more efficient than six generic “adapt this” prompts.
8. **Artifact quality calibration:** Worked examples are fictional/illustrative and sometimes have fewer rows than the basic completion target. Without labels and acceptance keys, learners cannot distinguish shape examples from expected answers.
9. **Kahoot governance:** Eleven files exist, but the outline does not schedule any. Running all six core banks plus review banks would overload the shared engagement budget and turn verification into competition rather than reasoning.

## Prioritized Recommendations

### Keep

1. **Keep the six-session arc and six application breakouts.** It aligns tightly with the catalog outcomes (`catalog:21-30,123-130`) and gives authentic workplace artifacts.
2. **Keep private prediction, rotating roles, verifier ownership, source replay, human approval, and one-minute share-outs** inside the companion READMEs. These are the most equitable and cognitively deep existing mechanics.
3. **Keep the S3 source sampling, S4 replay, S5 original retention, and S6 tracker-to-announcement fact gate.** They make verification concrete rather than rhetorical.
4. **Keep the six core Kahoot banks as optional diagnostics/reserve.** They are concise and cover misconceptions; do not treat file existence as a requirement to run them.

### Upgrade

1. **Upgrade demos to evidence-backed predict–commit–observe–explain.** Provide one non-sensitive fixture/input, a live run procedure, expected observable signals, and a captured instructor result for each of 12 demos. Retain current deck locations; do not add generic slides.
2. **Upgrade each companion exercise with a bounded acceptance contract before launch.** Follow the six evaluation reports: source manifest for Inbox; synthetic claim packet for Board; bounded PDF + claim inventory for Data Miner; approved media/transcript/image key for X-Ray; two draft fixtures + Canvas rubric for Coach; copyable tracker/template + fixed-date checks for Sorcerer.
3. **Upgrade quiz feedback:** require a brief reason or confidence signal for selected diagnostic questions, and revisit one misconception in a later session. Keep anonymous response paths.
4. **Upgrade timing controls:** publish an explicit allocation such as 8–12 minutes concept/demo launch + 40–45 minutes practice + 5–8 minutes share-out, or move the full 60-minute breakout outside the instructional hour. Do not claim both a full lab and full lecture fit in 60 minutes.
5. **Upgrade transfer once at day end:** have each learner write “If [work situation], I will [bounded Gemini/Workspace action], and I will verify [evidence] before sharing.”

### Replace

1. **Replace one same-session core Kahoot per day with a delayed retrieval reset** at the start of the next session (2–4 minutes, no notes, then corrective feedback). The cumulative review banks can supply prompts, but select only one or two items rather than running a full bank.
2. **Replace learner-selected media as the basic X-Ray path with an instructor-staged media package.** Keep learner choice as stretch; this directly addresses the evaluation’s timestamp/visual verification risk.
3. **Replace blank-artifact creation as the basic S6 path with a copyable staged template and fixed reference date.** Keep from-blank construction as intermediate/stretch.
4. **Replace unrestricted S2/S5 task choice with a default scenario/draft**, then allow alternatives only if time remains. This preserves agency without sacrificing completion.

### Remove

1. **Remove any assumption that all 11 Kahoot files should be delivered.** Unscheduled cumulative banks are reserve material; running them all would duplicate labs and consume practice time.
2. **Remove or shorten generic recap/discussion prompts that collect no decision, explanation, artifact, or instructor response.** A title or “discuss” callout alone is not meaningful engagement under the standard.
3. **Remove “Run `day1/demos/<file>.md`” as a purported execution instruction** once the decks are next edited; replace it with the repaired, explicit run procedure. Do not represent current prose paths as runnable.

## Proposed Engagement Plan

This plan assumes the catalog’s 60-minute session total remains fixed and treats the breakout as the substantial activity. If a full 60-minute breakout is mandatory, add six separate lab hours; there is no honest zero-net-time way to preserve full teaching, two demos, and a full breakout inside each current hour.

| Session | Proposed pattern | Net impact within current 60 min |
|---|---|---:|
| S1 | 4 min private/chat waterfall; 8 min concept + one evidence-backed demo/repair; 43 min bounded Inbox lab; 5 min share-out | 0 min; save 4–8 min by dropping second waterfall/shortening second demo |
| S2 | 6 min retrieval from S1; 9 min framework + one demo; 40 min scenario-card Board lab; 5 min share-out | 0 min; replace likely core Kahoot with retrieval |
| S3 | 8 min concept + one extraction demo; 44 min bounded Data Miner lab; 8 min source/export feedback | 0 min; no separate Kahoot |
| S4 | 6 min retrieval; 8 min multimodal demo with staged media; 40 min X-Ray lab; 6 min replay/share | 0 min; remove media-selection overhead |
| S5 | 8 min concept + one Gem/Canvas evidence run; 44 min default Coach lab; 4 min approval report-out | 0 min; stretch variants only after basic path |
| S6 | 8 min concept + one tracker-to-Docs demo; 42 min staged Sorcerer lab; 5 min approval; 5 min day-level if-then transfer | 0 min; replace core Kahoot with transfer/approval closure |

**Overall net time:** 0 minutes added if demos are short and one activity is replaced per session. This is not an estimate that all current content fits unchanged; it requires removing the second live demo or using it as a short evidence comparison, not narrating two full demos. To retain both full demos and a full 60-minute breakout in every session would require approximately **+72–96 minutes** across the day for transitions, or six separate lab hours depending on delivery design.

## Implementation Order

1. Repair and stage companion exercise evidence first, following the six existing breakout reports. Do not edit or generate launch decks until each handoff is unblocked.
2. Repair the 12 demo evidence layers and replace non-runnable run language with explicit procedures; re-run the demo evaluator.
3. Decide and document the Kahoot schedule: at most one short diagnostic or delayed review per session; reserve the remaining files.
4. Run a timing-gap analysis against the chosen 60-minute pattern and verify transitions, account preflight, and fallback paths.
5. Only then make narrowly targeted engagement changes: one delayed retrieval reset, quiz feedback/confidence where useful, and one day-level transfer plan. Avoid generic injection into the six breakout launch decks.
6. Re-audit engagement for spacing, duplication, access, feedback closure, and net time; re-run breakout/demo evaluators after repaired artifacts are available.

## Evidence and Scope Notes

Reviewed: `catalog/gemini-pro-sequential-outline.md`; all six `day1/slides/*.md`; all twelve `day1/demos/*.md`; all eleven `day1/quizzes/*.md`; and the six companion breakout directories, including each README, start artifact, solution artifact, and verification artifact. Existing evidence used: `20260826-v1-day1-demo-evaluation.md` and the six `20260826-v1-day1-*-breakout-evaluation.md` reports. No course artifact was edited. Current date/scope had no prior `20260826-vN-day1-engagement-audit.md`, so this report is `v1`.
