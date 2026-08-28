# Demo: Build a Contradiction-First Synthesis

## Purpose

Turn four mixed-authority policy sources into a claim-evidence matrix that preserves disagreement and missing information.

## Preparation

Open the `Remote Access Policy Review` notebook from Demo 05 or Breakout Lab 2.3. Select the policy, implementation guide, public article, and meeting notes.

## Prompt

```text
Compare the four selected sources for a manager preparing the remote-access rollout. Build a table with these columns: claim, policy evidence, implementation-guide evidence, other-source evidence, evidence status, and unresolved owner question. Cover the effective date, enrollment deadline, field-operations exception, and rollout method. Quote concise source language with citations. Use only these statuses: supported, contradicted, partial, unresolved. Do not resolve a conflict unless an authoritative source controls it.
```

## Delivery

1. Submit the prompt with all four sources selected.
2. Open citations for the effective date and field-operations exception.
3. Mark any row that combines a recommendation with a policy requirement.
4. Narrow partial claims and preserve unresolved questions.
5. Save only rows whose status and citations have been checked.

## Offline fallback (local check, not Notebook evidence)

Run `python3 day2/demos/verify_offline_evidence.py --case contradiction-first-synthesis`. This checks authored status signals only; it does not synthesize or cite sources.

Reject this generated row: “The company requires a phased rollout beginning 1 October.” The meeting note contains the unconfirmed date, and the public article recommends phasing without controlling company policy. The verified policy date is 15 October; the rollout method remains unresolved.

## Takeaway

A good synthesis exposes conflicts and missing evidence before it compresses the sources into a recommendation.
