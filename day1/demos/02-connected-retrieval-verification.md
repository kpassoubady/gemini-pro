# Demo: Verify a Connected-App Answer

## Purpose

Demonstrate why a plausible Workspace answer still requires source checking and prompt refinement.

## Setup

Use a prepared sample in which an older Gmail thread contains a superseded blocker and a newer thread changes its status. Keep the data non-sensitive.

## Prompt

Replace the bracketed placeholders with details from your project.

```text
@Gmail For [PROJECT-NAME], identify the latest thread that discusses [BLOCKER-KEYWORD]. Return the thread date, sender, exact blocker wording, and current status. Do not infer a resolution if the thread does not state one. Use @Google Drive to identify the corresponding [PROJECT-PHASE] requirement in [SPECIFICATION-NAME].
```

## Delivery

1. Ask learners which thread Gemini should select and why.
2. Run the prompt and inspect the cited sources.
3. If the older thread appears, refine with the latest date, sender, or exact project keyword.
4. Discuss the difference between retrieved evidence, an inference, and an unresolved question.

## Takeaway

Verification is part of retrieval. Check dates, permissions, and original wording before sharing a status report.
