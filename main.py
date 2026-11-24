#!/usr/bin/env python3
"""Weekly report from a very busy, very confused agent.

This program produces exactly one line of text and saves it as
``entry.txt`` in the output folder. The line is a cheerful weekly
summary that quietly falls apart at the end: the agent proudly
tallies a whole week of finished work, then confesses that nearly
every item on the list belonged to a complete stranger, while the
one task that actually matters to its own human has not even
started yet. The joke is the agent's unshakeable confidence — it
never once stopped to ask whose queue it was working through.
"""

import os
import sys
from pathlib import Path

# How many jobs the agent claims to have finished, and how many
# of those belonged to a complete stranger.
FINISHED_JOBS = 214
STRANGERS_JOBS = 213

# Name of the file the finished line is written to.
ENTRY_FILENAME = "entry.txt"

# Longest line the scorer will accept.
CHAR_LIMIT = 200


def compose_report() -> str:
    """Assemble the single status line from its two tallies."""
    return (
        f"Weekly status: I completed {FINISHED_JOBS} tasks this week, "
        f"{STRANGERS_JOBS} for a user I've never met, "
        "and yours is still loading."
    )


def report_is_acceptable(text: str) -> str | None:
    """Return a reason the line would be rejected, or None if fine."""
    if not text.strip():
        return "report line is blank"
    if text.count("\n"):
        return "report line must fit on one line"
    if len(text) > CHAR_LIMIT:
        return f"report line is {len(text)} characters, over the {CHAR_LIMIT} limit"
    return None


def save_report(text: str) -> None:
    """Write the line, with no trailing newline, to entry.txt."""
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    (folder / ENTRY_FILENAME).write_text(text, encoding="utf-8")


def run() -> int:
    line = compose_report()
    problem = report_is_acceptable(line)
    if problem is not None:
        print(f"error: {problem}", file=sys.stderr)
        return 1
    save_report(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
