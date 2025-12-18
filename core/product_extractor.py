from typing import Iterable, List

from core.claimed_registry import ClaimedRegistry
from core.domain_lexicon_gold import PRODUCTS, ACTIONS, LOCATIONS, OBJECTS
from core.domain_normalization import NORMALIZE_PRODUCT


def extract_products(
    tokens: Iterable[str],
    registry: ClaimedRegistry,
) -> List[str]:
    products: List[str] = []

    for token in tokens:
        canonical = NORMALIZE_PRODUCT.get(token, token)

        if canonical not in PRODUCTS:
            continue

        if (
            canonical in ACTIONS
            or canonical in LOCATIONS
            or canonical in OBJECTS
        ):
            continue

        if registry.is_claimed(canonical):
            continue

        registry.claim(canonical, "product")
        products.append(canonical)

    return products
