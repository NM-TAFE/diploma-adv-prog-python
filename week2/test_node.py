from node import Node
import unittest

class TestNode(unittest.TestCase):

    def test_node_initialised_with_none_next_node(self):
        '''test not initialisation'''
        # arrange act assert
        # arrange
        node = Node("some data")
        # act -> assert
        self.assertIsNone(node.next_node)

    def test_string_representation_of_node(self):
        node = Node("some data")
        self.assertEquals(str(node), "some data")
        i


