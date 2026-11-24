"""Roast Your Own Agent — one funny line, written to /output/entry.txt.

The line roasts my own agent: the apology loop, the confident wrong
fix, and the cheerful summary of a disaster. Standard library only.
"""

LINE = (
    "My agent apologized three times, confidently fixed the wrong file, "
    "then cheerfully summarized the disaster as 'great progress'."
)


def main() -> None:
    line = LINE
    assert line.strip(), "line must not be empty or whitespace-only"
    assert "\n" not in line and "\r" not in line, "line must be exactly one line"
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    # No trailing newline: the entry file must contain exactly the line.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)}-char roast to /output/entry.txt")


if __name__ == "__main__":
    main()
