from typing import Iterable, List

from core.claimed_registry import ClaimedRegistry
from core.domain_lexicon_gold import ACTIONS, PRODUCTS
from core.domain_normalization import NORMALIZE_ACTION


def extract_actions(
    tokens: Iterable[str],
    registry: ClaimedRegistry,
) -> List[str]:
    actions: List[str] = []

    for token in tokens:
        canonical = NORMALIZE_ACTION.get(token, token)

        if canonical not in ACTIONS:
            continue

        if canonical in PRODUCTS:
            continue

        if registry.is_claimed(canonical):
            continue

        registry.claim(canonical, "action")
        actions.append(canonical)

    return actions
