#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters entry.

Writes one original funny Wi-Fi network name to /output/entry.txt
(1-32 characters, UTF-8, not only whitespace). Standard library
only, no network, no input.

The name: "Ex moved out, kept the router" (29 characters). The
story it implies: a breakup, a move-out, and the ex walking off
with the router — the network you are staring at in your phone's
list is named after the very router that was taken. Situation: a
breakup move-out. Character: the ex. Something that happened: the
ex kept the router. ``assemble`` joins the two fragments into the
single name; ``validate`` checks the entry gate before anything
is written.
"""

from pathlib import Path

SETUP = "Ex moved out,"
PUNCH = "kept the router"

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one Wi-Fi name."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Enforce the entry gate: 1-32 chars, UTF-8, not only whitespace."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if not 1 <= len(line) <= 32:
        raise ValueError(f"line must be 1-32 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
