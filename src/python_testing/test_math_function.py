import pytest

from src.python_testing import math_functions


@pytest.mark.parametrize('num1, num2, result',
                         [
                             (7, 3, 10),
                             ('Hello', ' world', 'Hello world'),
                             (10.5, 25.5, 36)
                         ]
                         )
def test_add(num1, num2, result):
    assert math_functions.add(num1, num2) == result
