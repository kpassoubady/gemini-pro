# Demo: Control the Notebook Source Boundary

## Purpose

Show how selecting and deselecting sources changes the evidence available to Gemini Notebook without deleting material from the workspace.

## Source set

Use the fictional operational policy pack from `day2/breakout-workspace-builder/start/source-pack/` in the companion repo. Add all four files to one notebook and confirm that each imported source is readable.

## First question

```text
Using the selected notebook sources only, state the remote-access change, its effective date, the required employee action, and any exception. Cite the supporting passage for each statement. If sources conflict, describe the conflict instead of resolving it by assumption.
```

## Delivery

1. Select all four sources and submit the question.
2. Identify language influenced by the public article or ambiguous meeting note.
3. Deselect the article and meeting note while keeping the policy and implementation guide.
4. Submit the same question and compare claims, citations, and uncertainty.
5. Open each citation and verify that the passage supports the claim.

## Offline fallback (local check, not Notebook evidence)

Run `python3 day2/demos/verify_offline_evidence.py --case controlled-source-boundary`. This checks authored response signals only; it does not import sources or produce citations.

Compare these fictional responses:

- Response A says the change starts on 1 October and applies to every worker, citing an informal meeting note.
- Response B says the policy starts on 15 October and excludes approved field operations, citing the policy and implementation guide.

Response B uses the authoritative selected sources. The reviewer must still open both cited passages and check the date and exception.

## Takeaway

Source selection creates a temporary evidence boundary. It does not prove that every selected source is authoritative or that every citation supports the claim.
