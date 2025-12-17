import sys
from core.pipeline import normalize_text

def main() -> None:
    if not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        text = sys.argv[1]

    print(normalize_text(text))
