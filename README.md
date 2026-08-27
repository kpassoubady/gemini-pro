# Gemini Pro

Internal primary repository for the Gemini Pro course. Holds catalog, outlines, slides, diagrams, demos, and research notes.

### Workshop Objective

Students will learn by doing. By the end of this 6-hour session, participants will have built custom AI assistants, analyzed real-world datasets, and automated their daily workflows using specific, tested prompt structures.

---

### **Hour 1: The Connected Workspace & Data Retrieval**

**Concept:** Moving from manual typing to commanding Gemini to fetch and cross-reference live data.

* **Scenario:** You return from a vacation and need to catch up on a project without reading 50 disjointed emails and Google Docs.
* **The Prompt Structure:**
> `@Gmail Find the most recent email thread about [Project Name]. Summarize the current blockers. Then, look at `@Google Docs` for the [Project Spec Document] and tell me if those blockers affect our phase one deliverables.`


* **The Lab Exercise:** *The Inbox Interrogation*
1. Have students open Gemini and type `@Gmail`.
2. Ask them to search for a real, ongoing project or a specific sender.
3. Instruct them to cross-reference that email data with a specific Google Doc or Drive file using the `@Google Drive` extension in the same prompt.
4. **Output:** A concise status report generated entirely from internal data.



---

### **Hour 2: Cognitive Frameworks (Advanced Prompting)**

**Concept:** Stopping generic outputs by forcing the AI into structured, multi-perspective thinking.

* **Scenario:** You need to make a complex, high-stakes decision but have a personal bias and need objective pushback.
* **The Prompt Structure:**
> `Act as a board of three experts: A cynical risk-manager, a visionary optimist, and a pragmatic project manager. Debate the pros and cons of [Insert Decision/Idea]. Output a transcript of your debate, followed by a final consensus table.`


* **The Lab Exercise:** *The Board of Directors*
1. Students pick a real-life dilemma (e.g., adopting a new software tool, changing a team process, or making a large purchase).
2. Run the multi-persona prompt.
3. Use the "Modify" or "G" (Double-check) button to verify any factual claims made by the "experts" during the debate.
4. **Output:** A formatted table outlining risks, rewards, and a finalized recommendation.



---

### **Hour 3: Agentic Workflows & Deep Synthesis**

**Concept:** Using Gemini to process massive amounts of unstructured data and extract exact insights.

* **Scenario:** You are handed a 60-page industry report in PDF format and need to extract only the statistical data to build a presentation.
* **The Prompt Structure:**
> `Attached is a dense report. I do not want a summary. I want you to extract every statistical claim made in this document. Present them in a Markdown table with three columns: The Claim, The Page Number, and The Surrounding Context. Then, critique the methodology used to get those numbers.`


* **The Lab Exercise:** *The Data Miner*
1. Provide students with a large, dense PDF (e.g., an annual corporate report or a scientific study).
2. Have them upload it into the chat and run the extraction prompt.
3. Instruct them to click the "Export to Sheets" button at the bottom of the table to instantly create a usable database.
4. **Output:** A Google Sheet populated with extracted, cited data.



---

### **Hour 4: Multimodal Analysis (Sight & Sound)**

**Concept:** Interacting with video, audio, and complex imagery instead of just text.

* **Scenario:** You need to learn a new UI or understand a 1-hour tutorial video, but you only have 10 minutes.
* **The Prompt Structure:**
> `[Paste YouTube URL]. Do not just summarize this video. Give me the 3 most controversial or counter-intuitive points the speaker makes, complete with exact timestamps. Then, explain why a detractor might disagree with them.`


* **The Lab Exercise:** *The X-Ray Vision Test*
1. Students find a 1-hour+ YouTube lecture or tutorial.
2. Run the timestamp prompt to extract specific arguments.
3. Next, have students take a screenshot of a complex software UI or a messy flowchart.
4. Upload the image and prompt: `Act as a UI/UX expert. Break down the user flow in this image step-by-step and identify two areas of friction.`
5. **Output:** Timestamped video notes and a visual UI critique.



---

### **Hour 5: Persistent Personas (Gems & Canvas)**

**Concept:** Building reusable, custom AI environments so you never start from a blank page.

* **Scenario:** You frequently write outward-facing content (emails, blogs, policies) and need a permanent editor that understands your specific voice and rules.
* **The Prompt Structure (Gem Instructions):**
> `You are the 'Relentless Editor'. When I provide text, do not rewrite it for me. Instead, highlight clichés, point out logical gaps, and ask me piercing questions. Your goal is to coach me to make my arguments stronger, not do the work for me. Always adopt a direct, no-nonsense tone.`


* **The Lab Exercise:** *Building the Coach*
1. Guide students to the "Gems" creation menu.
2. Have them input the Relentless Editor instructions (or build one tailored to their job, like a "Code Reviewer" or "Client Email Polisher").
3. Paste a rough draft of their own writing into the Gem.
4. Move the output into the **Gemini Canvas** UI to highlight, edit, and rewrite specific paragraphs side-by-side with the AI.
5. **Output:** A permanently saved, custom AI assistant and a polished piece of writing.



---

### **Hour 6: Native Workspace In-App Automation**

**Concept:** Taking everything learned and applying it directly inside the Google apps used daily.

* **Scenario:** You need to build a functional project tracker and draft an announcement, but you don't want to leave your documents.
* **The Prompt Structure (In Google Sheets):**
> `Create a project tracking template for a software launch with columns for task, owner, status (include dropdown options for Pending, In Progress, Blocked), and a formula calculating days until the deadline.`


* **The Lab Exercise:** *The Workspace Sorcerer*
1. Students open a blank Google Sheet.
2. Use the "Help Me Organize" AI sidebar to generate the complex tracking template using natural language.
3. Open a blank Google Doc.
4. Use the "Help Me Write" feature to draft an announcement email based on the data in the sheet.
5. **Output:** A functional, formula-driven spreadsheet and a drafted document created entirely via in-app prompts.

## Related Repositories

- [gemini-pro-companion](https://github.com/kpassoubady/gemini-pro-companion) — student hands-on lab companion.
- [gemini-pro-setup](https://github.com/kpassoubady/gemini-pro-setup) — pre-class environment verification.
- [gemini-pro-book](https://github.com/kpassoubady/gemini-pro-book) — internal authoring repository for the book product.
- [gemini-pro-book-companion](https://github.com/kpassoubady/gemini-pro-book-companion) — exercises and code for book purchasers.