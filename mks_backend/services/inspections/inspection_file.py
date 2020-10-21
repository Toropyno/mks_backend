from typing import List

from mks_backend.models.inspections.inspection_file import InspectionFile
from mks_backend.repositories.inspections.inspection_file import InspectionFileRepository


class InspectionFileService:

    def __init__(self):
        self.repo = InspectionFileRepository()

    def get_files_by_inspection_id(self, id: int) -> List[InspectionFile]:
        return self.repo.get_files_by_inspection_id(id)

    def add_inspection_file(self, inspection_file: InspectionFile) -> None:
        return self.repo.add_inspection_file(inspection_file)

    def delete_inspection_file(self, inspection_id: int, file_id: str) -> None:
        self.repo.delete_inspection_file_by_id(id)
