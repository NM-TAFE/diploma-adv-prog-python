from __future__ import annotations


class Node[T]:
    """A node in a singly-linked list."""
    def __init__(self, data: T, _next: Node[T] | None = None) -> None:
        self._data = data
        self._next = _next

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f"{class_name}({self._data!r}, {self._next!r})"

    def __str__(self) -> str:
        return str(self._data) + " -> " + str(self._next)

    @property
    def next(self) -> Node[T] | None:
        return self._next

    @next.setter
    def next(self, node: Node[T] | None) -> None:
        if not isinstance(node, (Node, type(None))):
            raise TypeError("Next must be a Node instance or None.")
        self._next = node

    @property
    def data(self) -> T:
        return self._data
