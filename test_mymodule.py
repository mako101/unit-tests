from mock import patch
from unittest import TestCase
from mymodule import delete


class TestDelete(TestCase):
    @patch('mymodule.os')
    def test_delete(self, mock_os):
        delete('filepath')
        mock_os.delete.assert_called_with('filepath')

