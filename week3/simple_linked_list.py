from __future__ import annotations

from typing import Any, Iterator

class EmptyListException(Exception):
    pass


class Node:
    value: int
    next_node: Node | None

    def __init__(self,
                 value: int,
                 _next: Node | None = None
                 ) -> None:
        self._value = value
        self.next_node = _next

    @property
    def value(self):
        return self.value

    @value.setter
    def value(self, value):
        self._value = value



    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self):
        class_name = self.__class__.__name__
        return (f"{class_name}({self.value!r}"
                f", {self.next_node!r})")


class LinkedList:
    root: Node | None
    _current_node: Node | None


    def __init__(self, _root: Node | None = None):
        self.root = _root
        self._current_node = None

    def __iter__(self) -> Iterator:
        self._current_node = self.root
        return self

    def __next__(self):
        if not self._current_node:
            raise StopIteration
        value = self._current_node.value
        self._current_node = self._current_node.next_node
        return value

    def push(self, value: int) -> None:
        """Inserts a new node as the head"""
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        new_node.next_node = self.root
        self.root = new_node

    def pop(self) -> int:
        """removes the current head and returns its value"""
        value = self.root.value
        self.root = self.root.next_node
        return value

    def reversed(self) -> list[int, ...]:
        """Returns a list of values in the order they were entered
        (opposite of how they would be returned in a pop)"""
        pass

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}({self.root!r})"


