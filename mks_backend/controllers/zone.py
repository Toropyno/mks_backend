import colander
from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

from mks_backend.controllers.schemas.zone import ZoneSchema
from mks_backend.errors.colander_error import get_collander_error_dict
from mks_backend.errors.db_basic_error import DBBasicError
from mks_backend.serializers.zone import ZoneSerializer
from mks_backend.services.zone import ZoneService


class ZoneController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ZoneService()
        self.serializer = ZoneSerializer()
        self.schema = ZoneSchema()

    @view_config(route_name='get_all_zones', renderer='json')
    def get_all_zones(self):
        zones = self.service.get_all_zones()
        return self.serializer.convert_list_to_json(zones)

    @view_config(route_name='add_zone', renderer='json')
    def add_zone(self):
        try:
            zone_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=get_collander_error_dict(error.asdict()))
        zone = self.service.convert_schema_to_object(zone_deserialized)
        try:
            self.service.add_zone(zone)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': zone.zones_id}

    @view_config(route_name='get_zone', renderer='json')
    def get_zone(self):
        id = self.get_id()
        zone = self.service.get_zone_by_id(id)
        return self.serializer.convert_object_to_json(zone)

    @view_config(route_name='delete_zone', renderer='json')
    def delete_zone(self):
        id = self.get_id()
        self.service.delete_zone_by_id(id)
        return {'id': id}

    @view_config(route_name='edit_zone', renderer='json')
    def edit_zone(self):
        id = self.get_id()
        try:
            zone_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=get_collander_error_dict(error.asdict()))
        zone_deserialized['id'] = id
        zone = self.service.convert_schema_to_object(zone_deserialized)
        try:
            self.service.update_zone(zone)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': id}

    def get_id(self):
        return int(self.request.matchdict['id'])
