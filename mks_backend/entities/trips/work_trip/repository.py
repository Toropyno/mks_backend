from .model import WorkTrip

from mks_backend.entities.fias import FIAS
from mks_backend.entities.protocols.protocol import Protocol
from mks_backend.entities.constructions.construction import Construction
from mks_backend.entities.trips.visited_object import VisitedObject

from mks_backend.session import DBSession


class WorkTripRepository:

    def __init__(self):
        self._query = DBSession.query(WorkTrip)

    def get_all_work_trips(self) -> list:
        return self._query.all()

    def add_work_trip(self, work_trip: WorkTrip) -> None:
        DBSession.add(work_trip)
        DBSession.commit()

    def delete_work_trip_by_id(self, id: int) -> None:
        self._query.filter(WorkTrip.work_trips_id == id).delete()
        DBSession.commit()

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
        work_trips = self._query \
            .outerjoin(VisitedObject, Construction) \
            .outerjoin(Protocol).outerjoin(FIAS)

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
                work_trips = work_trips.filter(WorkTrip.protocol_id.is_(None))
            else:
                work_trips = work_trips.filter(WorkTrip.protocol_id.isnot(None))

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
                work_trips = work_trips.filter(Construction.is_critical.is_(True))
            else:
                work_trips = work_trips.filter(Construction.is_critical.isnot(True))
        if 'region' in params:
            work_trips = work_trips.filter(FIAS.region.ilike('%' + params['region'] + '%'))

        return work_trips.order_by(WorkTrip.trip_date).all()
