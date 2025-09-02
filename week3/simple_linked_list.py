from __future__ import annotations

from typing import Iterable


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
        return self._value

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
    _length: int

    def __init__(self,
                 values: list[int]):
        self.root = None
        self._current_node = None
        self._length = 0
        if values:
            for value in values:
                self.push(value)

    def __len__(self):
        return self._length

    def __iter__(self) -> Iterable[int]:
        """Simple demonstration of using an iterator
        Note: that this is unsafe in cases where
        you want to have multiple iterations that don't
        interfere with each other mutating global state

        A better approach is to use a separate Iterator.

        Better still use a generator (`yield`)"""
        self._current_node = self.root
        return self

    def __next__(self):
        if not self._current_node:
            raise StopIteration
        value = self._current_node.value
        self._current_node = self._current_node.next_node
        return value

    def push(self, value: int) -> None:
        """Inserts a new node as the root"""
        new_node = Node(value)
        new_node.next_node = self.root
        self.root = new_node
        self._length += 1

    def pop(self) -> int:
        """Removes the current root and returns its value"""
        if self.root is None:
            raise IndexError("Popping from empty list")
        value = self.root.value
        self.root = self.root.next_node
        self._length -= 1
        return value

    def reversed(self) -> list[int]:
        """Returns a list of values in the order they were entered
        (opposite of how they would be returned in a pop)"""
        return list(reversed(list(self)))

    def __repr__(self):

        class_name = self.__class__.__name__
        return f"{class_name}({self.reversed()})"


if __name__ == "__main__":
    pass


