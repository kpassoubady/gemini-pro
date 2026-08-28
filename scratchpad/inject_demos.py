import re
import os

BOOK_DIR = "/Users/kangs/code/github/gemini-pro-book/book"
DEMOS_DIR = "/Users/kangs/code/github/gemini-pro/day1/demos"

mapping = {
    "01-connected-workspace-data-retrieval.md": ["01-connected-retrieval-prompt.md", "02-connected-retrieval-verification.md"],
    "02-cognitive-frameworks.md": ["03-multi-perspective-decision.md", "04-multi-perspective-revision.md"],
    "03-agentic-workflows-deep-synthesis.md": ["05-pdf-statistical-extraction.md", "06-pdf-export-review.md"],
    "04-multimodal-analysis.md": ["07-youtube-timestamp-analysis.md", "08-screenshot-flow-critique.md", "13-visual-story-continuity.md", "14-storyboard-video-handoff.md"],
    "05-persistent-personas.md": ["09-relentless-editor-gem.md", "10-canvas-selective-edit.md"],
    "06-native-workspace-in-app-automation.md": ["11-sheets-project-tracker.md", "12-docs-announcement-handoff.md", "15-source-grounded-presentation.md", "16-editable-slide-repair.md"]
}

def format_demo(demo_path):
    with open(demo_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Convert code blocks under "## Prompt" or other sections to [!PROMPT] admonitions
    # Also handle story bible and other blocks if they are prompts.
    # Actually, the user specifically asked for prompt sections.
    # Let's find ```text inside Prompt sections.
    
    # We will replace all ```text with > [!PROMPT]\n> ... 
    # But wait, not all ```text might be prompts. 
    # Let's look for ```text and replace them.
    parts = content.split("```text\n")
    new_content = parts[0]
    for part in parts[1:]:
        inner_prompt, rest = part.split("\n```\n", 1)
        # Format inner prompt as admonition
        admonition = "> [!PROMPT]\n"
        for line in inner_prompt.strip().split("\n"):
            admonition += f"> {line}\n"
        new_content += admonition + "\n" + rest

    # Change `# Demo: Title` to `### Demo: Title` so it nests correctly under a `## Practical Demos` section.
    new_content = re.sub(r'^# ', '### ', new_content, flags=re.MULTILINE)
    # Demote ## to ####
    new_content = re.sub(r'^## ', '#### ', new_content, flags=re.MULTILINE)
    return new_content

for book_file, demos in mapping.items():
    book_path = os.path.join(BOOK_DIR, book_file)
    with open(book_path, "r", encoding="utf-8") as f:
        book_content = f.read()
    
    # We want to inject right before `## 🧪 Try It Yourself`
    insertion_point = "## 🧪 Try It Yourself"
    
    if insertion_point not in book_content:
        print(f"Warning: {insertion_point} not found in {book_file}")
        continue
        
    demos_text = "## Practical Demos\n\n"
    for demo_file in demos:
        demo_path = os.path.join(DEMOS_DIR, demo_file)
        demos_text += format_demo(demo_path) + "\n\n"
        
    parts = book_content.split(insertion_point, 1)
    new_book_content = parts[0] + demos_text + insertion_point + parts[1]
    
    with open(book_path, "w", encoding="utf-8") as f:
        f.write(new_book_content)
    
    print(f"Processed {book_file}")
