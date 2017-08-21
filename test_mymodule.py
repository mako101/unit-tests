from mock import patch
from unittest import TestCase
from mymodule import DeleteObject, UploadObject


class TestDelete(TestCase):

    def setUp(self):
        self.del_obj = DeleteObject()

    @patch('mymodule.os')
    def test_delete_exiting_file(self, mock_os):
        # the file does not exist
        mock_os.path.isfile.return_value = True

        self.del_obj.delete('filename')
        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with('filename')

    @patch('mymodule.os')
    def test_do_not_delete_non_existent_file(self, mock_os):
        # the file does not exist
        mock_os.path.isfile.return_value = False

        self.del_obj.delete('file')
        self.assertFalse(mock_os.remove.called, "Tried to delete non-existent file!")


class TestUpload(TestCase):

    @patch.object(DeleteObject, 'delete')
    def test_successful_upload(self, mock_delete):

        upload_object = UploadObject(delete_object=DeleteObject)
        upload_object.upload_complete('uploaded_file')

        mock_delete.delete.assert_called_with('uploaded_file')