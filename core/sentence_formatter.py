from core.role_joiner import join_role
from core.domain_lexicon_gold import LOCATION_PREPOSITIONS


GLUE_RULES = {
    "action": {"joiner": " og "},
    "object": {"joiner": " og ", "preposition": "af"},
}


def _pluralize(name: str) -> str:
    if name.endswith("e"):
        return name + "r"
    return name + "er"


def _render_object(obj, emit_quantity: bool) -> str:
    if isinstance(obj, str):
        return obj

    name = obj["name"]
    qty = obj.get("quantity")
    unit = obj.get("unit")

    # plural is grammatical, not optional
    render_name = _pluralize(name) if qty and qty > 1 else name

    if emit_quantity and qty:
        if unit:
            return f"{qty} {unit} {render_name}"
        return f"{qty} {render_name}"

    return render_name


def _render_location(loc: str) -> str:
    prep = LOCATION_PREPOSITIONS.get(loc, "i")
    return f"{prep} {loc}" if prep else loc


def format_sentence(
    actions: list[str],
    products: list[str],
    objects: list,
    locations: list[str],
    *,
    emit_quantity: bool = False,
) -> str:
    parts = []

    # test word handling: render only if explicitly present
    test_present = "afprøvet" in actions
    actions = [a for a in actions if a != "afprøvet"]

    if actions:
        parts.append(join_role("action", actions, GLUE_RULES))

    rendered_objects = [_render_object(o, emit_quantity) for o in objects]

    # product must precede object (bind first product to first object deterministically)
    if products and rendered_objects:
        rendered_objects[0] = f"{products[0]} {rendered_objects[0]}"

    obj_part = join_role("object", rendered_objects, GLUE_RULES)
    if obj_part:
        parts.append(obj_part)

    if locations:
        parts.append(" og ".join(_render_location(l) for l in locations))

    sentence = " ".join(parts).strip()
    if sentence:
        sentence += "."

    # explicit test clause: always prefixed by first object (incl. product + plural), no implicit append
    if test_present and objects:
        first_object = _render_object(objects[0], emit_quantity)
        if products:
            first_object = f"{products[0]} {first_object}"
        sentence += f" {first_object} afprøvet."

    return sentence
