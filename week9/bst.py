from __future__ import annotations


class Node[T]:
    _value: T
    _left: Node[T]
    _right: Node[T]

    def __init__(self,
                 value: T,
                 _left: Node[T] | None = None,
                 _right: Node[T] | None = None):
        self._value = value
        self._left = _left
        self._right = _right

    @property
    def value(self) -> T:
        return self._value

    @property
    def left_node(self) -> Node[T]:
        return self._left

    @left_node.setter
    def left_node(self, node: Node[T]):
        self._left = node

    @property
    def right_node(self) -> Node[T]:
        return self._right

    @right_node.setter
    def right_node(self, node: Node[T]):
        self._right = node

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}(value={self.value!r}, _left={self._left!r}, _right={self._right!r})'

class BST[T]:
    _root: Node[T]

    def __init__(self, _root: Node[T] | None = None):
        self._root = _root

    @property
    def is_empty(self):
        return self._root is None


    def _unwind_tree(self, node: Node):

        if node is None:
            return
        yield from self._unwind_tree(node._left)
        yield node.value
        yield from self._unwind_tree(node._right)



    def insert_with_while(self,
                          value: T) -> None:

        new_node: Node[T] = Node(value)
        if self._root is None:
            self._root = new_node
            return

        next_node = self._root

        while True:
            if new_node < next_node:
              if next_node.left_node is None:
                  next_node.left_node = new_node
                  return
              else:
                  next_node = next_node.left_node

            else:
                if next_node.right_node is None:
                    next_node.right_node = new_node
                    return
                else:
                    next_node = next_node.right_node


    def insert(self,
               value: T | Node[T],
               current_root: Node[T] | None = None) -> None:

        if not isinstance(value, Node):
            new_node = Node(value)
        else:
            new_node = value

        if self._root is None:
            self._root = new_node
            return

        if current_root is None:
            current_root = self._root
        # -------------

        if new_node < current_root:
            # only valid if left_node is None
            # keep walking down the tree otherwise...
            if current_root.left_node is None:
                current_root.left_node = new_node
            else:
                self.insert(new_node, current_root.left_node)

        else:
            if current_root.right_node is None:
                current_root.right_node = new_node
            else:
                self.insert(new_node.value, current_root.right_node)

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}({self._root!r})'


if __name__ == '__main__':
    import random
    bst = BST[int]()
    bst.insert = bst.insert_with_while
    for _ in range(20):

        bst.insert(random.randint(0,10000))
        # bst.insert(24)
        # bst.insert(12)
        # print(bst)
    # for x in  bst._unwind_tree(5):
    #     print(x)

    for x in bst._unwind_tree(bst._root):
        print(x)


    # print(next(x))
    # print("whatever")
    # print(next(x))

