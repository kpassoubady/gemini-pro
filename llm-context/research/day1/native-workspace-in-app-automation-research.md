# Session 6 Research: Native Workspace In-App Automation

**Research date:** 2026-08-26
**Course:** Gemini Pro
**Session:** Day 1, Session 6 — Native Workspace In-App Automation

## Scope and current product behavior

The session connects prompt design to work performed inside Google Sheets and Google Docs. Google’s current Sheets documentation describes Gemini-assisted table creation, formula generation, dropdown creation, formatting, and other natural-language actions. “Help me organize” is designed for creating a new table or template, while the Sheets side panel can support broader actions on eligible accounts. Google cautions that feature availability depends on the Workspace or Google AI plan and that native Google Sheets files work best.

The instructor should demonstrate a blank-sheet project tracker with task, owner, deadline, and status columns. Use dropdown values Pending, In Progress, and Blocked. Ask Gemini to propose a deadline calculation, then inspect the formula and test it with known dates. Preview and apply changes deliberately; do not treat generated formulas or formatting as correct without checking them.

In Google Docs, Help me write can create or refine content from a prompt and can reference relevant files. The generated announcement should be based on the project tracker, but the instructor should copy only confirmed project facts and review audience, call to action, tone, and dates before inserting or sharing.

## Recommended workflow

Use a single operational thread: define the launch tracker, inspect its structure, verify dropdowns and formulas, then draft an announcement from confirmed tracker data. Require learners to test at least one status value and one deadline calculation. Keep a small expected-value table so they can spot a wrong formula or date convention.

The natural-language interface lowers menu friction, but it can also hide implementation details. Teach learners to inspect the generated plan, formula, ranges, and applied changes. Google’s Sheets updates describe previewing edits and applying or undoing them; preserve the ability to undo and maintain a clean copy when experimenting.

## Industry relevance

MAS describes using Docs, Sheets, and Slides as shared files for global production timelines and collaboration. GCash reports using Workspace, AppSheet, and Looker Studio to automate internal projects and shorten research cycles, with Gemini supporting reports and decision-making. These examples show why a tracker plus announcement is a useful small-scale workflow, but customer-reported adoption and efficiency numbers are not guarantees for learners.

## Risks and guardrails

A generated tracker can use the wrong range, status values, date logic, or assumptions about ownership. A generated announcement can state an unapproved milestone or expose internal information. Use fictional or prepared launch data, verify formulas with known cases, review the document against the Sheet, and keep a human approval step before communication. Account, admin, plan, and interface differences require a prepared manual fallback.

## Sources

- Google Docs Editors Help, “Organize with Gemini in Google Sheets”: https://support.google.com/docs/answer/13951830
- Google Docs Editors Help, “Collaborate with Gemini in Google Sheets”: https://support.google.com/docs/answer/14356410
- Google Docs Editors Help, “Build or edit entire spreadsheets with Gemini in Sheets”: https://support.google.com/docs/answer/16959434
- Google Workspace Updates, “Use Gemini in Google Sheets to quickly add dropdowns, pivot tables, filters, and more”: https://workspaceupdates.googleblog.com/2025/05/use-gemini-google-sheets-advanced-actions.html
- Google Docs Editors Help, “Write & edit with Gemini in Docs”: https://support.google.com/docs/answer/13447609
- Google Workspace customer story, “How MAS gets more out of its creative workflows with Gemini”: https://workspace.google.com/blog/customer-stories/mas-gets-more-out-its-creative-workflows-using-gemini
- Google Workspace customer story, “How the GCash finance super app is building a new way to deliver value”: https://workspace.google.com/customers/success-stories/gcash/
