from mks_backend.models.trips.work_trip import WorkTrip
from mks_backend.repositories import DBSession

from mks_backend.errors.db_basic_error import db_error_handler


class WorkTripRepository:

    def __init__(self):
        self._query = DBSession.query(WorkTrip)

    def get_all_work_trips(self) -> list:
        return self._query.all()

    @db_error_handler
    def add_work_trip(self, work_trip: WorkTrip) -> None:
        DBSession.add(work_trip)
        DBSession.commit()

    def delete_work_trip_by_id(self, id: int) -> None:
        self._query.filter(WorkTrip.work_trips_id == id).delete()
        DBSession.commit()

    @db_error_handler
    def update_work_trip(self, new_work_trip: WorkTrip) -> None:
        old_work_trip = self._query.filter(
            WorkTrip.work_trips_id == new_work_trip.work_trips_id
        )
        old_work_trip.update(
            {
                'trip_date': new_work_trip.trip_date,
                'trip_name': new_work_trip.trip_name,
                'escort_officer': new_work_trip.escort_officer,
                'leadership_positions_id': new_work_trip.leadership_positions_id,
                'protocol_id': new_work_trip.protocol_id
            }
        )

        DBSession.commit()

    def get_work_trip_by_id(self, id: int) -> WorkTrip:
        return self._query.get(id)
