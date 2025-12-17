# core/action_extractor.py
from typing import Iterable, Optional

from core.domain_lexicon_gold import ACTIONS, OBJECTS, LOCATIONS, PRODUCTS
from core.domain_normalization import NORMALIZE_ACTION


def extract_action(tokens: Iterable[str]) -> Optional[str]:
    for token in tokens:
        canonical = NORMALIZE_ACTION.get(token, token)

        if canonical not in ACTIONS:
            continue

        # must not overlap any other category
        if (
            canonical in OBJECTS
            or canonical in LOCATIONS
            or canonical in PRODUCTS
        ):
            continue

        return canonical

    return None
