import re

from core.spell_correction import correct_text
from core.action_abbreviation import expand_action_abbreviation
from core.lemmatizer import lemmatize_text
from core.number_normalization import normalize_numbers

from core.claimed_registry import ClaimedRegistry
from core.action_extractor import extract_actions
from core.location_extractor import extract_locations
from core.object_extractor import extract_objects
from core.product_extractor import extract_products

from core.sentence_formatter import format_sentence


def _normalize_clause(clause: str) -> str:
    # 1) spell correction (clause-local)
    clause = correct_text(clause)

    # 2) tokenize (keep digits)
    raw_tokens = clause.lower().split()

    # 3) action abbreviation expansion
    raw_tokens = [expand_action_abbreviation(t) for t in raw_tokens]

    # 4) number-word normalization
    raw_tokens = normalize_numbers(raw_tokens)

    # 5) lemmatize
    tokens = lemmatize_text(" ".join(raw_tokens))

    # 6) role extraction with registry (per clause)
    registry = ClaimedRegistry()
    actions = extract_actions(tokens, registry)
    products = extract_products(tokens, registry)
    locations = extract_locations(tokens, registry)
    objects = extract_objects(tokens, registry)

    # 7) sentence realization
    # If nothing semantic extracted, pass through (status sentence)
    if not actions and not products and not objects and not locations:
        s = " ".join(raw_tokens).strip()
        return f"{s}." if s else ""

    return format_sentence(actions, products, objects, locations, emit_quantity=True)


def normalize_text(text: str) -> str:
    # Split into sentences deterministically by punctuation
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]

    out_parts: list[str] = []
    for sent in sentences:
        # Split into clauses on ' og ' (deterministic, surface-based)
        clauses = [c.strip() for c in re.split(r"\s+og\s+", sent, flags=re.IGNORECASE) if c.strip()]
        for clause in clauses:
            normalized = _normalize_clause(clause)
            if normalized:
                out_parts.append(normalized)

    return " ".join(out_parts)
