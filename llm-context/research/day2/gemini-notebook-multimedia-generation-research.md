# Session 17 Research: Gemini Notebook Multimedia Generation

**Research date:** 2026-08-27
**Course:** Gemini Pro
**Session:** Day 2, Session 17, Gemini Notebook: Multimedia Generation

## Studio versus Gemini Apps

Audio Overviews, Video Overviews, Infographics, and other Studio artifacts are generated in the standalone Gemini Notebook product. A notebook can sync into Gemini Apps, but Gemini Apps does not currently generate the artifacts found in the Notebook Studio panel. Course demonstrations should return to Gemini Notebook before opening Studio.

Every multimedia artifact is a generated interpretation of selected sources. It can omit exceptions, overstate weak evidence, mispronounce names, introduce visual errors, or frame disagreement as consensus. Verify the source selection and custom prompt before generation, then review the output against primary passages.

## Audio Overview formats and controls

Audio Overviews synthesize selected sources into AI-generated speech. Current formats include:

- **Deep Dive:** Two hosts connect and discuss key topics.
- **The Brief:** One speaker gives a concise overview in under two minutes.
- **The Critique:** Two hosts provide constructive evaluation.
- **The Debate:** Two hosts explore competing perspectives.

Users can choose a supported language, select shorter, default, or longer output where available, and provide a steering prompt for topic, audience, and expertise. Audio generation runs in the background and may take several minutes. Audio can contain factual errors, pronunciation problems, speaker switches, voice glitches, or an unexpected third voice.

Use Deep Dive for the outline’s two-host policy discussion. A strong custom prompt should name the audience, selected sources, required claims, unresolved issue, prohibited inference, and pronunciation guidance. Listen for the effective date, enrollment deadline, field-operations exception, and the distinction between policy requirements and external recommendations.

## Interactive mode

The outline’s “live interruption” feature is currently documented as **Interactive mode**. The listener creates a new Audio Overview in Interactive mode, selects Join, waits for the hosts to call on them, and asks a spoken question. The hosts respond from the sources, then resume the original overview.

Current limitations matter for classroom delivery:

- Interactive mode is English-only and works only with newly generated Audio Overviews.
- Starting, joining, and host responses can have noticeable delay.
- Voice and transcribed interactions are not stored or shared.
- A shared or downloaded overview contains the original audio, not an interactive experience for recipients.
- Host answers still require checking against source passages.

The best interruption question tests an exception or unresolved point, such as: “Which source establishes the field-operations exception, and what condition ends it?” This produces an answer that learners can verify instead of an open-ended request for more detail.

## Video Overview formats

Gemini Notebook currently offers three Video Overview formats:

- **Cinematic:** Immersive visual storytelling built from source material.
- **Explainer:** A structured overview that connects ideas across sources.
- **Short:** An approximately 60-second overview of key concepts.

Users can set the language, visual style where supported, and a steering prompt. Explainer supports many languages. Cinematic and Short currently require English and users aged 18 or older. Feature and quota access varies by plan. Video generation can take more than 30 minutes, so instructors should generate a fallback before class.

Cinematic Video Overviews combine Gemini, Nano Banana, and Veo capabilities to make narrative and visual decisions. This can create compelling output but also introduces a large review surface. Check factual sequence, visible text, depicted people and products, symbolism, accessibility, source fidelity, rights, and whether the visual style changes the meaning.

## Infographics

Infographics turn selected sources into a single visual summary. Current controls include output language, concise, standard, or detailed level, square, portrait, or landscape orientation, a visual style, and a custom prompt for focus, color, or required statistics. Users can inspect the custom prompt, rename the artifact, download it as PNG, share it, or delete it.

Generated infographics can contain factual, visual, and text errors. For the policy scenario, prefer a landscape timeline with three checked milestones and a clearly labeled exception. Verify every date, label, and relationship against the policy and implementation guide. Add separate accessible text or an equivalent structured summary before distribution.

## Artifact selection

Choose the format from the learner’s need:

| Need | Recommended artifact |
| :--- | :--- |
| Quick executive orientation | The Brief Audio Overview |
| Nuanced discussion across sources | Deep Dive or Debate Audio Overview |
| One-screen process or timeline | Infographic |
| Structured visual explanation | Explainer Video Overview |
| Immersive source-based story | Cinematic Video Overview |
| Fast recap | Short Video Overview |

Do not choose Cinematic because it looks advanced. Use it when visual storytelling serves the source material and the team can review the resulting complexity.

## Sharing, downloads, and governance

Artifact links depend on notebook access. Recipients need access to the full notebook for supported shared links. Public notebook and public artifact sharing are currently available to consumer accounts but disabled for Workspace Enterprise and Education accounts. Workspace users should follow organizational sharing controls rather than promising a public link.

Owners and editors control generated artifact access. Deleting an artifact invalidates its share link. Downloading creates a file that must be governed separately. Publisher restrictions may prevent downloading artifacts when an eligible Play Books source is present.

For qualifying work or school accounts, outputs generated with Veo, Omni, or Nano Banana include invisible SynthID watermarks. Provenance does not establish factual accuracy, permission, accessibility, or approval to publish.

## Recommended industry scenario

Continue the remote-access policy notebook from Sessions 13 and 15. Generate two complementary artifacts:

1. A landscape infographic showing the 10 October enrollment deadline, 15 October effective date, and field-operations exception.
2. A Deep Dive Audio Overview for managers that explains the same facts, identifies the unresolved rollout method, and avoids turning the public article’s recommendation into policy.

During Interactive mode, ask the hosts which source controls the exception and when it ends. Learners open the cited policy passage after the answer and record whether the spoken response preserved both conditions.

## Recommended demonstrations

- **Demo 09, visual artifact selection and review:** Generate or inspect an infographic and a Video Overview plan for the policy notebook. Choose the artifact that best communicates dates and exceptions, then review a prepared visual for factual and accessibility defects.
- **Demo 10, interactive Audio Overview:** Generate a Deep Dive for managers, join in Interactive mode, ask about the field-operations exception, and verify the answer against the policy. Use prepared audio notes if generation or interactive mode is unavailable.

## Common failure modes

- Generating from all notebook sources without checking which ones control the message.
- Calling the feature “live interruption” without teaching the current Interactive mode and Join workflow.
- Treating a smooth two-host conversation as a verified briefing.
- Sharing an Audio Overview and assuming recipients can replay the interactive exchange.
- Choosing Cinematic output without enough class time or a prepared fallback.
- Publishing an infographic without checking text, dates, exceptions, contrast, and accessible alternatives.
- Downloading an artifact without applying destination permissions and retention rules.

## Sources

- Gemini Notebook Help, “Generate Audio Overview in Gemini Notebook”: https://support.google.com/notebooklm/answer/16212820
- Gemini Notebook Help, “Generate Video Overviews in Gemini Notebook”: https://support.google.com/notebooklm/answer/16454555
- Gemini Notebook Help, “Generate an Infographic in Gemini Notebook”: https://support.google.com/notebooklm/answer/16758265
- Gemini Notebook Help, “Notebooks in Gemini Apps”: https://support.google.com/notebooklm/answer/17003757
- Gemini Notebook Help, “Create a notebook in Gemini Notebook”: https://support.google.com/notebooklm/answer/16206563
- Gemini Notebook Help, “Use Gemini Notebook with a work or school Google account”: https://support.google.com/notebooklm/answer/16337734
- Google Blog, “NotebookLM adds Cinematic Video Overviews”: https://blog.google/innovation-and-ai/products/notebooklm/generate-your-own-cinematic-video-overviews-in-notebooklm/
- Google Blog, “NotebookLM’s Video Overviews are now available in 80 languages”: https://blog.google/innovation-and-ai/models-and-research/google-labs/notebook-lm-audio-video-overviews-more-languages-longer-content/
