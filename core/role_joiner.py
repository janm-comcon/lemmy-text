# core/role_joiner.py

from typing import Sequence


def join_role(
    role: str,
    values: Sequence[str],
    glue_rules: dict,
) -> str | None:
    """
    Join multiple role values using declarative glue rules.
    """
    if not values:
        return None

    rule = glue_rules[role]
    joined = rule["joiner"].join(values)

    prep = rule.get("preposition")
    if prep:
        return f"{prep} {joined}"

    return joined
