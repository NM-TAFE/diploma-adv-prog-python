import unittest

class Cat:
    def act(self, action):
        if action == "bark":
            return "Woof! Woof!"

def key(self, val):
    if not val:
        raise ValueError
    if not isinstance(val, str):
        raise TypeError

    self.val = val

class TestMe(unittest.TestCase):
    def test_raise_exception_when_asked_to_bark(self):
        self.assertRaises(ValueError,
                          Cat().act("bark"),
                          "bark")
        with self.assertRaises(ValueError):
            Cat().act("bark")
            raise ValueError
