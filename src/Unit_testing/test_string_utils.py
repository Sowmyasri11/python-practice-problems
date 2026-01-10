import unittest
from string_utils import StringUtils

class TestStringUtils(unittest.TestCase):
    def setUp(self):
        self.util = StringUtils()

    def test_reverse(self):
        self.assertEqual(self.util.reverse_string("abc"), "cba")

    def test_palindrome(self):
        self.assertTrue(self.util.is_palindrome("madam"))
        self.assertFalse(self.util.is_palindrome("hello"))

if __name__ == "__main__":
    unittest.main()
