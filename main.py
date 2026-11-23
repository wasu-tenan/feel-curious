#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR,
or the --output path). Python 3.13, standard library only, deterministic.
"""

import argparse
import os

SETUP = (
    "The postman still leaves one letter a week at the blue house on the hill. "
    "It has stood empty since 1987, its windows boarded, and the letters are "
    "never opened."
)
TWIST = "Last Tuesday, one of them was gone."

# Two fragments joined deliberately with a single space, so the hook
# lands after a full stop: a routine, then the one thing that breaks it.
TEXT = " ".join((SETUP, TWIST))


def resolve_output_path(output_arg):
    if output_arg:
        if output_arg.endswith(".txt") or os.path.isfile(output_arg):
            return output_arg
        return os.path.join(output_arg, "entry.txt")
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Write the curiosity entry text to entry.txt."
    )
    parser.add_argument("--output", default=None,
                        help="Output file or directory (default: "
                             "$MAKEFUN_OUTPUT_DIR/entry.txt, else /output/entry.txt)")
    args = parser.parse_args(argv)
    path = resolve_output_path(args.output)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    # No trailing newline: the file is exactly the text, 1-280 code points.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
