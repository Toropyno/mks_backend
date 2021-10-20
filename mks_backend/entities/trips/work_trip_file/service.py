from .repository import WorkTripFilesRepository
from .model import WorkTripFiles


class WorkTripFilesService:

    def __init__(self):
        self.repository = WorkTripFilesRepository()

    def get_all_work_trip_files(self, work_trip_id: int) -> list:
        return self.repository.get_all_work_trip_files(work_trip_id)

    def add_work_trip_file(self, work_trip_file: WorkTripFiles) -> None:
        self.repository.add_work_trip_file(work_trip_file)

    def delete_work_trip_file(self, id) -> None:
        self.repository.delete_work_trip_file(id)
