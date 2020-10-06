from sqlalchemy import and_

from mks_backend.models.trips.visited_object import VisitedObject
from mks_backend.repositories import DBSession


class VisitedObjectRepository:

    def __init__(self):
        self._query = DBSession.query(VisitedObject)

    def get_visited_objects_by_work_trip(self, work_trip_id: int) -> list:
        return self._query.filter(VisitedObject.work_trips_id == work_trip_id).all()

    def delete_visited_object(self, work_trip_id: int, construction_id: int) -> None:
        self._query.filter(
            and_(VisitedObject.work_trips_id == work_trip_id, VisitedObject.construction_id == construction_id)
        ).delete()
        DBSession.commit()

    def add_visited_objects(self, visited_objects: tuple) -> None:
        for visited_object in visited_objects:
            DBSession.merge(visited_object)
        DBSession.commit()
