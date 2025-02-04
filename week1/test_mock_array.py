import unittest
from mock_array import Array

class TestMockArray(unittest.TestCase):
    def setUp(self):
        self.mock_array = Array(max_size=8)

    def test_insert_item_increments_index(self):
        self.assertEqual(self.mock_array.index, -1)
        self.mock_array.append(42)
        self.assertEqual(self.mock_array.index, 0)

    def test_get_inserted_item(self):
        self.mock_array.append(1)
        self.mock_array.append(2)
        self.assertEqual(self.mock_array.get(0), 1)
        self.assertEqual(self.mock_array.get(1), 2)

    def test_get_from_empty_list_raises_error(self):
        with self.assertRaises(IndexError):
            self.mock_array.get(0)