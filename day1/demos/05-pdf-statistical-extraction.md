# Demo: Extract Statistical Claims from a PDF

## Purpose

Show a multi-step document workflow that preserves claims, page references, context, and methodology questions.

## Prompt

Replace the bracketed placeholder with the report you want to analyze.

```text
Do not summarize [REPORT-NAME]. Extract every statistical claim into one row per claim. Return a table with Claim, Page Number, Surrounding Context, Population or Denominator, and Methodology Question. Copy numbers exactly. If a page reference or value is ambiguous, mark it as unresolved instead of guessing.
```

## Delivery

1. Upload a prepared, non-sensitive report.
2. Ask learners to predict which fields will make a claim verifiable.
3. Run the prompt and inspect several rows against the PDF.
4. Identify one chart or footnote that needs human review.

## Takeaway

Structured extraction makes evidence review possible, but the generated table remains a candidate dataset until sampled against the source.
