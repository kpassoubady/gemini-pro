# Session 3 Research: Agentic Workflows and Deep Synthesis

**Research date:** 2026-08-26
**Course:** Gemini Pro
**Session:** Day 1, Session 3 — Agentic Workflows and Deep Synthesis

## Scope and current product behavior

This session defines an agentic workflow as a multi-step task in which Gemini reads a source, extracts evidence, structures findings, and critiques or verifies the result. For the learner-facing activity, the Gemini web app can accept uploaded documents and answer questions, summaries, and insight requests. Users can upload files from their device or add files from Drive; Google’s help documentation says up to 10 files may be added in one prompt, subject to availability and account limits. Large files can still produce missed connections, so the instructor should provide a focused report rather than assume that a larger context guarantees completeness.

Gemini’s document-understanding documentation says PDF processing can use both visual and textual information, including tables, charts, and diagrams. The API documentation is not the classroom interface, but it reinforces a useful principle: structured extraction should specify the target fields and large or reusable files should be handled deliberately. The lab should use a dense, non-sensitive report and ask for page numbers and surrounding context for every statistical claim.

## Recommended extraction pattern

Tell Gemini what not to do as well as what to do: “Do not summarize.” Request one row per statistical claim with claim text, page number, surrounding context, and methodology critique. Ask it to mark ambiguous, missing, or conflicting values and to avoid inventing a page reference. Treat the output as a candidate dataset. Open a sample of pages, check that the claim is copied accurately, and inspect whether percentages, denominators, dates, and population definitions were preserved.

Export to Sheets is a convenient handoff when the response produces a table, but it is not a validation step. Before using the sheet, check headers, row completeness, numeric formats, duplicate claims, page references, and whether the extracted values remain tied to the original report.

## Current agentic trend

Google’s 2026 Deep Research documentation describes a preview agent that plans, searches, reads, and synthesizes multi-step research tasks, with collaborative planning and cited reports. The session should mention this as a current industry direction, not present it as the same feature as the basic PDF upload lab. The transferable lesson is to make intermediate operations and evidence visible rather than accepting an opaque final summary.

## Industry relevance

Gordon Food Service describes using Gemini-connected tools to make institutional knowledge more accessible for approximately 7,000 employees and to support decision-making and content creation. A PDF extraction workflow is a smaller, classroom-safe version of the same pattern: turn unstructured operational knowledge into a reviewable table. Workspace Studio examples also show document extraction followed by a Sheets handoff for invoice fields, illustrating how structured extraction can become an operational record. These examples should be framed as reported use cases, not universal performance claims.

## Risks and teaching guardrails

Extraction can omit claims, confuse a chart label with a statistic, misread a scanned page, or produce a plausible but incorrect citation. Methodology critique is itself a generated assessment and must not be treated as peer review. Avoid confidential reports, financial advice, medical conclusions, and personally identifiable information. Require a human sampling pass before the sheet is used in a presentation or decision.

## Sources

- Google Gemini Apps Help, “Upload and analyse files in Gemini Apps”: https://support.google.com/gemini/answer/14903178?hl=en-GB&co=GENIE.Platform%3DDesktop
- Google AI for Developers, “Document understanding”: https://ai.google.dev/gemini-api/docs/interactions/document-processing
- Google Docs Editors Help, “Build or edit entire spreadsheets with Gemini in Sheets”: https://support.google.com/docs/answer/16959434
- Google AI for Developers, “Gemini Deep Research Agent”: https://ai.google.dev/gemini-api/docs/deep-research
- Google Gemini, “Gemini Deep Research”: https://gemini.google/ag/overview/deep-research/?hl=en
- Google Cloud customer story, “Gordon Food Service”: https://cloud.google.com/customers/gordonfoodservice
- Google Workspace Studio example, “Extract PDF Data to Sheets Automatically”: https://www.youtube.com/watch?v=ZQ24QTudlhw
