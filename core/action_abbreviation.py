# core/action_abbreviation.py
"""
General, gold-driven action abbreviation expansion.

An abbreviation expands ONLY if it uniquely matches
a canonical action prefix.
"""

from core.domain_lexicon_gold import ACTIONS


MIN_PREFIX_LEN = 3


def expand_action_abbreviation(token: str) -> str:
    """
    Expand token to canonical action if it is a unique prefix.

    Examples:
        inst   -> installation
        mont   -> montering
        udsk   -> udskiftning
        mon    -> montering
        i      -> i  (too short)
        re     -> re (ambiguous)
    """
    # exact match → already canonical
    if token in ACTIONS:
        return token

    if len(token) < MIN_PREFIX_LEN:
        return token

    matches = [a for a in ACTIONS if a.startswith(token)]

    if len(matches) == 1:
        return matches[0]

    return token
