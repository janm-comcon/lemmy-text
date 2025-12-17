# core/location_extractor.py
from typing import Iterable, Optional

from core.domain_lexicon_gold import LOCATIONS, OBJECTS, PRODUCTS
from core.domain_normalization import NORMALIZE_LOCATION


def extract_location(tokens: Iterable[str]) -> Optional[str]:
    for token in tokens:
        canonical = NORMALIZE_LOCATION.get(token, token)

        if canonical not in LOCATIONS:
            continue

        # location must not be object or product
        if canonical in OBJECTS or canonical in PRODUCTS:
            continue

        return canonical

    return None
