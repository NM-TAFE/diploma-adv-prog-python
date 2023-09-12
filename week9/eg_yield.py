from typing import Iterator, Optional, TypeVar, Generic, Sequence

T = TypeVar("T", int, str, float)

class Node(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.next_node = None

    def __repr__(self):
        return f'Node({self.value!r}, {self.next_node!r})'

class LinkedList(Generic[T]):
    def __init__(self, from_list: Optional[Sequence[T]] = None):
        self.root: Optional[Node[T]] = None
        if from_list:
            [self.add_node(Node(value)) for value in from_list]

    def add_node(self, new_node: Node[T]):
        if self.root is None:
            self.root = new_node
            return
        for node in self._iter_over_nodes():
            if node.next_node is None:
                node.next_node = new_node
                break

    def _iter_over_nodes(self) -> Iterator[Node[T]]:
        current_node = self.root
        while current_node is not None:
            yield current_node
            current_node = current_node.next_node

    def __iter__(self) -> Iterator[T]:
        for node in self._iter_over_nodes():
            yield node.value

    def to_list(self) -> list[T]:
        return list(self)


# example generate from (delegate to an interator)
def generate_from():
    list_ = [1, 23,3, 4, 5]
    yield from list_
    x = yield
    print(x)


if __name__ == '__main__':
    my_list = LinkedList([1, 2, 3, 4, 5])
    for value in my_list:
        print(value)
        if value == 3:
            break
    print(list(my_list))