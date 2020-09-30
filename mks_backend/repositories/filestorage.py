from mks_backend.models import DBSession
from mks_backend.models.filestorage import Filestorage


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

    def get_many_file_storages_by_id(self, ids: list) -> list:
        return DBSession.query(Filestorage).filter(
            Filestorage.file_storages_id.in_(ids)
        ).all()
