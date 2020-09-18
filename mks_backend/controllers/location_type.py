import colander
from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config, view_defaults

from mks_backend.controllers.schemas.location_type import LocationTypeSchema
from mks_backend.errors.colander_error import get_collander_error_dict
from mks_backend.errors.db_basic_error import DBBasicError
from mks_backend.serializers.location_type import LocationTypeSerializer
from mks_backend.services.location_type import LocationTypeService


@view_defaults(renderer='json')
class LocationTypeController:

    def __init__(self, request: Request):
        self.request = request
        self.service = LocationTypeService()
        self.serializer = LocationTypeSerializer()
        self.schema = LocationTypeSchema()

    @view_config(route_name='get_all_location_types')
    def get_all_location_types(self):
        location_types = self.service.get_all_location_types()
        return self.serializer.convert_list_to_json(location_types)

    @view_config(route_name='add_location_type')
    def add_location_type(self):
        try:
            location_type_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=get_collander_error_dict(error.asdict()))

        location_type = self.serializer.convert_schema_to_object(location_type_deserialized)
        try:
            self.service.add_location_type(location_type)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': location_type.location_types_id}

    @view_config(route_name='delete_location_type')
    def delete_location_type(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_location_type_by_id(id)
        return {'id': id}

    @view_config(route_name='edit_location_type')
    def edit_location_type(self):
        try:
            location_type_deserialized = self.schema.deserialize(self.request.json_body)
            location_type_deserialized['id'] = self.request.matchdict['id']
        except colander.Invalid as error:
            return Response(status=403, json_body=get_collander_error_dict(error.asdict()))

        new_location_type = self.serializer.convert_schema_to_object(location_type_deserialized)
        try:
            self.service.update_location_type(new_location_type)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': new_location_type.location_types_id}

    @view_config(route_name='get_location_type')
    def get_location_type(self):
        id = int(self.request.matchdict['id'])
        location_type = self.service.get_location_type_by_id(id)
        return self.serializer.convert_object_to_json(location_type)
