from __future__ import annotations
from typing import Generator, Self

from node import Node


class LinkedList[T]:
    """A singly-linked list."""
    def __init__(self, _head: Node | None = None) -> None:
        self._head = _head

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f"{class_name}({self._head!r})"

    def __str__(self) -> str:
        return str(self._head)

    def push(self, data: T) -> None:
        """Add a new node to the head of the list."""
        new_node = Node[T](data, self._head)
        self._head = new_node

    def pop(self) -> T:
        """Remove the head node and return its data."""
        if self._head is None:
            raise IndexError("pop from empty list")
        data = self._head.data
        self._head = self._head.next
        return data

    # __iter__ must return an iterable (an object with a __next__ method))
    def __iter__(self) -> Self:
        self._iter_node = self._head
        return self

    def __next__(self) -> T:
        if self._iter_node is None:
            raise StopIteration
        data = self._iter_node.data
        self._iter_node = self._iter_node.next
        return data

    # ALT: alternatively, we could define __iter__ as a generator
    # (The generator has a __next__ method, so it's an iterator too)
    # TODO: comment-out **both** the __iter__ and __next__ methods above
    # TODO:  uncomment the __iter__ method below:
    # ######
    # def __iter__(self) -> Generator[T, None, None]:
    #     node = self._head
    #     while node is not None:
    #         yield node.data
    #         node = node.next
    # #####
