# Demo: Board of Three Experts

## Purpose

Show how role separation and an output schema expose tradeoffs in a software-tool decision.

## Prompt

Replace the bracketed placeholders with details from your decision.

```text
We are deciding whether a [TEAM-SIZE]-person [TEAM-FUNCTION] team should adopt [TOOL-OR-PROCESS]. Constraints: a [ROLLOUT-PERIOD] rollout, [BUDGET-CONSTRAINT], existing [CURRENT-PLATFORM] usage, and [DATA-RETENTION-REQUIREMENT]. Have a cynical risk manager, a visionary optimist, and a pragmatic project manager debate the decision. For each role, list assumptions, strongest argument, risks, and evidence needed. End with a consensus table of risks, rewards, recommendation, confidence, and unresolved questions. Mark claims that require verification.
```

## Delivery

1. Ask learners which role is most likely to identify migration risk.
2. Run the prompt and compare the three lenses.
3. Inspect whether the final recommendation is supported by stated constraints.
4. Ask learners to name one missing fact before accepting the recommendation.

## Takeaway

Personas organize inspection; they do not turn generated claims into independent evidence.
