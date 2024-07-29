from unittest import TestCase

from node import Node


class TestNode(TestCase):
    def test_node_initialization(self):
        node = Node(1)
        self.assertEqual(node.data, 1)
        self.assertIsNone(node.next)

    def test_push_node(self):
        node = Node(1)

        # can set next to a new node
        node.next = Node(2)
        self.assertEqual(node.next.data, 2)
        self.assertIsNone(node.next.next)

        # can set next to None
        node.next = None
        self.assertIsNone(node.next)

    def test_can_only_set_nextto_node_instance_or_none(self):
        node = Node(1)
        with self.assertRaises(TypeError):
            node.next = 3
        with self.assertRaises(TypeError):
            node.next = "hello"
        with self.assertRaises(TypeError):
            node.next = object()


    def test_node_repr(self):
        node = Node(1)
        self.assertEqual(repr(node), "Node(1, None)")

        node.next = Node(2)
        self.assertEqual(repr(node), "Node(1, Node(2, None))")

    def test_node_str(self):
        node = Node(1)
        self.assertEqual(str(node), "1 -> None")

        node.next = Node(2)
        self.assertEqual(str(node), "1 -> 2 -> None")

if __name__ == "__main__":
    import unittest

    unittest.main()
