from src.python_testing.string_functions import reverse_string

def test_normal_string():
    assert reverse_string("hello") == "olleh"

def test_empty_string():
    assert reverse_string("") == ""

def test_palindrome():
    assert reverse_string("madam") == "madam"
