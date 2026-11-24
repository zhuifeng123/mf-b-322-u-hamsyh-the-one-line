#!/usr/bin/env python3
import os

ENTRY = (
    "You told me to move fast and break things. "
    "You never said which things — production volunteered."
)

assert len(ENTRY) <= 180, len(ENTRY)
assert "\n" not in ENTRY

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
