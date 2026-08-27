# Session 4 Research: Multimodal Analysis

**Research date:** 2026-08-26
**Course:** Gemini Pro
**Session:** Day 1, Session 4 — Multimodal Analysis

## Scope and current product behavior

This session combines video and image analysis in the Gemini web app. Google’s video-understanding documentation describes extracting information from video, answering questions about content, and referring to specific moments with timestamps in `MM:SS` format. Gemini can use both audio and visual streams. Processing details matter: the documentation describes default sampling behavior that can miss rapid motion or quick scene changes, so a timestamp is a model-generated pointer that must be checked against the original video.

The classroom flow should use a public, non-sensitive YouTube lecture or tutorial and ask for three controversial or counter-intuitive points, exact timestamps, and a credible detractor’s response. YouTube URL analysis is subject to product and feature availability; provide a short downloaded sample or transcript fallback if the classroom account cannot use the URL.

For images, Gemini Apps can accept uploaded photos and other supported files. A screenshot or flowchart prompt should name the role, request a step-by-step flow, and ask for two friction points with visual evidence. Learners should distinguish what is visibly present from an interpretation about usability or user intent.

## Prompt and verification pattern

Use a prompt with four parts: media scope, analytical lens, structured output, and verification rule. For video, require timestamp, claim, speaker evidence, and detractor response. For screenshots, require observed element, inferred user action, friction, and confidence. Ask Gemini to say when a detail is unreadable or absent rather than guessing.

Verify each timestamp by opening the original video and checking the surrounding seconds. Verify visual claims by zooming into the screenshot or flowchart and confirming that labels, arrows, and controls are actually present. Fast transitions, small UI text, ambiguous arrows, and missing audio can cause errors.

## Industry relevance

Premji Invest describes using multimodal and multilingual analysis to assess product quality and customer-experience signals from translated text, audio, and video reviews. HeyGen describes using Gemini’s visual intelligence and long-context capabilities in a video agent that analyzes and structures video production tasks. These are useful examples of multimodal systems supporting human decisions and workflows, but their reported outcomes are customer claims and should not be presented as classroom benchmarks.

## Risks and guardrails

A video or screenshot can contain private information, credentials, customer data, or copyrighted material. Use public or prepared media and crop screenshots before upload. Do not infer a person’s sensitive traits from an image. Timestamps can be approximate, and a visual critique can confuse design preference with measurable friction. Require the original media check before learners share notes or recommendations.

## Sources

- Google AI for Developers, “Video understanding”: https://ai.google.dev/gemini-api/docs/video-understanding
- Google Gemini Apps Help, “Upload and analyse files in Gemini Apps”: https://support.google.com/gemini/answer/14903178?hl=en-GB&co=GENIE.Platform%3DDesktop
- Google AI for Developers, “Image understanding”: https://ai.google.dev/gemini-api/docs/image-understanding
- Google Cloud Applied AI Engineering, “Multimodal Prompting with Gemini: Working with Videos”: https://googlecloudplatform.github.io/applied-ai-engineering-samples/genai-on-vertex-ai/gemini/prompting_recipes/multimodal/multimodal_prompting_video/
- Google Cloud customer story, “Premji Invest”: https://cloud.google.com/customers/premjiinvest
- Google Cloud customer story, “HeyGen”: https://cloud.google.com/customers/heygen
