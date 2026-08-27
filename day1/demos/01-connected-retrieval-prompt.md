# Demo: Connected Workspace Retrieval

## Purpose

Show how an explicit source scope turns a vague catch-up request into a verifiable project status report.

## Setup

Use a prepared, non-sensitive project email thread and matching specification in Google Drive. Confirm the instructor account can access both sources.

## Prompt

```text
@Gmail Find the most recent email thread about Project Northstar. List the blockers stated in the thread, including the date and supporting excerpt. Then use @Google Drive to compare those blockers with the Project Northstar Phase 1 specification. Return a table with blocker, source evidence, affected deliverable, and unresolved question. Clearly label evidence versus inference.
```

## Delivery

1. Run the prompt in Gemini and pause while learners predict what evidence should appear.
2. Open the cited Gmail thread and Drive document.
3. Compare the source dates and wording with the generated table.
4. Point out one supported claim and one inference that needs confirmation.

## Takeaway

A connected prompt is strongest when it names the source, constrains the request, and makes verification part of the output.
