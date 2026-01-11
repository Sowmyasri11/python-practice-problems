import pytest
from src.python_testing.math_functions import multiply

@pytest.fixture
def numbers():
    return (2,3)

def test_multiply(numbers):
    a, b=numbers
    assert multiply(a,b)==6