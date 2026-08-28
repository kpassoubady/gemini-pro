# Session 11 Research: Advanced Presentation Workflows

**Research date:** 2026-08-27
**Course:** Gemini Pro
**Session:** Day 2, Session 11 — Advanced Presentation Workflows

## Scope

This Day 2 session extends Day 1 Session 6 from Sheets and Docs artifacts into presentation creation. It should distinguish two creation surfaces and several output types rather than presenting every capability as interchangeable:

1. **Gemini Canvas:** Create a slide presentation from a prompt or uploaded source, iterate in Canvas, then export to Google Slides or PDF.
2. **Gemini in Google Slides:** Generate a fully editable presentation in a blank deck, generate or edit one fully editable slide, summarize a presentation, rewrite content, and reference approved sources.
3. **Help me visualize:** Generate or edit images and create slide or infographic images. The beta slide-image output is not the same as an editable slide.

Feature availability varies by plan, account type, language, platform, administrator settings, and rollout stage. The full-presentation and single-slide generation help pages currently describe eligible plans, desktop use, and English-only availability. Check the signed-in account before delivery.

## Full editable presentations in Google Slides

Gemini in Google Slides can generate a fully editable presentation containing text and images. The workflow begins from the Slides start screen or an empty presentation. The user describes the topic and goal, adds reference material, optionally provides an existing deck as a style reference, answers clarifying questions, and reviews a generated plan before approving deck generation.

The generated plan exposes three useful control points:

- **Overview:** The intended presentation and audience.
- **Sources:** The files Gemini plans to use.
- **Steps:** The proposed content outline for each slide.

Before approval, the user can edit slide titles or descriptions, add or delete slides, and update the plan. After generation, every element remains editable. The user can refine individual slides, generate additional slides, manually edit elements, and generate or edit images.

## Advanced grounding and style capabilities

For full-deck generation, Gemini can use files from Drive such as Google Docs, Sheets, PDFs, and prior presentations. Depending on source settings, it may also search relevant content from the web, Drive, Chat, or Gmail. Suggested sources are candidates, not automatic evidence; users should inspect the source list and verify claims against the underlying material.

A separate prior deck can be selected with Match presentation style. This uses the deck as a visual reference for the generated presentation. Style matching should not be described as a guarantee of brand compliance. Review theme, fonts, colors, logo treatment, image rights, and template rules before publication.

## Single-slide generation and conversational editing

Gemini can generate one fully editable slide at a time inside an existing presentation. It can start from scratch or reuse the visual style of another presentation. The user previews the result, then inserts it as a new slide or replaces the selected slide.

Gemini can also edit an existing slide through natural-language instructions such as simplifying the slide, reducing text, adding an image, or converting the layout to two columns. Specific Drive files can be added as sources or referenced with `@`; the Sources panel shows files used for the response.

This capability supports a repair workflow: identify one observable defect, request a bounded change, preview the revision, compare it with the original, and only then replace the slide.

## Canvas-to-Slides workflow

Gemini Canvas can create a slide presentation from a prompt and optional uploaded files. It can also transform an existing Canvas document or report into a slideshow. Users can export the result to Google Slides for editing and collaboration or export it as PDF.

Canvas is useful for rapid ideation or transforming a conversation into an initial narrative. Google Slides is the stronger surface when teams need native collaboration, precise element-level editing, approved source settings, style matching, and a reviewable presentation plan.

## Images, slide images, and infographics

Gemini in Slides can generate and edit images, customize style and aspect ratio, remove image backgrounds, and insert an image normally or as a background. Current Google documentation identifies Gemini 3 Pro Image as the image-generation and editing capability in Slides and Vids.

Help me visualize also offers beta generation of a slide image and an infographic image based on presentation context. These outputs are rendered images. They are not equivalent to the fully editable slides created through Generate a slide. This distinction matters for accessibility, text correction, localization, chart updates, and brand review.

For production work, prefer editable text, shapes, and charts when the content must be corrected, translated, read by assistive technology, or maintained. Treat generated visuals as draft assets and verify labels, numbers, spelling, likenesses, logos, and rights.

## Recommended advanced workflow

1. Define the audience, decision or action, duration, slide count, tone, and constraints.
2. Assemble approved source files and one style-reference deck if appropriate.
3. Ask Gemini to create a source-grounded presentation and answer its clarifying questions.
4. Review the source list and presentation plan before approving generation.
5. Inspect the generated narrative for one idea per slide and a clear evidence-to-action sequence.
6. Repair weak slides one at a time with bounded prompts instead of regenerating the whole deck.
7. Verify claims, charts, dates, names, citations, accessibility, speaker intent, brand rules, and permissions.
8. Rehearse the deck and record the human owner who authorizes sharing.

## Prompt design

A strong presentation brief should include:

- Business purpose and audience.
- Decision, action, or learning outcome.
- Number of slides or presentation duration.
- Narrative order and required sections.
- Approved source files and source-use boundaries.
- Desired style and an optional style-reference deck.
- Required evidence, charts, visuals, and calls to action.
- Prohibited claims, sensitive information, and review criteria.

An effective repair prompt names the selected slide, the defect, the required change, what must remain unchanged, and the acceptance check. For example: simplify one slide to one conclusion and three evidence points, retain the cited values, replace decoration with an editable comparison chart, and do not introduce new claims.

## Verification and governance

Generated presentations can contain unsupported claims, incorrect synthesis, misleading charts, fabricated specificity, poor contrast, dense layouts, inaccessible image-based text, and off-brand visuals. A generated deck is a draft, even when it is polished and fully editable.

Review at least these gates:

- **Grounding:** Every material claim maps to an approved source.
- **Data:** Numbers, units, periods, denominators, and chart encodings are correct.
- **Narrative:** The sequence supports the audience’s decision or action.
- **Design:** Hierarchy, contrast, spacing, and visual consistency are usable.
- **Accessibility:** Reading order, text alternatives, color use, and image-based text are reviewed.
- **Governance:** Confidentiality, sharing permissions, rights, brand, and final approval are explicit.

## Recommended classroom demonstrations

Use a fictional internal launch-readiness scenario grounded in a short policy document and a verified project tracker.

- **Demo 03:** Generate a five-slide plan from approved sources, inspect the source list and plan, and reject an attractive but unsupported claim before deck generation.
- **Demo 04:** Repair one overloaded slide with a bounded prompt, compare editable output with a generated slide image, and apply an accessibility and evidence checklist.

Both demos should include offline artifacts because full presentation generation may be unavailable for the instructor’s plan, language, account, administrator configuration, or rollout.

## Sources

- Google Docs Editors Help, “Generate presentations with Gemini in Google Slides”: https://support.google.com/docs/answer/17111393
- Google Docs Editors Help, “Generate a slide with Gemini in Google Slides”: https://support.google.com/docs/answer/16961475
- Google Docs Editors Help, “Collaborate with Gemini in Google Slides”: https://support.google.com/docs/answer/14355071
- Google Docs Editors Help, “Generate & edit images with Gemini in Google Slides & Vids”: https://support.google.com/docs/answer/13951829
- Gemini Apps Help, “Create docs, apps & more with Canvas”: https://support.google.com/gemini/answer/16047321
- Google Docs Editors Help, “Learn about prompts for Gemini in Docs, Sheets, Slides, Vids & Forms”: https://support.google.com/docs/answer/15013615
- Google Workspace Blog, “Create on-brand presentations in minutes with Gemini in Google Slides,” July 22, 2026: https://workspace.google.com/blog/product-announcements/create-on-brand-presentations-in-minutes-with-gemini-in-google-slides
