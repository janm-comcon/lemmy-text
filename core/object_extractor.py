# core/object_extractor.py
from typing import Iterable, Optional

from core.domain_lexicon_gold import OBJECTS, PRODUCTS
from core.domain_normalization import NORMALIZE_OBJECT


def extract_object(tokens: Iterable[str]) -> Optional[str]:
    for token in tokens:
        canonical = NORMALIZE_OBJECT.get(token, token)

        if canonical not in OBJECTS:
            continue

        # object must not be product
        if canonical in PRODUCTS:
            continue

        return canonical

    return None
