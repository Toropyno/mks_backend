from typing import List

from sqlalchemy import and_

from mks_backend.models import DBSession
from mks_backend.models.inspections.inspection_file import InspectionFile

from mks_backend.errors.db_basic_error import db_error_handler


class InspectionFileRepository:

    def __init__(self):
        self._query = DBSession.query(InspectionFile)

    @db_error_handler
    def add_inspection_file(self, file: InspectionFile):
        DBSession.add(file)
        DBSession.commit()

    def get_files_by_inspection_id(self, id: int) -> List[InspectionFile]:
        return self._query.filter(InspectionFile.inspections_id == id).all()

    def delete_inspection_file_by_id(self, inspection_id: int, file_id: str) -> None:
        self._query.filter(and_(
            InspectionFile.inspections_id == inspection_id,
            InspectionFile.idfilestorage == file_id
        )).delete()
        DBSession.commit()
