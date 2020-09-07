from mks_backend.models.filestorage import Filestorage
from mks_backend.models import DBSession


class FilestorageRepository:

    def add_filestorage(self, file: Filestorage):
        DBSession.add(file)
        DBSession.commit()

    @classmethod
    def get_filestorage_by_id(cls, id: str) -> Filestorage:
        return DBSession.query(Filestorage).get(id)

    @classmethod
    def delete_filestorage_by_id(cls, id) -> None:
        filestorage = cls.get_filestorage_by_id(id)
        DBSession.delete(filestorage)
        DBSession.commit()
