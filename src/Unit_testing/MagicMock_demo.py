from unittest.mock import MagicMock
#create MagicMock
mock_data = MagicMock()
# configure methods return values
mock_data.connect.return_value = True

mock_data.get_data.return_value = [
    "item1",
    "item2",
]
#use the configured mock
connected = mock_data.connect()
data = mock_data.get_data()

