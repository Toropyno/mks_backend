from typing import List

from mks_backend.models import DBSession
from mks_backend.models.inspections.inspection_file import InspectionFile


class InspectionFileRepository:

    def __init__(self):
        self._query = DBSession.query(InspectionFile)

    def add_inspection_file(self, file: InspectionFile):
        DBSession.add(file)
        DBSession.commit()

    def get_files_by_inspection_id(self, id: int) -> List[InspectionFile]:
        return self._query.filter(InspectionFile.inspections_id == id).all()

    def delete_inspection_file_by_id(self, id) -> None:
        self._query.filter(InspectionFile.inspections_id == id).delete()
        DBSession.commit()
