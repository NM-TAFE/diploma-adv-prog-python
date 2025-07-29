class EmptyListException(Exception):
    pass


class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next_node = _next
    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Node({self.value!r}, {self.next_node!r})"




class LinkedList:
    def __init__(self, _root=None):
         self.root = _root

    def push(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        new_node = Node(value)
        new_node.next_node = self.root
        self.root = new_node




    def __repr__(self):
        return f"LinkedList({self.root!r})"




    def pop(self):
        pass

    def reversed(self):
        pass
