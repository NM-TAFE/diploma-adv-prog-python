from __future__ import annotations
from quick_sort import Player # please don't keep your player in your quick sort!


class Node:
    def __init__(self,
                 player: Player,
                 left: Node | None = None,
                 right: Node | None = None):
        self.player = player
        self.left = left
        self.right = right

    def __iter__(self):
        return iter((self.player, self.left, self.right))

    def __lt__(self, other: Node):
        if not isinstance(other, Node):
            raise TypeError("Can only compare players")

        return self.player < other.player

    def __repr__(self):
        class_name = self.__class__.__name__
        return (f"{class_name}({self.player!r}, "
                f"{self.left!r},"
                f"{self.right!r})")


class BST:
    def __init__(self,
                 _root: Node | None):
        self.root = _root

    def insert(self, player: Player | Node, current_node: Node | None = None ):
        if isinstance(player, Player):
            node = Node(player)
        elif isinstance(player, Node):
            node = player
        else:
            raise TypeError(f"Unsupported player type: {player=} {type(player)=}")

        if self.root is None:
            self.root = node
            return

        current_node = current_node or self.root
        if current_node < node:
            if current_node.left is None:
                current_node.left = node
            else:
                self.insert(node, current_node.left)

        elif current_node.right is None:
            current_node.right = node

        else:
            self.insert(node, current_node.right)

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}({self.root!r})"


if __name__ == '__main__':
    bst = BST(Node(Player(42)))
    bst.insert(Node(Player(12)))
    bst.insert(Node(Player(50)))
    bst.insert(Node(Player(100)))
    print(bst)
