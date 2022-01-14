from mks_backend.entities.trips.work_trip import WorkTripService

from .repository import VisitedObjectRepository


class VisitedObjectService:

    def __init__(self):
        self.work_trip_service = WorkTripService()
        self.repo = VisitedObjectRepository()

    def get_visited_objects_by_work_trip(self, work_trip_id: int) -> list:
        return self.work_trip_service.get_work_trip_by_id(work_trip_id).constructions

    def delete_visited_object(self, work_trip_id: int, construction_id: int) -> None:
        self.repo.delete_visited_object(work_trip_id, construction_id)

    def add_visited_objects(self, visited_objects: tuple):
        self.repo.add_visited_objects(visited_objects)
