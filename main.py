"""One-line office joke for make.fun's "Make the AI Judge Laugh" bounty.

The program writes exactly one joke about office life, a single line of
under 200 characters, to entry.txt in the grader's output directory and
nothing else. Pure standard library, fully deterministic: no randomness,
no clock, no network, no input files.
"""

import os

# The joke. Setup: a company-wide plea to end reply-all. Turn: the plea
# itself is answered by 214 people replying all to agree with it -- the
# very behaviour it asked to stop, performed in agreement.
JOKE = (
    "I emailed the whole company asking everyone to stop replying all. "
    "214 people replied all to agree."
)


def main() -> int:
    # The sealed gate: entry.txt must be UTF-8 text of 1 to 199
    # characters, not only white space, exactly one line. Fail loudly
    # here rather than hand the grader an invalid file.
    text = JOKE.strip()
    if not text or len(text) > 199 or "\n" in text or "\r" in text:
        raise ValueError(
            "joke must be one non-blank line of 1-199 characters, "
            f"got {len(text)}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(JOKE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
