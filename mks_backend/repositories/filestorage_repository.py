from mks_backend.models.filestorage import Filestorage
from mks_backend.models import DBSession


class FilestorageRepository(object):
    def add_file(self, file):
        DBSession.add(file)
        DBSession.commit()

    @classmethod
    def get_filestorage_by_id(cls, id):
        return DBSession.query(Filestorage).get(id)

    @classmethod
    def delete_protocol_by_id(cls, id):
        protocol = cls.get_filestorage_by_id(id)
        DBSession.delete(protocol)
        DBSession.commit()
