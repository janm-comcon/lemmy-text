# core/product_extractor.py
from typing import Iterable, Optional

from core.domain_lexicon_gold import PRODUCTS
from core.domain_normalization import NORMALIZE_PRODUCT


def extract_product(tokens: Iterable[str]) -> Optional[str]:
    for token in tokens:
        canonical = NORMALIZE_PRODUCT.get(token, token)

        if canonical in PRODUCTS:
            return canonical

    return None
