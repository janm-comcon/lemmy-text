from core.spell_correction import correct_text
from core.action_abbreviation import expand_action_abbreviation
from core.lemmatizer import lemmatize_text

from core.claimed_registry import ClaimedRegistry
from core.action_extractor import extract_actions
from core.location_extractor import extract_locations
from core.object_extractor import extract_objects
from core.product_extractor import extract_products
from core.number_normalization import normalize_numbers

from core.sentence_formatter import format_sentence


def normalize_text(text: str) -> str:
    # 1. spell correction
    text = correct_text(text)

    # 2. early tokenization
    raw_tokens = [
        t for t in text.lower().split()
        if not t.isdigit()
    ]

    # 3. action abbreviation expansion
    raw_tokens = [expand_action_abbreviation(t) for t in raw_tokens]

    # 4. lemmatize
    tokens = lemmatize_text(" ".join(raw_tokens))

    # 5. role extraction with registry
    registry = ClaimedRegistry()

    actions = extract_actions(tokens, registry)
    locations = extract_locations(tokens, registry)
    objects = extract_objects(tokens, registry)
    _products = extract_products(tokens, registry)

    # 6. sentence realization
    return format_sentence(actions, objects, locations)
