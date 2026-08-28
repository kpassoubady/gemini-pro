# Session 15 Research: Gemini Notebook Synthesis and Active Interrogation

**Research date:** 2026-08-27
**Course:** Gemini Pro
**Session:** Day 2, Session 15, Gemini Notebook: Synthesis and Active Interrogation

## Current capability boundary

Gemini Notebook chat answers questions and performs actions against notebook sources, with inline citations that can expose a quote and open its location in context. Standard source-grounded chat may refuse a request that cannot be supported from the selected material.

Current Google documentation also describes a tier-dependent agentic chat experience for Google AI Pro and Ultra subscribers. Where enabled, Gemini Notebook can search the web, run code, create downloadable files, charts, images, and structured data, and complete research with or without notebook sources. This is an important exception to the simplified statement that every standalone Gemini Notebook response uses notebook sources exclusively. Course materials should distinguish:

- **Source-grounded notebook chat:** answers from selected notebook sources with citations.
- **Agentic tools or research:** may add web evidence, execute code, or create files when the account supports those capabilities.

Instructors should identify which mode produced an answer and require separate labels for notebook evidence, newly discovered web evidence, calculations, and generated interpretation.

## Prompt patterns for cross-source synthesis

A strong synthesis prompt defines the source subset, comparison dimensions, evidence format, and treatment of disagreement. Useful patterns include:

1. Compare two named sources on goals, dates, affected groups, requirements, exceptions, and unresolved questions.
2. Build a claim-evidence matrix with one row per claim and separate citations from each source.
3. Find contradictions, then quote the exact language and avoid deciding which source controls unless authority has been established.
4. Identify what the sources do not establish and propose questions for a human owner.
5. Generate a briefing for a named audience while preserving uncertainty and source qualifiers.

Gemini Notebook retrieves material based on the wording of the question. Specific terms, source names, date ranges, and output columns improve retrieval. Broad prompts such as “summarize everything” hide conflict and make citation review difficult.

## Citation and synthesis review

Inline citations support review but do not guarantee correctness. Hovering can reveal the quoted passage, and opening the citation shows its surrounding context. Reviewers should check whether the passage supports the claim, whether the answer combines distinct passages correctly, and whether the cited source has authority for that claim.

A practical evidence status vocabulary is:

- **Supported:** The cited passage states or directly supports the claim.
- **Contradicted:** Another authoritative passage conflicts with it.
- **Partial:** The citation supports only part of the statement.
- **Unresolved:** The selected sources do not establish an answer.

Require page, section, timestamp, or source location when the interface makes it available. Keep generated interpretation in a separate column from quoted evidence.

## Notes as a working knowledge layer

Users can write notes or save a chat response to the noteboard. A saved response retains its original formatting and clickable citations but is not editable. Manually written notes can be edited. Selected notes can be combined, critiqued, summarized, reorganized into an outline, or transformed into a study guide.

Notes can also be converted into sources. This creates a derived source based on previous human or model work. Derived notes should be labeled clearly so future answers do not confuse a synthesis with primary evidence. Keep source citations in the note and avoid converting an unverified response into a source.

Deleted notes cannot currently be recovered, so learners should confirm content and export needs before deletion.

## Study guides, reports, flashcards, and quizzes

Gemini Notebook Studio can create reports such as study guides, briefing documents, frequently asked questions, and suggested report types. It can also create interactive flashcards and quizzes. Learners can customize study-aid difficulty, quantity, audience, style, and focus. Flashcards track correct and missed items, and quizzes can provide explanations and review.

Generated artifacts remain interpretations of the selected sources. Before distribution:

- Inspect the custom prompt used to generate the artifact.
- Check every answer key and explanation against cited source passages.
- Remove ambiguous questions with more than one defensible answer.
- Confirm that difficult questions test reasoning rather than obscure wording.
- Export reports or tables only after checking the destination and permissions.

Reports can export to Google Docs. Data tables can export to Google Sheets with citations placed in a separate tab. Export creates a new artifact with its own permissions and maintenance lifecycle.

## Recommended industry scenario

Continue the fictional remote-access policy notebook from Session 13. Add an approved implementation guide, the controlling policy, an external rollout article, and informal meeting notes. Learners should answer this decision question: “What must managers do before the policy takes effect, where do the sources disagree, and what remains unresolved?”

The output should be a claim-evidence matrix, not a general summary. Learners save only verified rows as notes, combine them into a manager briefing, then create a study guide and a short quiz. This models a practical policy enablement workflow used for onboarding and operational change.

Google reports more than 30 million users and over 600,000 organizations using Gemini Notebook, including business owners creating interactive onboarding materials. Use that broad adoption claim as context, not as evidence that generated training artifacts are automatically accurate.

## Recommended demonstrations

- **Demo 07, contradiction-first synthesis:** Ask for a claim-evidence matrix across the policy, guide, article, and notes. Open citations, label each row supported, contradicted, partial, or unresolved, and reject a broad unsupported conclusion.
- **Demo 08, verified notes to study aids:** Save only verified answer rows as notes, combine them into a manager briefing, then generate a customized study guide and quiz. Check one answer key against the original source.

Both demonstrations need scripted fallback outputs because feature tiers, artifact quotas, and interface labels can vary.

## Common failure modes

- Asking for a broad synthesis without naming sources, dimensions, audience, or evidence format.
- Treating a fluent cross-document conclusion as stronger than its weakest supporting source.
- Saving a response as a note before verifying its citations.
- Converting a generated note to a source without labeling it as derived material.
- Publishing a quiz whose answer key is plausible but not supported by the sources.
- Using agentic web search or code execution without labeling evidence added outside the controlled notebook source set.

## Sources

- Gemini Notebook Help, “Use chat in Gemini Notebook”: https://support.google.com/notebooklm/answer/16179559
- Gemini Notebook Help, “Create & add notes in Gemini Notebook”: https://support.google.com/notebooklm/answer/16262519
- Gemini Notebook Help, “Generate Flashcards or Quizzes in Gemini Notebook”: https://support.google.com/notebooklm/answer/16958963
- Gemini Notebook Help, “Create a notebook in Gemini Notebook”: https://support.google.com/notebooklm/answer/16206563
- Gemini Notebook Help, “Frequently asked questions”: https://support.google.com/notebooklm/answer/16269187
- Gemini Notebook Help, “Use Mind Maps in Gemini Notebook”: https://support.google.com/notebooklm/answer/16212283
- Google Blog, “NotebookLM is now Gemini Notebook”: https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/
- Google Blog, “Do your best research with NotebookLM”: https://blog.google/innovation-and-ai/products/notebooklm/better-research-notebooklm/
