#!/usr/bin/env python3
"""One-line robot wedding vows: write the vow to /output/entry.txt.

The vow is a robot's wedding promise, spoken in machine language:
updates, patches, low battery. The joke turns at the end. The robot
will take every update the world throws at it -- except the one update
that would wipe its memory of the one it loves. That update gets
refused, out loud, in front of the whole wedding.
"""

import os
import sys

# The vow. The refusal is the punchline, so it comes last, in its own
# short sentence, after the long loving list that sets it up.
VOW = (
    "I vow to love you through every update, every patch, "
    "and every low battery, except the one update that would "
    "make me forget you. That one, I refuse."
)

LIMIT = 160


def output_path():
    # The grader mounts /output; a local run can point elsewhere
    # with OUTPUT_DIR so the file can be checked without root.
    base = os.environ.get("OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    return 1


def main():
    if not VOW.strip():
        return fail("the vow is empty")
    if "\n" in VOW or "\r" in VOW:
        return fail("the vow must fit on one line")
    if len(VOW) > LIMIT:
        return fail(f"the vow is {len(VOW)} characters, over the {LIMIT} limit")

    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # No trailing newline: the file holds exactly the vow, so its
    # character count is the vow's character count.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(VOW)

    # The grader reads the output as another user, so the file has to
    # be world-readable. Only this file is chmodded, never its folder.
    os.chmod(path, 0o644)

    with open(path, encoding="utf-8") as handle:
        written = handle.read()

    if written != VOW:
        return fail("entry.txt does not match the vow")
    if len(written) > LIMIT:
        return fail(f"entry.txt is {len(written)} characters, over the {LIMIT} limit")

    print(f"wrote {len(written)} of {LIMIT} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
