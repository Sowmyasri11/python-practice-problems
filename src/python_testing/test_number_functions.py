import pytest
from src.python_testing.number_functions import is_even

@pytest.mark.parametrize("num,expected", [(2, True), (3, False), (0, True), (-4, True)])
def test_is_even(num, expected):
    assert is_even(num) == expected
