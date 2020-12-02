from typing import List

from mks_backend.services.filestorage import FilestorageService
from mks_backend.models.inspections.inspection_file import InspectionFile
from mks_backend.repositories.inspections.inspection_file import InspectionFileRepository


class InspectionFileService:

    def __init__(self):
        self.filestorage_service = FilestorageService()
        self.repo = InspectionFileRepository()

    def get_files_by_inspection_id(self, id: int) -> List[InspectionFile]:
        return self.repo.get_files_by_inspection_id(id)

    def add_inspection_file(self, inspection_file: InspectionFile) -> None:
        self.repo.add_inspection_file(inspection_file)

    def delete_inspection_file(self, file_id: str) -> None:
        self.repo.delete_inspection_file_by_id(file_id)
