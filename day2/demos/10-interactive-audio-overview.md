# Demo: Interrogate an Audio Overview

## Purpose

Generate a two-host policy briefing, join it in Interactive mode, and verify the hosts' answer about an exception.

## Preparation

Open the verified `Remote Access Policy Review` notebook and select only the policy and implementation guide. Prepare the scripted fallback below in case audio generation or Interactive mode is unavailable.

## Deep Dive prompt

```text
Create a Deep Dive for managers implementing the remote-access policy. Explain the 10 October enrollment deadline, 15 October effective date, and field-operations exception. State that the rollout method remains unresolved. Do not turn the public article's recommendation into company policy. Pronounce “managed-access profile” as three distinct words.
```

## Interactive question

```text
Which source establishes the field-operations exception, who qualifies, and what condition ends it?
```

## Delivery

1. Create a new Deep Dive with Interactive mode enabled.
2. Play the overview and listen for dates, conditions, and unsupported additions.
3. Select Join, wait for the hosts, and ask the bounded question.
4. Open the policy passage and verify all parts of the spoken answer.
5. Explain that shared audio contains the original overview, not the interaction.

## Offline fallback (local check, not Audio Overview evidence)

Run `python3 day2/demos/verify_offline_evidence.py --case interactive-audio-overview`. This checks authored interaction labels only; it does not generate audio or join Interactive mode.

Host answer: “The policy allows all field workers to use the old process indefinitely.” The answer fails because the exception requires approval and ends after regional security review.

## Takeaway

Interactive mode helps probe the material, but the spoken answer still needs passage-level verification.
