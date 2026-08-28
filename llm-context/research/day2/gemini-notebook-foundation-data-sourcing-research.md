# Session 13 Research: Gemini Notebook Foundation and Data Sourcing

**Research date:** 2026-08-27
**Course:** Gemini Pro
**Session:** Day 2, Session 13, Gemini Notebook: Foundation and Data Sourcing

## Product identity and current positioning

Google renamed NotebookLM to Gemini Notebook in August 2026. It remains a standalone, source-grounded research product and now also works across the Gemini app and, where available, Google Search. Course materials should introduce the current name, state “formerly NotebookLM” once for recognition, and avoid teaching NotebookLM and Gemini Notebook as separate products.

Notebooks can be created and edited in both Gemini Apps and the standalone Gemini Notebook experience. Names, sources, and custom instructions sync across the two surfaces. The surfaces do not ground answers identically:

- Standard Gemini Notebook chat grounds answers in the selected notebook sources.
- Tier-dependent agentic chat in Gemini Notebook can add web research, code execution, and generated files when those tools are enabled.
- Gemini Apps can use notebook sources together with web search and other Gemini tools.

This distinction is central to the course. Use source-grounded chat when a learner must make a claim from a controlled source set. When agentic tools or Gemini Apps contribute outside information, require the user to label notebook evidence separately from web evidence, calculations, and generated interpretation.

## Source model

A notebook is a persistent research workspace containing sources, custom instructions, chats, notes, and generated artifacts. The model answers against sources selected for the current question. Selecting and deselecting sources creates a temporary evidence boundary without deleting material from the notebook.

The desktop experience supports a broad range of sources, including Google Docs, Slides, and Sheets; PDF, DOCX, PPTX, CSV, Markdown, text, and ePub files; images and audio; pasted text; web URLs; eligible Google Play Books; public YouTube URLs; and Gemini chats. Mobile source options can be narrower.

Important import behavior includes:

- Google Drive sources auto-update every few minutes and refresh when the notebook opens. Users can also request a manual sync.
- Footnotes and comments from Google files are not imported.
- A Google Drive import uses content the user has permission to access, but exported Docs or Sheets do not inherit notebook sharing permissions.
- Website imports capture supported page text. Paywalls, dynamic pages, blocked crawlers, and non-text elements can produce incomplete sources.
- Public YouTube imports depend on the available transcript and do not provide independent visual verification.
- Audio is transcribed at import, so names, numbers, and specialized terms require review.

## Limits and availability

Do not teach the catalog’s fixed “500 notebooks and 300 sources” statement as a universal limit. Current limits vary by account and access tier. Google’s standard-access documentation lists 100 notebooks and 50 sources per notebook, while higher tiers increase those limits up to 500 notebooks and 600 sources. Gemini Apps also states that source limits depend on the Google AI plan. Daily query and artifact quotas vary as well and are subject to change.

The instructor should show learners where to inspect their current plan and limits rather than place a single capacity number on a slide. Confirm age, region, language, mobile, plan, and administrator restrictions before delivery.

## Enterprise privacy and governance

For qualifying Workspace accounts, Google documents enterprise-grade security and privacy for Gemini Notebook. Uploaded files, chats, and model outputs are not human reviewed or used to improve generative AI models. Administrators can enable or disable the service and assign access tiers. Personal-account behavior and feedback handling differ, so instructors should not generalize Workspace protections to every account.

Use non-sensitive sources in class. Before importing workplace material, verify classification, sharing rights, retention policy, and whether the account is organization-managed. A notebook should have a clear owner and business purpose, especially when collaborators can add sources or generated artifacts.

## Recommended industry scenario

Use a fictional operational policy change for a distributed company. The source pack should contain:

1. A policy PDF with effective dates and exceptions.
2. A Google Doc implementation guide that can be edited and resynced.
3. A short public web article providing outside context.
4. Raw meeting notes containing one ambiguous statement.

Learners create a notebook, classify each source by authority and freshness, inspect the imported content, and select only the policy plus implementation guide for a controlled question. They then compare the standalone Gemini Notebook answer with a Gemini Apps answer that may use web tools. This makes the grounding boundary observable and supports later synthesis, study-aid, and multimedia sessions.

## Recommended demonstrations

- **Demo 05, controlled source boundary:** Add four sources, ask one question with all sources selected, then deselect the web article and meeting notes. Compare the evidence and citations in the two answers.
- **Demo 06, cross-surface grounding:** Open the same synced notebook in Gemini Notebook and Gemini Apps. Ask the same current-events question and identify which claims come only from notebook sources and which use external tools.

Both demos need screenshots or scripted fallback responses because account rollout, source syncing, and connected-app access may differ in class.

## Common failure modes

- Treating a notebook as a folder without checking source authority, freshness, or import completeness.
- Assuming every selected source has equal evidentiary value.
- Confusing a citation with proof that the cited passage supports the claim.
- Expecting comments, footnotes, web interactions, video visuals, or audio names to import perfectly.
- Exporting an artifact and assuming notebook permissions carry over.
- Using Gemini Apps with a notebook and assuming every sentence came exclusively from notebook sources.

## Sources

- Google Blog, “NotebookLM is now Gemini Notebook”: https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/
- Gemini Notebook Help, “Notebooks in Gemini Apps”: https://support.google.com/notebooklm/answer/17003757
- Gemini Apps Help, “Organize your projects with notebooks in Gemini Apps”: https://support.google.com/gemini/answer/16972047
- Gemini Notebook Help, “Create a notebook in Gemini Notebook”: https://support.google.com/notebooklm/answer/16206563
- Gemini Notebook Help, “Add or discover new sources for your notebook”: https://support.google.com/notebooklm/answer/16215270
- Gemini Notebook Help, “Frequently asked questions”: https://support.google.com/notebooklm/answer/16269187
- Gemini Notebook Help, “Use Gemini Notebook with a work or school Google account”: https://support.google.com/notebooklm/answer/16337734
- Google Workspace Admin Help, “Turn Gemini Notebook on or off for users”: https://support.google.com/a/answer/15239506
- Google Workspace Help, “Generative AI in Google Workspace Privacy Hub”: https://support.google.com/a/answer/15706919
