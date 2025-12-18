# core/claimed_registry.py
from typing import Dict


class ClaimedRegistry:
    """
    Tracks which canonical tokens have been claimed
    by which semantic role during extraction.
    """

    def __init__(self):
        self._claimed: Dict[str, str] = {}

    def is_claimed(self, token: str) -> bool:
        return token in self._claimed

    def claim(self, token: str, role: str) -> None:
        self._claimed[token] = role

    def role_of(self, token: str) -> str | None:
        return self._claimed.get(token)
