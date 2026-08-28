# Demo: Repair One Slide Without Losing Control

## Purpose

Use a bounded prompt to repair an overloaded slide, then distinguish a fully editable slide from a generated image of a slide.

## Verified source extract

Use this fictional extract from `LaunchTracker`:

| Reference | Blocker | Owner | Date | Verified status |
|:---|:---|:---|:---|:---|
| Row 4 | Security review | Priya | 2026-09-02 | Blocked: approver needed |
| Row 7 | Training sign-off | Mateo | 2026-09-04 | Blocked: owner confirmation needed |

## Starting slide

Create or select a launch-status slide containing:

- A vague heading: “Project Update”
- Seven bullets mixing facts, interpretation, and actions
- Both verified source rows, including references
- A decorative image that does not support the message

## Repair prompt

```text
Revise only the selected slide. Rename it “Two Blockers Need Owners This Week.” Keep the two verified blocker names, owners, dates, and source references unchanged. Remove repetition and unsupported interpretation. Use a two-column layout: verified blocker evidence on the left and requested owner actions on the right. Replace the decorative image with simple editable shapes. Do not add a completion percentage, new deadline, approval claim, or customer-impact claim. Return a preview; do not replace the slide automatically.
```

## Acceptance check

- The title states one conclusion.
- Every retained fact still matches its source.
- Evidence and requested actions are visually distinct.
- Text remains editable and follows a logical reading order.
- No new number, date, status, or approval appears.

## Editable or flattened?

Compare two available routes:

1. **Ask Gemini:** Generate or edit one slide whose elements can be edited.
2. **Insert → Help me visualize → Slide (beta):** Use the separate rendered-image route documented by Google.

Use the editable route when text correction, accessibility, localization, chart maintenance, or collaboration matters.

## Offline fallback

Ask learners which output passes the acceptance check:

- **Output A:** A polished slide image with tiny embedded text and no editable reading order.
- **Output B:** Editable title, text, and shapes; facts unchanged; one unsupported “low risk” badge added.

Neither passes. Output A fails editability and accessibility; Output B introduces an unsupported interpretation.

## Delivery

1. Show the starting slide and ask learners to name its single most important message.
2. Submit the repair prompt in Ask Gemini and inspect the preview before replacement.
3. Compare the revision with the acceptance check and its source files.
4. Explain the editable-slide and slide-image distinction before choosing a route.
5. If generation is unavailable, diagnose Output A and Output B.

> Availability depends on the signed-in plan, account, administrator settings, desktop and language support, and rollout stage.

## Takeaway

Repair one defect at a time, preserve verified evidence explicitly, preview before replacement, and choose editable elements over flattened slide images when the deck must remain maintainable.
