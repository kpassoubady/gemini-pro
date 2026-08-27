---
marp: true
theme: default
style: '@import url("https://cdn.jsdelivr.net/gh/kpassoubady/marp-themes@v6/blue-theme.css");'
paginate: true
header: 'Gemini Pro'
footer: 'Day 1 - Optional Session 7: Enterprise Multimedia Workflows'
---

<style>
.industry-badge {
  border-left: 0.25em solid #e65100;
  background: #fff3e0;
  padding: 0.3em 0.8em;
  font-size: 0.78em;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #e65100;
  margin-bottom: 0.5em;
  display: inline-block;
  border-radius: 0 4px 4px 0;
}
</style>

<!-- _class: lead -->
<!-- _paginate: false -->

# Gemini Pro
## Enterprise Multimedia Workflows

**Day 1 - Optional Session 7**

<img class="logo" src="https://cdn.jsdelivr.net/gh/kpassoubady/marp-themes@v6/logo-white.svg" />

---

# What We'll Cover

1. Analyze images, audio, music, and video
2. Generate, edit, and sequence consistent visual stories
3. Create Audio Overviews, voiceovers, and music
4. Produce video with Gemini Apps and Google Vids
5. Govern enterprise media from prompt to publication

---

<!-- _class: divider -->

# One Ecosystem, Several Surfaces
## Choose the product that matches the workflow

<img class="logo" src="https://cdn.jsdelivr.net/gh/kpassoubady/marp-themes@v6/logo-white.svg" />

---

# This Extends Session 4

**Session 4 focused on analysis:**
- Inspect existing videos, screenshots, and flowcharts.
- Verify timestamps and visible evidence.

**This optional session adds creation:**
- Generate images, speech, music, and video.
- Add enterprise approval, provenance, and publishing controls.

---

# Choose the Right Surface

| Surface | Best fit |
|:---|:---|
| **Gemini Apps** | Individual analysis, ideation, and draft assets |
| **Google Vids** | Collaborative workplace video production |
| **Enterprise Agent Platform** | Governed APIs, applications, and scaled pipelines |

A “Pro” model or plan does not make every feature available everywhere.

---

# Capability Map

| Need | Typical surface |
|:---|:---|
| Analyze files and media | Gemini Apps or an enterprise API |
| Generate or edit images | Gemini Apps, Vids, or enterprise models |
| Create narration or an audio briefing | Audio Overviews, Vids, or Gemini Audio |
| Generate music | Gemini Apps, Vids, or Lyria APIs |
| Create video | Gemini Apps, Vids, or Veo and Omni APIs |

---

# The Enterprise Question

Do not start with “Which model should we use?”

Start with:

1. What business artifact is needed?
2. Which approved sources may inform it?
3. Who must review it?
4. Where will it be stored and published?

---

<!-- _class: divider -->

# Analyze Existing Media
## Extract evidence before generating new assets

<img class="logo" src="https://cdn.jsdelivr.net/gh/kpassoubady/marp-themes@v6/logo-white.svg" />

---

# Supported Analysis Patterns

Gemini Apps can work with supported documents, spreadsheets, notebooks, photos, audio, and video.

Use it to:
- Describe and compare media.
- Transcribe, summarize, or extract claims.
- Identify moments with approximate timestamps.
- Turn observations into a structured review queue.

---

# Images and Screenshots

Ask Gemini to separate:

- **Observation:** Visible text, objects, controls, colors, or layout.
- **Interpretation:** Meaning, intent, usability, quality, or risk.
- **Unknown:** Cropped, blurred, occluded, or unreadable content.
- **Action:** A review step tied to visible evidence.

Never infer sensitive traits from an image.

---

# Audio and Music Analysis

Possible tasks include:

- Transcription and translation
- Speaker separation and segment summaries
- Timestamped questions about a recording
- Detection of speech tone or non-speech sounds
- Structural discussion of music

Treat identity, emotion, lyrics, and quotations as claims to verify.

---

# Video Analysis

Request a review table with:

1. Approximate timestamp
2. Visible or audible evidence
3. Interpretation
4. Confidence
5. Human verification result

Fast motion, small text, cuts, and overlapping audio can be missed.

---

# A Reusable Analysis Prompt

```text
Analyze this [media] for [business purpose].
Separate direct observations from interpretations.
For each finding, cite a timestamp or visible region,
state confidence, and mark anything unreadable or uncertain.
Do not infer identity, intent, or sensitive attributes.
Return a review table for a human approver.
```

---

<!-- _class: divider -->

# Create and Edit Images
## Move from a vague request to a reviewable visual brief

<img class="logo" src="https://cdn.jsdelivr.net/gh/kpassoubady/marp-themes@v6/logo-white.svg" />

---

# Image Capabilities

Current Gemini surfaces can support:

- Text-to-image generation
- Conversational image editing
- Background, object, and composition changes
- Variants for format, audience, or channel
- Product mockups, diagrams, and storyboards

Availability and model labels depend on account and surface.

---

# Build an Image Brief

Specify:

1. Business purpose and audience
2. Subject, setting, and composition
3. Style, lighting, and aspect ratio
4. Required text and brand constraints
5. Elements to exclude
6. Acceptance and review criteria

---

# Image Review Gate

Before external use, verify:

- Product and factual accuracy
- Spelling and rendered text
- Trademarks, logos, and likeness rights
- Representation and accessibility
- Brand and legal approval
- Provenance and disclosure requirements

---

# Visual Asset Workflow (Retail)

<div class="industry-badge">REAL-WORLD SCENARIO</div>

**Retail product launch:**

- Generate background concepts around an approved product image.
- Reject any output that changes the product, packaging, or label.
- Test crops for web, mobile, and social placements.
- Route selected variants to brand, accessibility, and legal review.

---

<!-- _class: divider -->

# Advanced Visual Storytelling
## Keep characters, worlds, and themes stable across many assets

<img class="logo" src="https://cdn.jsdelivr.net/gh/kpassoubady/marp-themes@v6/logo-white.svg" />

---

# Why One Prompt per Image Drifts

Each isolated generation can reinterpret:

- The character's face, age, clothing, or proportions
- A product's shape, color, label, or scale
- The location, palette, lighting, or art direction
- Recurring props and their positions

Treat a sequence as one production system, not several unrelated prompts.

---

# Start with a Story Bible

| Lock across every asset | Change scene by scene |
|:---|:---|
| Character and product identity | Action and expression |
| Wardrobe and signature props | Shot size and camera angle |
| World rules and color palette | Location within the world |
| Rendering style and aspect ratio | Time, weather, and motion |

Approve the locked column before generating the sequence.

---

# Master Prompt: Mina and Orbit

```text
Visual story bible — preserve in every frame:
Mina: South Asian field engineer, early 30s; shoulder-length
wavy black hair; round teal glasses; mustard field jacket;
navy backpack; small silver compass pin.
Orbit: palm-sized white spherical inspection drone with one
cyan ring light; no text, face, arms, or logos.
World: optimistic solar-powered railway; teal-and-gold palette;
soft gouache illustration; natural proportions; 16:9 landscape.
Never change identity, wardrobe, signature props, palette,
rendering style, or aspect ratio unless the scene delta says so.
```

---

# One Story, Four Clear Frames

| Frame | Scene delta | Story beat |
|:---|:---|:---|
| 1 | Wide shot; Mina arrives at a dark station | A problem appears |
| 2 | Close-up; Orbit scans a broken solar panel | The clue is found |
| 3 | Medium shot; Mina reconnects one cable | The repair works |
| 4 | Wide sunset; station lights glow behind them | The world changes |

The story bible stays fixed; only the scene delta changes.

---

# Build an Anchor Pack First

1. Generate one neutral full-body character reference.
2. Generate front, side, and three-quarter views.
3. Add expression, wardrobe, product, and prop references.
4. Approve one style frame for palette, texture, and lighting.
5. Reuse approved images as references where the surface allows.

A verbal description helps; references reduce ambiguity but cannot guarantee continuity.

---

# Prompt Each Shot as a Delta

```text
Use the approved story bible and reference images.
Frame 2 of 4 — clue:
Close-up at platform level. Orbit projects a cyan scan across
one cracked solar panel while Mina studies the result.
Continuity: same identity, wardrobe, compass pin, drone design,
station architecture, teal-and-gold palette, and gouache style.
Do not add people, logos, text, tools, or new costume details.
Return one 16:9 image with clear space at lower right for captions.
```

Describe what changes; repeat what must not change.

---

# Use a Continuity Ledger

| Check | Frame 1 truth | Reject when |
|:---|:---|:---|
| Mina | Teal glasses, mustard jacket, compass pin | Any item changes or disappears |
| Orbit | White sphere, one cyan ring, no face | Limbs, text, or a face appears |
| World | Teal-gold gouache railway | Palette or medium shifts |
| Geography | Panel sits left of platform clock | Spatial relationship flips |

Record accepted truths early so reviewers compare evidence, not memory.

---

<!-- _class: demo -->

# Demo: Character Continuity Under Pressure

Run `day1/demos/13-visual-story-continuity.md`.

- Baseline: Generate a second frame from a scene-only prompt.
- Drift: Name the identity, wardrobe, prop, or style changes.
- Repair: Recreate it with the master prompt and approved reference.
- Evidence: Score both outputs with the same continuity ledger.

> Live generation is optional; the demo includes an offline continuity review.

---

<!-- _class: divider -->

# From Story Frames to Motion
## Animate approved keyframes instead of rediscovering the story

<img class="logo" src="https://cdn.jsdelivr.net/gh/kpassoubady/marp-themes@v6/logo-white.svg" />

---

# Move from Still Image to Video

1. Approve the story bible and storyboard.
2. Generate and review a keyframe for each shot.
3. Animate the approved keyframe where image-to-video is available.
4. Describe motion, camera behavior, duration, and sound.
5. Assemble clips, narration, music, and captions in Google Vids.

Do not ask one long prompt to solve identity, story, motion, and editing at once.

---

# Video Prompt: Describe Motion

```text
Animate approved Frame 2 for five seconds.
Mina remains still and studies the panel. Orbit glides 20 cm
left to right while its cyan ring pulses twice. The scan follows
that path across the panel. Slow camera push-in; no cut or zoom.
Preserve faces, hands, clothing, props, station geometry, palette,
and gouache texture. No dialogue, text, logo, or new object.
End with Orbit stationary so Frame 3 can begin from that pose.
```

The keyframe defines appearance; the video prompt defines change over time.

---

# Design the Shot Handoff

| Outgoing shot | Incoming shot | Continuity handle |
|:---|:---|:---|
| Orbit stops beside the panel | Mina reaches toward that panel | Match object position |
| Mina looks screen-right | Cable appears screen-right | Match eyeline |
| Cyan ring pulses twice | Station lights activate | Repeat color cue |
| Camera ends close | Next shot starts medium | Preserve geography |

Plan the final moment of one clip as the first constraint of the next.

---

# Keep Sound Continuous Too

Lock a small audio bible:

- Narrator voice, pace, pronunciation, and loudness
- Character names and approved terminology
- Music motif, instrumentation, and transition points
- Ambient sound and intentional silence
- Caption wording and timing

Review the assembled timeline; polished clips can still create a confusing story.

---

<!-- _class: demo -->

# Demo: Storyboard-to-Video Handoff

Run `day1/demos/14-storyboard-video-handoff.md`.

- Inputs: Use two approved adjacent keyframes.
- Motion: Animate only the action between the frames.
- Handoff: Match prop position, eyeline, lighting, and end pose.
- Assembly: Add reviewed narration and captions in Google Vids.

> If video generation is unavailable, compare the prepared shot plan.

---

<!-- _class: divider -->

# Audio, Speech, and Music
## Distinguish knowledge synthesis from creative production

<img class="logo" src="https://cdn.jsdelivr.net/gh/kpassoubady/marp-themes@v6/logo-white.svg" />

---

# Three Different Audio Jobs

| Job | Enterprise option |
|:---|:---|
| Understand a recording | Gemini media analysis |
| Turn sources into a briefing | Audio Overview |
| Narrate approved copy | Google Vids voiceover or speech API |
| Hold a live voice interaction | Gemini Live API |

Choose based on evidence, latency, control, and publishing needs.

---

# Audio Overviews

Audio Overviews create podcast-style conversations from supported sources such as documents, slides, notebooks, and research reports.

They are useful for:
- Executive pre-reads and learning reinforcement
- Alternate consumption of approved content
- Discovering questions before a live briefing

They are synthesized explanations, not recordings of the source.

---

# Generate Music with Lyria

Eligible Gemini Apps and Google Vids accounts can create music with Lyria.

A prompt may use text, images, or video as creative context and specify:
- Genre, instrumentation, tempo, and mood
- Duration, structure, vocals, or instrumental mode
- Business purpose and prohibited elements

Full-track and usage access depends on the selected model and plan.

---

# A Reusable Music Brief

```text
Create a [duration] [instrumental/vocal] track for [purpose].
Mood: [three adjectives]. Tempo: [range].
Instrumentation: [approved palette]. Structure: [sections].
Leave room for narration and end with [transition].
Do not imitate a named artist or reuse protected lyrics.
```

Review lyrics, pronunciation, cultural context, rights, and brand fit.

---

# Audio Workflow (Learning and Development)

<div class="industry-badge">REAL-WORLD SCENARIO</div>

**Internal policy rollout:**

- Create an Audio Overview from the approved policy and FAQ.
- Produce a short Vids explainer with reviewed voiceover copy.
- Add generated music only when it improves comprehension.
- Publish the policy itself as the authoritative source.

---

<!-- _class: divider -->

# Generate and Produce Video
## Match quick ideation, collaboration, or API scale

<img class="logo" src="https://cdn.jsdelivr.net/gh/kpassoubady/marp-themes@v6/logo-white.svg" />

---

# Three Routes to Video

- **Gemini Apps:** Generate or refine short media from a conversation.
- **Google Vids:** Plan, assemble, edit, collaborate, and share at work.
- **Enterprise Agent Platform:** Build repeatable workflows with Veo, Omni, and APIs.

A generated clip is a production ingredient, not a completed campaign.

---

# What Google Vids Adds

A Vids workflow can combine:

- A prompt and approved Drive sources
- A suggested outline and scenes
- Stock, uploaded, or generated media
- Scripts, AI voiceovers, music, and avatars
- Collaborative editing and sharing

The team still owns the final narrative and approval.

---

# Build a Video Brief

Specify:

1. Audience, goal, duration, and aspect ratio
2. Subject, setting, action, and continuity
3. Shot, camera movement, lighting, and pacing
4. Dialogue, narration, music, and sound
5. Brand, safety, factual, and rights constraints
6. Required captions and final approvers

---

# Video Workflow (Change Management)

<div class="industry-badge">REAL-WORLD SCENARIO</div>

**Internal system launch:**

- Ground the storyboard in approved launch documents.
- Generate only the scenes that stock or recorded media cannot provide.
- Review UI depictions, dates, claims, narration, and captions.
- Require the system owner and communications lead to approve release.

---

<!-- _class: divider -->

# Enterprise Governance
## Keep control across input, generation, review, and publication

<img class="logo" src="https://cdn.jsdelivr.net/gh/kpassoubady/marp-themes@v6/logo-white.svg" />

---

# Know the Workspace Trust Boundary

For qualifying Workspace editions, Google states that:

- Interactions stay within the organization.
- Existing Workspace protections apply.
- Content is not human reviewed or used to train generative AI models outside the domain without permission.

Do not extend these assurances to personal accounts or unapproved tools.

---

# Administrators Control Access

Admins can manage access to:

- The Gemini app
- Connected Workspace services
- Gemini features inside Workspace apps
- Google Vids and its generative features
- Organizational units, groups, and eligible licenses

Validate the classroom account before promising a feature.

---

# Provenance Helps, but Is Not Approval

Google uses technologies such as SynthID and Content Credentials across supported generated media.

They can help establish origin or editing history, but they do not prove:
- Factual accuracy
- Ownership of every input
- Brand suitability
- Legal permission to publish

---

# Production Approval Workflow

1. Approve the purpose and source assets.
2. Minimize sensitive input data.
3. Generate from a documented brief.
4. Review facts, quality, accessibility, safety, and rights.
5. Check provenance and disclosure.
6. Record the owner who authorizes publication.

---

# Applied Activity: Choose a Surface

Your team needs an internal two-minute launch explainer grounded in an approved policy and slide deck.

Choose one:

A. Generate everything in a personal Gemini account
B. Build and review it collaboratively in Google Vids
C. Create a custom media-generation API before testing the message

Commit to an answer and name one required approval.

---

# Applied Activity: Recommended Answer

**Choose B: Google Vids.**

- It fits collaborative workplace production.
- Approved Workspace sources can inform the storyboard.
- Scripts, voiceovers, visuals, and music remain editable.
- Review and sharing stay in the team workflow.

Use an API only when repetition, integration, or scale justifies it.

---

# Feature Availability Changes

Before delivery or deployment, verify:

- Workspace edition and assigned access
- Admin settings and connected services
- Country, language, age, and rollout restrictions
- Current generation limits and model status
- Retention, sharing, and publishing policy

**Capability check:** 27 August 2026

---

# Official References (1/2)

- [Work and school account capabilities](https://support.google.com/gemini/answer/14620100?co=DASHER._Family%3DBusiness-Enterprise&hl=en)
- [Upload and analyze files](https://support.google.com/gemini/answer/14903178?hl=en&co=GENIE.Platform%3DDesktop)
- [Generate and edit images](https://support.google.com/gemini/answer/14286560)
- [Generate videos](https://support.google.com/gemini/answer/16126339?co=GENIE.Platform%3DDesktop&hl=en)
- [Generate music](https://support.google.com/gemini/answer/16901237)

---

# Official References (2/2)

- [Generate Audio Overviews](https://support.google.com/gemini/answer/16047373)
- [Gemini features in Google Vids](https://support.google.com/docs/answer/15609411?hl=en)
- [Workspace privacy hub](https://support.google.com/a/answer/15706919)
- [Google Cloud generative media](https://cloud.google.com/ai/generative-media)
- [Lyria enterprise documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/overview)

---

# Key Takeaways

1. Gemini can analyze and generate across images, audio, music, and video.
2. Gemini Apps, Google Vids, and enterprise APIs serve different operating needs.
3. A detailed creative brief makes generated media easier to evaluate.
4. Enterprise controls reduce risk but do not replace human approval.
5. Verify current licenses, limits, provenance, rights, and facts before publishing.

---

<!-- _class: lead -->
<!-- _paginate: false -->

# Questions?

**Optional extension complete: choose one governed media workflow to pilot**

<img class="logo" src="https://cdn.jsdelivr.net/gh/kpassoubady/marp-themes@v6/logo-white.svg" />
