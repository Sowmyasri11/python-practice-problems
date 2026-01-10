from unittest.mock import Mock

from src.Unit_testing import employee

# create mock object
mock_object = Mock()

# confiugre return value
mock_object.return_Value = "Hello world!"

# call the mock
result = mock_object()

# configure method on mock
mock_object.some_method.return_value = 42

# call the method
value = mock_object().some_method()
