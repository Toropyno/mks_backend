from typing import List

from mks_backend.session import DBSession
from mks_backend.models.inspections.inspection_file import InspectionFile

from mks_backend.errors import DBBasicError


class InspectionFileRepository:

    def __init__(self):
        self._query = DBSession.query(InspectionFile)

    def add_inspection_file(self, file: InspectionFile):
        DBSession.add(file)
        DBSession.commit()

    def get_files_by_inspection_id(self, id: int) -> List[InspectionFile]:
        return self._query.filter(InspectionFile.inspections_id == id).all()

    def delete_inspection_file_by_id(self, idfilestorage: str) -> None:
        inspection_file = self.get_inspection_file_by_id(idfilestorage)
        DBSession.delete(inspection_file)
        DBSession.commit()

    def get_inspection_file_by_id(self, idfilestorage: str):
        inspection_file = self._query.get(idfilestorage)
        if not inspection_file:
            raise DBBasicError('inspection_file_nf')
        return inspection_file
