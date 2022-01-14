from typing import List

from .model import WorkTripFile
from .repository import WorkTripFilesRepository


class WorkTripFilesService:

    def __init__(self):
        self.repository = WorkTripFilesRepository()

    def get_all_work_trip_files_by_work_trip_id(self, work_trip_id: int) -> list:
        return self.repository.get_all_work_trip_files_by_work_trip_id(work_trip_id)

    def add_work_trip_file(self, work_trip_files: List[WorkTripFile]) -> None:
        self.repository.add_work_trip_file(work_trip_files)

    def delete_work_trip_file(self, id_) -> None:
        self.repository.delete_work_trip_file(id_)
