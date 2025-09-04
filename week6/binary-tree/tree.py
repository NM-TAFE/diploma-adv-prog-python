from node import Node


class Tree:
    def __init__(self):
        self.__root = None

    def find(self, key):
        current = self.__root
        while current.key != key:
            if key < current.key:
                current = current.subtree_left
            else:
                current = current.subtree_right

            if current is None:
                return None

        return current

    def insert(self, key, value):
        new_node = Node()
        new_node.key = key
        new_node.value = value

        if self.__root is None:
            self.__root = new_node
        else:
            current = self.__root
            while True:
                parent = current
                if key < current.key:
                    current = current.subtree_left
                    if current is None:
                        parent.subtree_left = new_node
                        return
                else:
                    current = current.subtree_right
                    if current is None:
                        parent.subtree_right = new_node
                        return

    def traverse(self, _type):
        if _type == 1:
            print("Pre-order traversal:")
            self.pre_order(self.__root)
        elif _type == 2:
            print("In-order traversal:")
            self.in_order(self.__root)
        elif _type == 3:
            print("Post-order traversal:")
            self.post_order(self.__root)

    @staticmethod
    def pre_order(root):
        if root is not None:
            print(str(root))
            Tree.pre_order(root.subtree_left)
            Tree.pre_order(root.subtree_right)

    @staticmethod
    def in_order(root):
        if root is not None:
            Tree.in_order(root.subtree_left)
            print(str(root))
            Tree.in_order(root.subtree_right)

    @staticmethod
    def post_order(root):
        if root is not None:
            Tree.post_order(root.subtree_left)
            Tree.post_order(root.subtree_right)
            print(str(root))
