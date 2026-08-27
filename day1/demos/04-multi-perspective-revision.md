# Demo: Repair a Generic Recommendation

## Purpose

Demonstrate how to revise a multi-persona prompt when every role gives broad, interchangeable advice.

## Revision request

Replace the bracketed placeholders with your decision criteria.

```text
The role responses are too generic. Re-run the analysis using these concrete criteria: migration must finish within [ROLLOUT-PERIOD], the tool must [DATA-EXPORT-REQUIREMENT], administrators need [GOVERNANCE-REQUIREMENT], and the team has [TRAINING-CAPACITY] for training. For each criterion, show which role raised it, the evidence needed, and whether it changes the recommendation. Identify the strongest rejected alternative.
```

## Delivery

1. Show the first generic response.
2. Apply the bounded revision request.
3. Compare the new table with the original recommendation.
4. Highlight the unresolved claim that still needs vendor or policy verification.

## Takeaway

Useful revision adds decision criteria and evidence requirements, not just more role names.
