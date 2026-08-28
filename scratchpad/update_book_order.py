import json

with open('/Users/kangs/code/github/gemini-pro-book/book/builder/book-order.json', 'r') as f:
    data = json.load(f)

# The new chapters array
new_chapters = []

# Insert Front Cover
new_chapters.append({
  "section": "Front Cover",
  "files": [
    "cover/FrontCover.md",
    "cover/FrontCoverPage.png"
  ],
  "note": "PNG file is required for EPUB format cover"
})

# Insert About Author
new_chapters.append({
  "section": "About Author",
  "files": [
    "cover/AboutAuthor.md"
  ]
})

# Add existing chapters
new_chapters.extend(data['chapters'])

# Insert Back Cover
new_chapters.append({
  "section": "Back Cover",
  "files": [
    "cover/BackCover.md"
  ]
})

data['chapters'] = new_chapters

with open('/Users/kangs/code/github/gemini-pro-book/book/builder/book-order.json', 'w') as f:
    json.dump(data, f, indent=2)
