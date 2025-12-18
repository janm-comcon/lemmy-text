from typing import Iterable, List, Optional

from core.claimed_registry import ClaimedRegistry
from core.domain_lexicon_gold import OBJECTS, UNITS
from core.domain_normalization import NORMALIZE_OBJECT


DEFAULT_UNIT = "stk"


def _pluralize(name: str) -> str:
    if name.endswith("e"):
        return name + "r"
    return name + "er"


def _singularize_if_possible(token: str) -> str:
    # deterministic plural reduction only if singular is in OBJECTS
    if token.endswith("er"):
        cand = token[:-2]
        if cand in OBJECTS:
            return cand
    if token.endswith("e"):
        cand = token[:-1]
        if cand in OBJECTS:
            return cand
    return token


def extract_objects(tokens: Iterable[str], registry: ClaimedRegistry) -> List[dict]:
    objects: List[dict] = []

    pending_qty: Optional[int] = None
    pending_unit: Optional[str] = None

    for token in tokens:
        if token.isdigit():
            pending_qty = int(token)
            continue

        if token in UNITS:
            pending_unit = token
            continue

        token = _singularize_if_possible(token)
        canonical = NORMALIZE_OBJECT.get(token, token)

        if canonical not in OBJECTS:
            continue

        # IMPORTANT: do NOT exclude overlap with ACTIONS/LOCATIONS/PRODUCTS here.
        # Priority + registry decide the role.
        if registry.is_claimed(canonical):
            continue

        unit = pending_unit
        if pending_qty and pending_qty > 1 and not unit:
            unit = DEFAULT_UNIT

        registry.claim(canonical, "object")
        objects.append(
            {
                "name": canonical,
                "quantity": pending_qty,
                "unit": unit,
            }
        )

        pending_qty = None
        pending_unit = None

    return objects
