from unittest import TestCase
from unittest.mock import patch

def greet_user():
    name = input("Enter your name: ")
    return f"Hello, {name}!"

class TestGreetUser(TestCase):
    @patch('builtins.input', return_value='Dylan')
    def test_greet_user(self, mock_input):
        # Call the function that requires user input
        result = greet_user()

        # Assert that the function returns the expected result
        self.assertEqual(result, "Hello, Ben!")

if __name__ == "__main__":
    import unittest
    unittest.main()
