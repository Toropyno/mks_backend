from sqlalchemy import desc

from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.object_file import ObjectFile
from mks_backend.repositories import DBSession


class ObjectFileRepository:

    def get_object_file_by_id(self, id: int) -> ObjectFile:
        return DBSession.query(ObjectFile).get(id)

    def get_all_object_files(self) -> list:
        return DBSession.query(ObjectFile).order_by(desc(ObjectFile.upload_date)).all()

    @db_error_handler
    def add_object_file(self, object_file: ObjectFile) -> None:
        DBSession.add(object_file)
        DBSession.commit()

    def delete_object_file_by_id(self, id: int) -> None:
        DBSession.query(ObjectFile).filter(ObjectFile.object_files_id == id).delete()
        DBSession.commit()

    @db_error_handler
    def update_object_file(self, new_object_file: ObjectFile) -> None:
        DBSession.query(ObjectFile).filter_by(object_files_id=new_object_file.object_files_id).update(
            {
                'idfilestorage': new_object_file.idfilestorage,
                'construction_objects_id': new_object_file.construction_objects_id,
                'upload_date': new_object_file.upload_date,
                'note': new_object_file.note,
            }
        )
        DBSession.commit()
