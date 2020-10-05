from mks_backend.models.trips.work_trip import WorkTrip
from mks_backend.repositories.trips.work_trip import WorkTripRepository


class WorkTripService:

    def __init__(self):
        self.repo = WorkTripRepository()

    def get_all_work_trips(self) -> list:
        return self.repo.get_all_work_trips()

    def get_work_trip_by_id(self, id: int) -> WorkTrip:
        return self.repo.get_work_trip_by_id(id)

    def add_work_trip(self, work_trip: WorkTrip) -> None:
        self.repo.add_work_trip(work_trip)

    def update_work_trip(self, new_work_trip: WorkTrip) -> None:
        self.repo.update_work_trip(new_work_trip)

    def delete_work_trip_by_id(self, id: int) -> None:
        self.repo.delete_work_trip_by_id(id)
