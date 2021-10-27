from typing import List

from .model import InspectionFile
from .repository import InspectionFileRepository

from mks_backend.entities.filestorage import FilestorageService


class InspectionFileService:

    def __init__(self):
        self.filestorage_service = FilestorageService()
        self.repo = InspectionFileRepository()

    def get_files_by_inspection_id(self, id: int) -> List[InspectionFile]:
        return self.repo.get_files_by_inspection_id(id)

    def add_inspection_files(self, inspection_files: List[InspectionFile]) -> None:
        self.repo.add_inspection_files(inspection_files)

    def delete_inspection_file(self, file_id: str) -> None:
        self.repo.delete_inspection_file_by_id(file_id)
