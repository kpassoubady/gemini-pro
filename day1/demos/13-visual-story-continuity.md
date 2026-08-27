# Demo: Character Continuity Under Pressure

## Purpose

Show why scene-only prompts drift, then use a reusable story bible, an approved reference image, and a continuity ledger to repair the sequence.

## Story bible

```text
Preserve in every frame: Mina is a South Asian field engineer in her early 30s with shoulder-length wavy black hair, round teal glasses, a mustard field jacket, a navy backpack, and a small silver compass pin. Orbit is a palm-sized white spherical inspection drone with one cyan ring light and no text, face, arms, or logos. The world is an optimistic solar-powered railway in a teal-and-gold palette, rendered as a soft gouache illustration with natural proportions in 16:9 landscape. Never change identity, wardrobe, signature props, palette, rendering style, or aspect ratio unless explicitly requested.
```

## Frame 1 prompt

```text
Use the story bible. Frame 1 of 4: wide establishing shot. Mina arrives at a quiet railway platform at dawn. Orbit floats beside her right shoulder. The station lights are dark, and one damaged solar panel is visible beside the platform clock. No other people, logos, or text. Return one 16:9 image.
```

## Deliberately weak Frame 2 prompt

```text
Create a close-up of the engineer while her drone scans a broken solar panel.
```

## Repaired Frame 2 prompt

```text
Use the story bible and approved Frame 1 as visual references. Frame 2 of 4: close-up at platform level. Orbit projects a cyan scan across the same damaged solar panel while Mina studies the result. Preserve Mina's identity, teal glasses, mustard jacket, navy backpack, compass pin, and position relative to Orbit. Preserve Orbit's white sphere, single cyan ring, and lack of face or limbs. Match the railway architecture, teal-and-gold palette, dawn lighting, gouache texture, and 16:9 format. Do not add people, logos, text, tools, or costume details.
```

## Frame 3 prompt

```text
Use the story bible and approved frames as visual references. Frame 3 of 4: medium over-the-shoulder shot. Mina reconnects a glowing teal wire on the damaged solar panel while Orbit hovers closely to illuminate the work area. Preserve Mina's identity, teal glasses, mustard jacket, navy backpack, compass pin, and position relative to the panel. Preserve Orbit's white sphere, single cyan ring, and lack of face or limbs. Match the railway architecture, teal-and-gold palette, dawn lighting, gouache texture, and 16:9 format. Do not add people, logos, text, or extra props.
```

## Frame 4 prompt

```text
Use the story bible and approved frames as visual references. Frame 4 of 4: wide shot, pulling back. The solar panel is repaired and the station lights now glow warmly, casting a golden hue over the platform. Mina and Orbit stand together on the platform looking down the tracks. Preserve Mina's identity, teal glasses, mustard jacket, navy backpack, and compass pin. Preserve Orbit's white sphere and single cyan ring. Match the railway architecture, teal-and-gold palette, early morning lighting, gouache texture, and 16:9 format. Do not add people, logos, text, or change costume details.
```

## Offline fallback

Score these fictional output reports before revealing the diagnosis:

- **Output A:** Mina has rectangular black glasses and a green coat; Orbit has two arms; the image is photorealistic.
- **Output B:** Mina and Orbit match the anchor, but the compass pin is absent and the panel moved to the right of the clock.

Output A fails identity, wardrobe, drone design, palette, and style. Output B is closer but still fails prop and geography continuity.

## Delivery

1. Generate Frame 1 and select one result as the approved anchor.
2. Generate the weak Frame 2 without the anchor; ask learners to name visible drift.
3. Generate the repaired Frame 2 in the original conversation and attach Frame 1 if the surface supports references.
4. Score both Frame 2 outputs for identity, wardrobe, Orbit design, palette, style, geography, and aspect ratio.
5. Generate Frame 3 and Frame 4 sequentially, continuing to use previous approved frames as references to maintain strict continuity.
6. If generation is unavailable, score Output A and Output B with the same ledger.

## Takeaway

A master prompt defines stable truths, reference images reduce ambiguity, and scene deltas describe only what should change.
