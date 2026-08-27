---
marp: true
theme: default
style: '@import url("https://cdn.jsdelivr.net/gh/kpassoubady/marp-themes@v6/blue-theme.css");'
paginate: true
header: 'Gemini Pro'
footer: 'Day 1 - Session 6: Native Workspace In-App Automation'
---

<style>
.industry-badge {
  border-left: 0.25em solid #e65100;
  background: #fff3e0;
  padding: 0.3em 0.8em;
  font-size: 0.78em;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #e65100;
  margin-bottom: 0.5em;
  display: inline-block;
  border-radius: 0 4px 4px 0;
}
</style>

<!-- _class: lead -->
<!-- _paginate: false -->

# Gemini Pro
## Native Workspace In-App Automation

**Day 1 - Session 6**

<img class="logo" src="https://cdn.jsdelivr.net/gh/kpassoubady/marp-themes@v6/logo-white.svg" />

---

# What We'll Cover

1. Create a tracker in Google Sheets
2. Verify dropdowns and deadline formulas
3. Draft from confirmed facts in Docs
4. Demo: tracker and announcement handoff
5. Lab 1.6: The Workspace Sorcerer

---

<!-- _class: divider -->

# From Prompt to Workspace Artifact
## Build, inspect, and approve the result

<img class="logo" src="https://cdn.jsdelivr.net/gh/kpassoubady/marp-themes@v6/logo-white.svg" />

---

# Start with a Blank Sheet

Describe the project and required fields:

- Task and owner
- Status: Pending, In Progress, Blocked
- Deadline
- Days until deadline formula

Review the generated plan before applying it.

---

# Verify the Tracker

Test known cases:

1. A past deadline
2. Today’s deadline
3. A future deadline

Also check the formula range, date format, dropdown values, and sample data.

---

# Workspace Automation Handoff

<img src="../diagrams/workspace-automation-handoff.svg" alt="Verified Sheets tracker facts flow into a reviewed Docs announcement" style="display:block; margin:0 auto; max-height:420px;" />

---

# Workspace Automation Handoff (Fintech)

<div class="industry-badge">REAL-WORLD SCENARIO</div>

**Fintech (Intuit: QuickBooks Online + Mailchimp):**

- Build a tracker for campaign, owner, approval status, and invoice-data check before a Mailchimp segment is used.
- Draft the Docs announcement from confirmed tracker rows only; the product integration can connect purchase and invoice history to contacts, but it does not approve copy or deadlines.

---

# Workspace Automation Handoff (Retail)

<div class="industry-badge">REAL-WORLD SCENARIO</div>

**Retail (Ocado Retail: product-catalog operations):**

- Create a tracker for category, owner, image/content readiness, status, and deadline before an online grocery assortment update.
- Test past, today, and future dates, then draft a store-operations announcement from confirmed rows; keep the human approval gate.

---

# Draft from Confirmed Facts

In Docs, specify:

- Audience and purpose
- Confirmed milestone and owners
- Current status and next action
- Date and tone
- A clear call to action

Do not invent deadlines or imply approval.

---

# Demo: Build the Tracker

Run `day1/demos/11-sheets-project-tracker.md`.

- Review the generated plan.
- Test status values and deadline cases.
- Inspect formula range and date format.

> Use fictional sample tasks.

---

# Demo: Announcement Handoff

Run `day1/demos/12-docs-announcement-handoff.md`.

- Compare every date and owner with the Sheet.
- Remove unsupported wording.
- Review audience, tone, and call to action.

---

# Lab 1.6: The Workspace Sorcerer

Open `day1/breakout-workspace-sorcerer/` in the companion repo.

**Goal:** Build a formula-driven launch tracker and related announcement.

1. Create and verify the Sheet.
2. Draft from confirmed facts in Docs.
3. Reflect on one workflow to adapt after class.

---

# Human Approval Gate

Before sharing either artifact:

- Test the formula with known dates.
- Confirm dropdown values and ownership.
- Compare announcement facts with the Sheet.
- Remove unsupported milestones.
- Get the appropriate human approval.

---

# Feature Availability

Gemini features require eligible plans and may be controlled by administrators.

If the AI surface is unavailable:

- Use the prepared manual template.
- Preserve the same fields and verification checks.
- Discuss what the AI would have accelerated.

---

# Key Takeaways

1. Natural-language prompts can create useful Workspace structures.
2. Formulas, dropdowns, dates, and ranges must be tested.
3. Docs drafts should use confirmed tracker facts only.
4. Human approval remains the final automation step.

---

<!-- _class: lead -->
<!-- _paginate: false -->

# Questions?

**Course complete: choose one workflow to adapt**

<img class="logo" src="https://cdn.jsdelivr.net/gh/kpassoubady/marp-themes@v6/logo-white.svg" />
