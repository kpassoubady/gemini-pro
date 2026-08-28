# Demo: Build a Source-Grounded Presentation Plan

## Purpose

Create and review a plan for a fully editable presentation from approved Workspace sources, then inspect its evidence and narrative before Gemini generates the deck.

## Prerequisites

Before class, use `day1/demos/11-sheets-project-tracker.md` and `day1/demos/12-docs-announcement-handoff.md` to create two fictional Drive files named `LaunchTracker` and `LaunchAnnouncement`. If available, add an approved company presentation only as a style reference.

## Presentation brief

```text
Create a five-slide internal launch-readiness presentation for department leaders. The goal is to secure owners for unresolved launch tasks, not to claim final approval. Use only @LaunchTracker and @LaunchAnnouncement for facts. Structure the deck as: decision needed, current status, blockers and owners, next seven days, requested actions. Show the source for every date and status in concise slide text. Use a calm executive tone. Do not invent metrics, completion percentages, deadlines, customer impact, or approvals. Ask clarifying questions, then show me the source list and presentation plan before generating the deck.
```

## Plan review gate

Before approval, check that the plan:

1. Lists only the two approved content sources.
2. Separates current status from requested action.
3. Preserves unresolved and blocked states.
4. Includes exactly five slides with one purpose each.
5. Contains no unsupported percentage, outcome, or approval claim.

## Offline fallback (local check, not Gemini in Slides evidence)

Run `python3 day2/demos/verify_offline_evidence.py --case source-grounded-presentation`. This checks only authored plan signals; it does not create an editable presentation.

Compare these fictional plan lines before revealing the diagnosis:

- **Plan A:** “Launch is 90% complete and on track to increase adoption by 25%.”
- **Plan B:** “Two tasks remain blocked; leadership must confirm owners for the next seven days.”

Plan A invents completion and impact claims. Plan B stays within the stated purpose but still requires checking against the tracker.

## Delivery

1. Open a blank presentation and select Ask Gemini or Generate presentation.
2. Add the tracker and announcement as content sources; add the prior deck separately with Match presentation style.
3. Submit the brief and answer only clarifying questions supported by the sources.
4. Inspect Sources and each step in the generated plan; revise or delete unsupported steps.
5. Approve generation only after the plan passes the review gate.
6. If full-deck generation is unavailable, evaluate Plan A and Plan B with the same gate.

> Availability depends on the signed-in plan, account, administrator settings, desktop and language support, and rollout stage.

## Takeaway

The highest-leverage review happens before generation: constrain sources, inspect the plan, and reject unsupported claims before polished slides make them look credible.
