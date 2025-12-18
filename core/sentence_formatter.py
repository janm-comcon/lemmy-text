# core/sentence_formatter.py

from core.role_joiner import join_role


GLUE_RULES = {
    "action": {
        "joiner": " og ",
    },
    "object": {
        "joiner": " og ",
        "preposition": "af",
    },
    "location": {
        "joiner": " og ",
        "preposition": "i",
    },
}


def format_sentence(
    actions: list[str],
    objects: list[str],
    locations: list[str],
) -> str:
    """
    Format sentence using role-based glue rules.

    Special rule:
    - If the only action is 'afprøvet' and at least one object exists,
      bind the test explicitly to the first object:
        '<object> afprøvet.'
    """
    # --- special disambiguation rule ---
    if actions == ["afprøvet"] and objects:
        return f"{objects[0]} afprøvet."

    # --- default behavior ---
    if not actions:
        actions = ["afprøvet"]

    parts = []

    # actions first
    parts.append(join_role("action", actions, GLUE_RULES))

    obj_part = join_role("object", objects, GLUE_RULES)
    if obj_part:
        parts.append(obj_part)

    loc_part = join_role("location", locations, GLUE_RULES)
    if loc_part:
        parts.append(loc_part)

    sentence = " ".join(parts) + "."

    if "afprøvet" not in actions:
        sentence += " afprøvet."

    return sentence
