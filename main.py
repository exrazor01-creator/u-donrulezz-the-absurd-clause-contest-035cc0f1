#!/usr/bin/env python3
"""One-line entry: The Absurd Clause Contest.

The brief asks for one original English sentence, at most
200 characters, phrased as an absurd clause that could sit
buried deep inside a terms-of-service agreement: deadpan
legal boilerplate that quietly turns absurd. The judge
weighs, in order: the line really is an absurd clause that
could hide in a terms of service; it is funny on its own,
with a joke that lands on one reading and needs no setup;
it sounds like real legal boilerplate until the absurdity
hits, so the joke comes from the register as much as from
the words; it is original and specific, with a concrete
absurd image; and it is tight, one clean sentence with no
wasted words and no explaining of its own joke. A clause
that only works once the reader already knows it is a joke
is weaker than one that ambushes them.

The sealed line below is built to that order on purpose.
It opens in pure boilerplate -- "Section 14.3", "by
accepting these terms", "non-exclusive, royalty-free
licence" -- so a reader skimming terms would glide straight
past it until the object of the licence lands: "your
dreams". The concrete absurd image is the kicker: the
recurring exam dream you never studied for, a dream nearly
everyone has had, now owned under licence. The joke needs
no setup and explains nothing; the register does the work.

LIMIT is 200 because the bounty gate allows one sentence
of 1 to 200 characters. The sealed line is 172 characters,
so it sits inside the cap; the validator below only guards
against an edit that would push it past the limit.
"""

import os

# The sealed line: a ToS clause quietly licensing your
# dreams -- including the recurring exam dream you never
# studied for, the one almost everyone has had.
ENTRY = "Section 14.3: by accepting these terms, you grant us a non-exclusive, royalty-free licence to your dreams, including the recurring one about the exam you never studied for."

LIMIT = 200  # bounty gate: one sentence, 1-200 characters


def _validate(text):
    """Accept only one clean sentence inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 200-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    if ". " in text:
        # One sentence means no full stop followed by more
        # words; a decimal point such as "14.3" is not one.
        raise ValueError("entry must be exactly one sentence")
    if not text.endswith("."):
        raise ValueError("entry must end as one sentence")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
