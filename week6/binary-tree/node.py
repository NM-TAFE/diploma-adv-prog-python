class Node:
    def __init__(self):
        self.key = None
        self.value = None
        self.subtree_right = None
        self.subtree_left = None

    def __str__(self):
        return "{ " + str(self.key) + " => " + str(self.value) + " }"
