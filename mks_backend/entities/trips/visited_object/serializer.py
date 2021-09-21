from .model import VisitedObject


class VisitedObjectSerializer:
    def to_object(self, work_trip_id: int, contruction_id: int) -> VisitedObject:
        return VisitedObject(work_trips_id=work_trip_id, construction_id=contruction_id)

    def convert_list_to_objects(self, work_trip_id: int, contructions: list) -> tuple:
        return tuple(
            self.to_object(work_trip_id, construction_id) for construction_id in contructions
        )
