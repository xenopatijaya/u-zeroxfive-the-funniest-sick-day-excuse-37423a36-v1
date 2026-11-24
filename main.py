"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one line (93 characters) to /output/entry.txt: a sick-day excuse
someone could actually send to call in sick.

The joke: a sore throat is a real, half-believable reason to stay home —
but here the throat hasn't just gone hoarse, it has "closed for
renovations", as if it were a shop with a shutter down. The punch lands
on the last word: the "reopening date is still pending", so there is no
return time to argue with, just an indefinite closure. No worn fever,
no dog, no dead grandmother — one fresh image, in the voice of a real
text message, and every word doing work.

Python standard library only; no network, no input files.
"""

import os

EXCUSE = "Calling in sick \u2014 my throat's closed for renovations and the reopening date is still pending."


def main() -> None:
    text = EXCUSE.strip()
    assert "\n" not in text, "excuse must be a single line"
    assert 1 <= len(text) <= 200, f"excuse must be 1-200 chars, got {len(text)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    # Verify the file holds exactly the excuse, byte for byte.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        assert f.read() == text, "entry.txt does not match the excuse"
    print(f"{text} ({len(text)} chars)")


if __name__ == "__main__":
    main()
