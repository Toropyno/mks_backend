from os import path as os_path, remove as os_remove
from shutil import copyfileobj

from mks_backend.models.filestorage import Filestorage
from mks_backend.models import DBSession


class FilestorageRepository(object):
    PROTOCOL_STORAGE = '/tmp/protocols/'

    def add_file(self, file):
        DBSession.add(file)
        DBSession.commit()

    def create_file(self, id_file_storage, file):
        file_path = self.PROTOCOL_STORAGE + id_file_storage
        with open(file_path, 'wb') as output_file:
            copyfileobj(file, output_file)

    @classmethod
    def get_filestorage_by_id(cls, id):
        return DBSession.query(Filestorage).get(id)

    @classmethod
    def delete_filestorage_by_id(cls, id):
        # delete from DB
        filestorage = cls.get_filestorage_by_id(id)
        DBSession.delete(filestorage)
        DBSession.commit()
        #  delete from filesystem
        path_to_file = FilestorageRepository.PROTOCOL_STORAGE + id
        if os_path.exists(path_to_file):
            os_remove(path_to_file)
