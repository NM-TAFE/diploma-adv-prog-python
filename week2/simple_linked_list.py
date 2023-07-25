from node import Node
from typing import Any, Optional


class EmptyListError(Exception):
    """Raised when trying to modify a list with no nodes"""


class SimpleLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def remove_from_left(self) -> None:
        if self.head is None:
            raise EmptyListError("List is empty")

        self.head = self.head.next_node

    def add(self, data: Any) -> None:
        if self.head is None:
            self.head = Node(data)
            return
        current_node = self.head
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = Node(data)

    def to_list(self) -> list:
        if self.head is None:
            return []

        node_values = []
        current_node = self.head
        while current_node is not None:
            node_values.append(current_node.data)
            current_node = current_node.next_node
        return node_values


if __name__ == '__main__':
    my_list = SimpleLinkedList()
    my_list.add("Rafael")
    my_list.add("Fafel")
    my_list.add("Shmufel")
    print(my_list.to_list())
    try:
        while True:
            my_list.remove_from_left()
    except EmptyListError:
        print("List is empty")
    print(my_list.to_list())
    my_node = Node("somedata")
    print(my_node.data)
    my_node._data = "some other data"
    print(my_node.data)
