from simple_linked_list import Node
import unittest
from unittest import TestCase

def only_positive(a):
    if a < 0:
        raise ValueError("Only positive please")
    return a

class TestNode(unittest.TestCase):
    def setUp(self):
        print("Do stuff before each test!")
        whatever = 42
        self.node = Node(42)
    def test_only_positive_returns_positive_number(self):
        self.assertEqual(only_positive(42), 42)

    def test_negatives_raise_an_error(self):
        self.assertRaises(ValueError, only_positive, -42)
        with self.assertRaises(ValueError):
            only_positive(-42)


    def test_new_node_is_of_type_node(self):
        self.assertIsInstance(Node(42), Node)
        # self.node = "hahahahaha"

    def test_str_repr_is_node_value(self):
        # wrong
        # self.assertEqual(Node(42).__str__(), "42")
        # right:
        self.assertEqual(str(self.node), "42")



# AssertionError: Node(42, None) is not an instance of <class 'str'>
# AssertionError: <simple_linked_list.Node object at 0x0000023443E61E80> is not an instance of <class 'str'>