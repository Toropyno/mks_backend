from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.controllers.schemas.trips.work_trip import WorkTripSchema, WorkTripFilterSchema
from mks_backend.serializers.trips.work_trip import WorkTripSerializer
from mks_backend.services.trips.work_trip import WorkTripService

from mks_backend.errors.handle_controller_error import handle_colander_error, handle_db_error


@view_defaults(renderer='json')
class WorkTripController:

    def __init__(self, request: Request):
        self.request = request
        self.service = WorkTripService()
        self.serializer = WorkTripSerializer()
        self.schema = WorkTripSchema()
        self.filter_schema = WorkTripFilterSchema()

    @handle_colander_error
    @view_config(route_name='get_all_work_trips')
    def get_all_work_trips(self):
        filter_params = self.filter_schema.deserialize(self.request.params)
        work_trips = self.service.get_work_trips(filter_params)
        return self.serializer.convert_list_to_json(work_trips)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_work_trip')
    def add_work_trip(self):
        work_trip_deserialized = self.schema.deserialize(self.request.json_body)

        work_trip = self.serializer.convert_schema_to_object(work_trip_deserialized)
        self.service.add_work_trip(work_trip)
        return {'id': work_trip.work_trips_id}

    @view_config(route_name='delete_work_trip')
    def delete_work_trip(self):
        id = self.get_id()
        self.service.delete_work_trip_by_id(id)
        return {'id': id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_work_trip')
    def edit_work_trip(self):
        work_trip_deserialized = self.schema.deserialize(self.request.json_body)
        work_trip_deserialized['id'] = self.get_id()

        new_work_trip = self.serializer.convert_schema_to_object(work_trip_deserialized)
        self.service.update_work_trip(new_work_trip)
        return {'id': new_work_trip.work_trips_id}

    @view_config(route_name='get_work_trip')
    def get_work_trip(self):
        id = self.get_id()
        work_trip = self.service.get_work_trip_by_id(id)
        return self.serializer.to_json(work_trip)

    def get_id(self) -> int:
        return int(self.request.matchdict['id'])
