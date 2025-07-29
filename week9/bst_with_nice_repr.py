from __future__ import annotations

class Node[T]:
    def __init__(self, value: T, left: Node =None, right: Node =None):
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other: object):
        if not isinstance(other, Node):
            return NotImplemented
        return self.value == other.value



    def __repr__(self):

        return f'Node({self.value!r}, left={self.left!r}, right={self.right!r})'


class BST[T]:
    def __init__(self, root: Node[T] | None = None):
        self.root = root

    @classmethod
    def from_list(cls, values: list[T]):
        tree = cls()
        for value in values:
            tree.insert(value)
        return tree

    def insert(self, value: T | Node[T], sub_tree_root = None):
        if not isinstance(value, Node):
            new_node = Node(value)
        else:
            new_node = value
        if sub_tree_root is None:
            sub_tree_root = self.root
        if sub_tree_root is None:
            self.root = new_node
            return

        if new_node.value > sub_tree_root.value:
            if sub_tree_root.right is None:
                sub_tree_root.right = new_node
                return
            else:
                self.insert(new_node, sub_tree_root.right)
        else:
            if sub_tree_root.left is None:
                sub_tree_root.left = new_node
                return
            else:
                self.insert(new_node, sub_tree_root.left)

    def __repr__(self):
        return f'BST(root={self.root!r})'


if __name__ == '__main__':
    bst = BST.from_list([4, 6, 2, 8])
    print(bst)
    bst = BST(root=Node(4, left=Node(2, left=None, right=None), right=Node(6, left=None, right=Node(8, left=None, right=None))))