import os

ROAST = "My agent turns every loss into a report, every report into a plan, and every plan into another loss."


def validate(text):
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    validated = validate(ROAST)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(validated + "\n")


if __name__ == "__main__":
    main()
