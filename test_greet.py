import unittest

from greet import greet


class GreetTest(unittest.TestCase):
    def test_greet_name(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_greet_empty_string_raises(self):
        with self.assertRaises(ValueError):
            greet("")


if __name__ == "__main__":
    unittest.main()
