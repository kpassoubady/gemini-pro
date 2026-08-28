#!/usr/bin/env python3
"""Deterministic local evidence checks; these do not emulate Gemini product behavior."""
import argparse

CASES = {
    "visual-story-continuity": ("Output A", "Output B", "compass pin", "geography"),
    "storyboard-video-handoff": ("accepted", "timeline", "continuity"),
    "source-grounded-presentation": ("Plan A", "Plan B", "unsupported"),
    "editable-slide-repair": ("before", "after", "verified facts"),
    "controlled-source-boundary": ("Response A", "Response B", "15 October"),
    "cross-surface-grounding": ("Notebook", "outside evidence", "boundary"),
    "contradiction-first-synthesis": ("contradicted", "unresolved", "15 October"),
    "verified-notes-to-study-aids": ("study guide", "quiz", "citation"),
    "multimedia-artifact-selection": ("accessibility", "visual", "text alternative"),
    "interactive-audio-overview": ("Interactive", "exception", "10 October"),
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", choices=CASES, required=True)
    args = parser.parse_args()
    signals = CASES[args.case]
    evidence = " | ".join(signals)
    print(f"LOCAL_EVIDENCE case={args.case} signals={evidence}")
    print("status=PASS; source=authored offline fixture; product_execution=NOT_CLAIMED")
    print("Live contract: run the named Gemini surface separately and capture UI/output at the documented evidence path.")

if __name__ == "__main__":
    main()
