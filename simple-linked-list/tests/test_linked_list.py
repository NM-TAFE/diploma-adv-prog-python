from linked_list import LinkedList
from node import Node

from unittest import TestCase


class TestLinkedList(TestCase):
    def setUp(self):
        self.linked_list = LinkedList[int]()

    def test_linked_list_initialization(self):
        self.assertIsNone(self.linked_list._head)
        self.assertIsInstance(self.linked_list, LinkedList)

    def test_push_to_empty_list(self):
        self.linked_list.push(1)
        self.assertIsNotNone(self.linked_list._head)
        self.assertEqual(self.linked_list._head.data, 1) # type: ignore
        self.assertIsInstance(self.linked_list._head, Node)
        self.assertIsNone(self.linked_list._head.next) # type: ignore

    def test_push_multiple_values(self):
        self.linked_list.push(1)
        self.linked_list.push(2)
        self.assertEqual(self.linked_list._head.data, 2)
        self.assertEqual(self.linked_list._head.next.data, 1)
        self.assertIsNone(self.linked_list._head.next.next)

        self.linked_list.push(3)
        self.assertEqual(self.linked_list._head.data, 3)
        self.assertEqual(self.linked_list._head.next.data, 2)
        self.assertIsNotNone(self.linked_list._head.next.next)

    def test_pop(self):
        with self.assertRaises(IndexError):
            self.linked_list.pop()

        self.linked_list.push(1)
        self.linked_list.push(2)
        self.assertEqual(self.linked_list.pop(), 2)
        self.assertEqual(self.linked_list.pop(), 1)
        with self.assertRaises(IndexError):
            self.linked_list.pop()

    def test_iter(self):
        linked_list = LinkedList()
        linked_list.push(1)
        linked_list.push(2)
        linked_list.push(3)

        for i, data in enumerate(linked_list):
            self.assertEqual(data, 3 - i)

    def test_repr(self):
        linked_list = LinkedList()
        self.assertEqual(repr(linked_list), "LinkedList(None)")

        linked_list.push(1)
        self.assertEqual(repr(linked_list), "LinkedList(Node(1, None))")

        linked_list.push(2)
        self.assertEqual(repr(linked_list), "LinkedList(Node(2, Node(1, None)))")

    def test_str(self):
        linked_list = LinkedList()
        self.assertEqual(str(linked_list), "None")

        linked_list.push(1)
        self.assertEqual(str(linked_list), "1 -> None")

        linked_list.push(2)
        self.assertEqual(str(linked_list), "2 -> 1 -> None")
