# 3) BST (Binary Search Tree) Search
# [Slide: Binary Search Tree]
# left subtree keys < node.key < right subtree keys.
# Search is O(log n) if balanced; worst case O(n) if skewed.
class BSTNode:
    # __slots__ tells Python to only allow these three attributes.
    __slots__ = ("key", "left", "right")
    def __init__(self, key):
        pass

# insert a key into the BST

    # if the tree is empty, create a new node as root

    # if smaller, insert into the left subtree

    # if larger, insert into the right subtree

    # if equal, do nothing

    # return the root, hint: this may be unchanged


# Search for a key in the BST
def bst_search_iterative():
    """Return the node with key == key, or None if not found (recursive)."""
    # Base case: empty tree or we’ve reached a leaf
    pass

    # start at the root

    # traverse the tree until None is given

        # ff the key matches, return the node

        # if the key is smaller, go left; otherwise, go right

    # if not found, return None


def bst_search_recursive(root, key):
    """Return the node with key == key, or None if not found (recursive)."""
    # Base case: empty tree or we’ve reached a leaf
    pass
    
    # if key matches, return this node
    
    # if key is smaller, search in left subtree
    
    # if key is larger, search in right subtree
