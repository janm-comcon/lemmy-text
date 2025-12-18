from typing import Iterable, List

from core.claimed_registry import ClaimedRegistry
from core.domain_lexicon_gold import OBJECTS, ACTIONS, LOCATIONS, PRODUCTS
from core.domain_normalization import NORMALIZE_OBJECT


def extract_objects(
    tokens: Iterable[str],
    registry: ClaimedRegistry,
) -> List[str]:
    objects: List[str] = []

    for token in tokens:
        canonical = NORMALIZE_OBJECT.get(token, token)

        if canonical not in OBJECTS:
            continue

        if (
            canonical in ACTIONS
            or canonical in LOCATIONS
            or canonical in PRODUCTS
        ):
            continue

        if registry.is_claimed(canonical):
            continue

        registry.claim(canonical, "object")
        objects.append(canonical)

    return objects
