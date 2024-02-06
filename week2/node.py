from __future__ import annotations


class Node:
    def __init__(self, value: int,
                 next_node: Node | None = None) \
            -> None:
        self._value: int = value
        self._next_node: Node | None = next_node

    @property
    def value(self) -> int:
        return self._value

    @property
    def next_node(self) -> Node:
        return self._next_node

    @next_node.setter
    def next_node(self, node: Node):
        self._next_node = node

    def __str__(self) -> str:
        return f'{self.value}'

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return (f'{class_name}({self.value!r}, '
                f'{self.next_node!r})')

