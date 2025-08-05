from __future__ import annotations

from typing import Any, Optional

class EmptyListException(Exception):
    pass


class Node:
    value: int
    next_node: Node | None

    def __init__(self,
                 value: int,
                 _next: Node | None = None
                 ) -> None:
        self.value = value
        self.next_node = _next

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}({self.value!r}, {self.next_node!r})"


class LinkedList:
    root: Node

    def __init__(self, _root: Node | None = None):
        self.root = _root

    def __iter__(self):
        ...

    def push(self, value: int) -> None:
        """Inserts a new node as the head"""
        pass

    def pop(self) -> int:
        """removes the current head and returns its value"""
        pass

    def reversed(self) -> list[int, ...]:
        """Returns a list of values in the order they were entered
        (opposite of how they would be returned in a pop)"""
        pass

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}({self.root!r})"


