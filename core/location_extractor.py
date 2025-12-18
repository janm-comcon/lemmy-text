from typing import Iterable, List

from core.claimed_registry import ClaimedRegistry
from core.domain_lexicon_gold import LOCATIONS, ACTIONS, PRODUCTS
from core.domain_normalization import NORMALIZE_LOCATION


def extract_locations(
    tokens: Iterable[str],
    registry: ClaimedRegistry,
) -> List[str]:
    locations: List[str] = []

    for token in tokens:
        canonical = NORMALIZE_LOCATION.get(token, token)

        if canonical not in LOCATIONS:
            continue

        if canonical in ACTIONS or canonical in PRODUCTS:
            continue

        if registry.is_claimed(canonical):
            continue

        registry.claim(canonical, "location")
        locations.append(canonical)

    return locations
