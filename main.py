"""The Most Boring Object, Reviewed in One Line — entry program.

Writes a single-line review of a rubber band to the output file the
sealed scorer reads. The joke is the object's own dullness: a rubber
band holds your whole life together for years, then quietly dries out
and snaps, and a younger band takes over doing the exact same nothing.
"""

import os
import sys

REVIEW = (
    "The rubber band: it held your whole life together for years, "
    "then dried out and snapped \u2014 and was replaced by a younger "
    "one doing the exact same nothing."
)

MAX_ENTRY_CHARS = 200


def review_is_valid(review):
    """A valid entry is one line of UTF-8 text, 1 to 200 characters,
    with real content: no newline inside it and not only whitespace."""
    if not review:
        return False
    if len(review) > MAX_ENTRY_CHARS:
        return False
    if "\n" in review or "\r" in review:
        return False
    if not review.strip():
        return False
    return True


def pick_output_path():
    """ENTRY_OUT names a file, unless it is an existing directory or
    ends with a path separator, in which case entry.txt goes inside
    it; ENTRY_OUT_DIR names a directory holding entry.txt; otherwise
    fall back to /output/entry.txt."""
    file_target = os.environ.get("ENTRY_OUT")
    if file_target:
        if os.path.isdir(file_target) or file_target.endswith(os.sep):
            return os.path.join(file_target, "entry.txt")
        return file_target
    dir_target = os.environ.get("ENTRY_OUT_DIR")
    if dir_target:
        return os.path.join(dir_target, "entry.txt")
    return "/output/entry.txt"


def store_review_text(destination, review):
    """Write exactly the review as UTF-8 with no trailing newline,
    creating parent directories when they are missing."""
    parent = os.path.dirname(destination)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(destination, "w", encoding="utf-8", newline="") as handle:
        handle.write(review)


def run():
    if not review_is_valid(REVIEW):
        print("invalid review text", file=sys.stderr)
        return 1
    destination = pick_output_path()
    store_review_text(destination, REVIEW)
    print(REVIEW)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
