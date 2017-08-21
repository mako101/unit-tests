import os


class DeleteObject(object):

    def delete(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)


class UploadObject(object):

    def __init__(self, delete_object):
        self.delete_object = delete_object

    def upload_complete(self, filename):
        self.delete_object.delete(filename)


