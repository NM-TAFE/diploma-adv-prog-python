from __future__ import annotations
class Node:
    next_node: Node | None
    _value: int

    def __init__(self):
        self._value = 42
        self.next_node = None

    @property
    def value(self) -> int:
        return self._value