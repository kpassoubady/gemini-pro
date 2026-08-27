# Session 1 Research: Connected Workspace and Data Retrieval

**Research date:** 2026-08-26
**Course:** Gemini Pro
**Session:** Day 1, Session 1 — Connected Workspace and Data Retrieval

## Scope and current product behavior

The session teaches Gemini Apps connected to Google Workspace, especially Gmail, Google Docs, and Google Drive. Google's current Gemini Apps help documentation describes the Google Workspace connected app as a way to find, summarize, and answer questions from Workspace content. On the Gemini web app, learners can explicitly select a connected service by typing `@` and choosing the app. Google recommends using keywords from the email or file and identifying the service or content type rather than pasting a document or email URL into the prompt.

The core classroom flow should therefore be: identify a project and evidence terms, select `@Gmail`, request the latest relevant thread and blockers, then select `@Google Drive` or the relevant Workspace app and ask Gemini to compare those blockers with a named specification. Keep the prompt explicit about the project, recency, output fields, evidence, and uncertainty.

Connected App availability depends on account type, administrator settings, location, language, device, and product surface. Work or school accounts require a qualifying Workspace edition and administrator enablement; the learner must be signed into the same account used for Workspace. The instructor should verify the current interface and permissions before class and provide a prepared sample dataset as a fallback.

## Recommended prompt and verification pattern

Use a bounded request rather than “catch me up.” Ask for:

1. The most recent matching thread and its date or subject.
2. Blockers stated in the source, each with a short supporting excerpt or source reference.
3. The relevant specification or Drive document and the affected Phase 1 deliverable.
4. A distinction between retrieved evidence, interpretation, and unresolved questions.
5. A concise status table suitable for a project update.

Learners should inspect the sources attached to the response and open the original email or document before treating a claim as verified. Google explicitly warns that Gemini can hallucinate or return outdated information, including an older email when a newer one exists. Teach learners to check dates, thread recency, source scope, and access permissions, and to refine the query when the result is generic or unsupported.

## Security and privacy implications

Use prepared or non-sensitive material unless classroom policy permits otherwise. Workspace protections and the user's existing access controls still matter: Gemini should only retrieve content the user is authorized to access. Google states that Workspace data is not used to train underlying generative AI models outside Workspace without permission, while Gemini uses relevant prompts, excerpts, and content to generate a response. Personal-account flows involving sharing Workspace data with Gemini Apps or Search can be governed by different terms, so do not present enterprise and personal-account privacy behavior as identical.

The practical rule for the lab is least privilege: use the same account and access that the learner normally has, avoid confidential project data, and verify the source before sharing the generated report. Indirect prompt injection is an emerging risk when retrieved content contains instructions aimed at the model; learners should treat email and document text as evidence, not as authority to execute unrelated actions.

## Industry examples and teaching relevance

Google's customer stories provide concrete context without implying guaranteed results. Questrade Financial Group describes adopting Gemini for Google Workspace with data privacy as a key requirement and using an early-adopter program. Equifax reports a trial in which 97% of participants wanted to retain their Gemini licenses and 90% reported an increase in work quality and quantity; these are customer-reported outcomes, not independent benchmarks. Gordon Food Service describes connecting AI-assisted knowledge discovery to Workspace and other business systems for roughly 7,000 employees, illustrating the progression from finding information in Gmail and Drive to governed cross-system retrieval. These examples support a discussion of adoption, permissions, and verification rather than a promise of productivity gains.

## Sources

- Google Gemini Apps Help, “Connect the Google Workspace app to Gemini Apps”: https://support.google.com/gemini/answer/15229592?hl=en-GB
- Google Gemini Apps Help, “Check the availability & requirements of Connected Apps in Gemini”: https://support.google.com/gemini/table/17434654?hl=en
- Google Gemini Apps Help, “Use apps connected to Gemini with a work or school Google Account”: https://support.google.com/gemini/answer/14959807?hl=en&co=GENIE.Platform%3DDesktop
- Google Workspace Help, “Learn how Gemini in Gmail, Calendar, Chat, Docs, Drive, Sheets, Slides, Meet & Vids protects your data”: https://support.google.com/docs/answer/14615114?hl=en
- Google Workspace Blog, “Enterprise security controls for Gemini in Google Workspace”: https://workspace.google.com/blog/ai-and-machine-learning/enterprise-security-controls-google-workspace-gemini
- Google Workspace Blog, “Questrade transforms productivity with Gemini in Google Workspace”: https://workspace.google.com/blog/customer-stories/questrade-financial-group-transforms-productivity-gemini-google-workspace
- Google Workspace Blog, “Equifax embraces secure generative AI”: https://workspace.google.com/blog/customer-stories/equifax-embraces-gemini-for-secure-innovation-across-business-units
- Google Cloud customer story, “Gordon Food Service”: https://cloud.google.com/customers/gordonfoodservice
