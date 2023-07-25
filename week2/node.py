from typing import Any, Optional


class Node:
    def __init__(self, data: Any):
        self._data: Any = data
        self.next_node: Optional[Node] = None

    @property
    def data(self):
        return self._data

    def __str__(self):
        return f'{self.data}'

if __name__ == '__main__':
    node = Node(42)
    assert str(node) == '42'

