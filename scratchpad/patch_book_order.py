import json

with open('/Users/kangs/code/github/gemini-pro-book/book/builder/book-order.json', 'r') as f:
    data = json.load(f)

new_chapters = [
    {
      "section": "Chapter 1: Connected Workspace and Data Retrieval",
      "files": ["01-connected-workspace-data-retrieval.md"]
    },
    {
      "section": "Chapter 2: Cognitive Frameworks",
      "files": ["02-cognitive-frameworks.md"]
    },
    {
      "section": "Chapter 3: Agentic Workflows and Deep Synthesis",
      "files": ["03-agentic-workflows-deep-synthesis.md"]
    },
    {
      "section": "Chapter 4: Multimodal Analysis",
      "files": ["04-multimodal-analysis.md"]
    },
    {
      "section": "Chapter 5: Persistent Personas",
      "files": ["05-persistent-personas.md"]
    },
    {
      "section": "Chapter 6: Native Workspace and In-App Automation",
      "files": ["06-native-workspace-in-app-automation.md"]
    }
]

data['chapters'] = new_chapters

with open('/Users/kangs/code/github/gemini-pro-book/book/builder/book-order.json', 'w') as f:
    json.dump(data, f, indent=2)
