from mks_backend.models.trips.work_trip import WorkTrip

from mks_backend.serializers.utils.date_and_time import get_date_string
from mks_backend.serializers.trips.leadership_position import LeadershipPositionSerializer
from mks_backend.serializers.protocols.protocol import ProtocolSerializer


class WorkTripSerializer:

    def to_json(self, work_trip: WorkTrip) -> dict:
        return {
            'id': work_trip.work_trips_id,
            'date': get_date_string(work_trip.trip_date),
            'name': work_trip.trip_name,
            'escortOfficer': work_trip.escort_officer,
            'leadershipPosition': LeadershipPositionSerializer.to_json(
                work_trip.leadership_position
            ),
            'protocol': ProtocolSerializer.convert_object_to_json(
                work_trip.protocol
            )
        }

    def convert_list_to_json(self, work_trips: list) -> list:
        return list(map(self.to_json, work_trips))

    def convert_schema_to_object(self, schema: dict) -> WorkTrip:
        work_trip = WorkTrip()

        work_trip.work_trips_id = schema.get('id')
        work_trip.trip_date = schema.get('date')
        work_trip.trip_name = schema.get('name')
        work_trip.escort_officer = schema.get('escortOfficer')
        work_trip.leadership_positions_id = schema.get('leadershipPosition')
        work_trip.protocol_id = schema.get('protocol')

        return work_trip
