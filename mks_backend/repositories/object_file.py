from sqlalchemy import desc

from mks_backend.models.object_file import ObjectFile
from mks_backend.models import DBSession

from mks_backend.errors.db_basic_error import db_error_handler, DBBasicError


class ObjectFileRepository:

    def __init__(self):
        self._query = DBSession.query(ObjectFile)

    def get_object_file_by_id(self, id: int) -> ObjectFile:
        object_file = self._query.get(id)
        if not object_file:
            raise DBBasicError('object_file_nf')
        return object_file

    def get_all_object_files(self) -> list:
        return self._query.order_by(desc(ObjectFile.upload_date)).all()

    @db_error_handler
    def add_object_file(self, object_file: ObjectFile) -> None:
        DBSession.add(object_file)
        DBSession.commit()

    def delete_object_file_by_id(self, id_: int) -> None:
        object_file = self.get_object_file_by_id(id_)
        DBSession.delete(object_file)
        DBSession.commit()

    @db_error_handler
    def update_object_file(self, new_object_file: ObjectFile) -> None:
        self._query.filter_by(object_files_id=new_object_file.object_files_id).update(
            {
                'idfilestorage': new_object_file.idfilestorage,
                'construction_objects_id': new_object_file.construction_objects_id,
                'upload_date': new_object_file.upload_date,
                'note': new_object_file.note,
            }
        )
        DBSession.commit()
