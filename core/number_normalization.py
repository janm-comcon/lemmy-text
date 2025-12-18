# core/number_normalization.py

NUMBER_WORDS = {
    "nul": 0,
    "en": 1,
    "et": 1,
    "to": 2,
    "tre": 3,
    "fire": 4,
    "fem": 5,
    "seks": 6,
    "syv": 7,
    "otte": 8,
    "ni": 9,
    "ti": 10
}

def normalize_numbers(tokens: list[str]) -> list[str]:
    normalized = []
    for tok in tokens:
        if tok.isdigit():
            normalized.append(tok)
        elif tok in NUMBER_WORDS:
            normalized.append(str(NUMBER_WORDS[tok]))
        else:
            normalized.append(tok)
    return normalized