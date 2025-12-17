# core/lemmatizer.py
from typing import List
import re

from lemmy.lemmatizer import Lemmatizer

_lemmatizer = Lemmatizer()

# simple, deterministic tokenizer (sufficient for your use-case)
_TOKEN_RE = re.compile(r"\b\w+\b", re.UNICODE)


def lemmatize_text(text: str) -> List[str]:
    """
    Lemmatize Danish text using Lemmy.

    - Input: raw text
    - Output: list of lemmas (lowercase)
    """
    if not text:
        return []

    text = text.lower()
    tokens = _TOKEN_RE.findall(text)

    lemmas: List[str] = []

    for token in tokens:
        try:
            candidates = _lemmatizer.lemmatize(token)
        except Exception:
            # if Lemmy fails, fall back to token itself
            lemmas.append(token)
            continue

        if not candidates:
            lemmas.append(token)
            continue

        # Lemmy may return:
        # - strings
        # - tuples
        # - objects with .lemma
        first = candidates[0]

        if isinstance(first, str):
            lemmas.append(first)
        elif isinstance(first, tuple):
            lemmas.append(first[0])
        elif hasattr(first, "lemma"):
            lemmas.append(first.lemma)
        else:
            lemmas.append(str(first))

    return lemmas
