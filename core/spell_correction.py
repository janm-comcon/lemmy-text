# core/spell_correction.py
"""
Domain-aware spell correction.

Corrections are ONLY applied if:
- The corrected form exists in gold lexicons or normalization maps
- Edit distance is small
"""

from difflib import get_close_matches

from core.domain_lexicon_gold import ACTIONS, OBJECTS, LOCATIONS, PRODUCTS
from core.domain_normalization import (
    NORMALIZE_ACTION,
    NORMALIZE_OBJECT,
    NORMALIZE_LOCATION,
    NORMALIZE_PRODUCT,
)

# Build allowed vocabulary (authoritative)
VOCABULARY = set().union(
    ACTIONS,
    OBJECTS,
    LOCATIONS,
    PRODUCTS,
    NORMALIZE_ACTION.keys(),
    NORMALIZE_OBJECT.keys(),
    NORMALIZE_LOCATION.keys(),
    NORMALIZE_PRODUCT.keys(),
)

def correct_token(token: str) -> str:
    """
    Correct token if a very close match exists in domain vocabulary.
    """
    if token in VOCABULARY:
        return token

    matches = get_close_matches(token, VOCABULARY, n=1, cutoff=0.88)
    return matches[0] if matches else token


def correct_text(text: str) -> str:
    """
    Apply conservative spell correction token-wise.
    """
    tokens = text.lower().split()
    corrected = [correct_token(tok) for tok in tokens]
    return " ".join(corrected)
