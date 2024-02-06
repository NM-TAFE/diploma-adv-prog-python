from __future__ import annotations
from typing import Any, Optional, Iterable
from node import Node

class EmptyListError(Exception):
    ...


class LinkedList:
    def __init__(self, values: Iterable[int] | None = None) -> None:
        self.head: Node | None = None
        if values:
            self.from_list(values)



    def from_list(self, values):
        for value in values:
            self.append(value)

    def to_list(self) -> list[int]:

        if self.head is None:
            raise EmptyListError("No values to convert")

        current_node = self.head
        values = []
        while current_node:
            values.append(current_node.value)
            current_node = current_node.next_node
        return values

    def push(self, value: int):
        self.head = Node(value, self.head)

    def append(self, value: int) -> None:
        if self.head is None:
            self.head = Node(value)
            return
        current_node = self.head
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = Node(value)


