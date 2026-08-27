# Demo: Review Before Export to Sheets

## Purpose

Demonstrate that exporting a table to Sheets is a handoff step, not proof that the extraction is correct.

## Prompt

```text
Review the extracted table for duplicate claims, missing page references, inconsistent units, and values whose denominator is unclear. Return a review column with PASS, CHECK, or UNRESOLVED and explain each non-PASS row without changing the original claim.
```

## Delivery

1. Show the candidate extraction table.
2. Ask learners to find one suspicious row before running the review prompt.
3. Run the prompt and compare its flags with the source page.
4. Export only the reviewed table to Google Sheets and check the headers and formats.

## Takeaway

A spreadsheet makes findings reusable; it does not remove the obligation to validate them.
