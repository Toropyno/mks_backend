from mks_backend.models.trips.work_trip import WorkTrip
from mks_backend.models.protocols.protocol import Protocol
from mks_backend.models.construction import Construction
from mks_backend.models.trips.visited_object import VisitedObject
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

    def get_filtered_work_trips(self, params: dict) -> list:

        # Here it is necessary to combine the tables using the outerjoin method
        # to be able to filter by the entities to which work_trip refers
        work_trips = self._query\
            .outerjoin(VisitedObject, Construction)\
            .outerjoin(Protocol)

        if 'trip_name' in params:
            trip_name = params['trip_name']
            work_trips = work_trips.filter(WorkTrip.trip_name.ilike('%{}%'.format(trip_name)))
        if 'trip_date_start' in params:
            trip_date_start = params['trip_date_start']
            work_trips = work_trips.filter(WorkTrip.trip_date >= trip_date_start)
        if 'trip_date_end' in params:
            trip_date_end = params['trip_date_end']
            work_trips = work_trips.filter(WorkTrip.trip_date <= trip_date_end)
        if 'leadership_positions_id' in params:
            leadership_positions_id = params['leadership_positions_id']
            work_trips = work_trips.filter(WorkTrip.leadership_positions_id == leadership_positions_id)
        if 'escort_officer' in params:
            escort_officer = params['escort_officer']
            work_trips = work_trips.filter(WorkTrip.escort_officer.ilike('%{}%'.format(escort_officer)))
        if 'have_protocol' in params:
            if not params['have_protocol']:
                work_trips = work_trips.filter(WorkTrip.protocol_id == None)
            else:
                work_trips = work_trips.filter(WorkTrip.protocol_id != None)

                if 'protocol_date_start' in params:
                    protocol_date_start = params['protocol_date_start']
                    work_trips = work_trips.filter(Protocol.protocol_date >= protocol_date_start)
                if 'protocol_date_end' in params:
                    protocol_date_end = params['protocol_date_end']
                    work_trips = work_trips.filter(Protocol.protocol_date <= protocol_date_end)
                if 'protocol_num' in params:
                    protocol_num = params['protocol_num']
                    work_trips = work_trips.filter(Protocol.protocol_num.ilike('%{}%'.format(protocol_num)))

        if 'project_code' in params:
            project_code = params['project_code']
            work_trips = work_trips.filter(Construction.project_code.ilike('%{}%'.format(project_code)))
        if 'is_critical' in params:
            if params['is_critical']:
                work_trips = work_trips.filter(Construction.is_critical == True)
            else:
                work_trips = work_trips.filter(Construction.is_critical != True)
        if 'fias_subject' in params:
            # TODO: rework with MKSBRYANS-205
            pass

        return work_trips.order_by(WorkTrip.trip_date).all()
