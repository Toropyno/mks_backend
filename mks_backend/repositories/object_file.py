from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.object_file import ObjectFile
from mks_backend.repositories import DBSession


class ObjectFileRepository:

    def get_object_file_by_id(self, id: int) -> ObjectFile:
        return DBSession.query(ObjectFile).get(id)

    def get_all_object_files(self) -> list:
        return DBSession.query(ObjectFile).order_by(ObjectFile.upload_date).all()

    @db_error_handler
    def add_object_file(self, object_file: ObjectFile) -> None:
        DBSession.add(object_file)
        DBSession.commit()

    def delete_object_file(self, object_file: ObjectFile) -> None:
        DBSession.delete(object_file)
        DBSession.commit()
