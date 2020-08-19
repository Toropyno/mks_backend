import colander
from pyramid.view import view_config
from pyramid.response import Response

from mks_backend.services.zones_service import ZoneService
from mks_backend.serializers.zones_serializer import ZoneSerializer
from mks_backend.controllers.schemas.zones_schema import ZonesSchema


class ZonesController(object):

    def __init__(self, request):
        self.request = request
        self.service = ZoneService()
        self.serializer = ZoneSerializer()
        self.schema = ZonesSchema()

    @view_config(route_name='zones', request_method='GET', renderer='json')
    def get_all_zones(self):
        zones = self.service.get_all_zones()
        json = self.serializer.convert_list_to_json(zones)
        return json

    @view_config(route_name='add_zone', request_method='POST', renderer='json')
    def add_zone(self):
        try:
            zone_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        zone = self.serializer.convert_schema_to_object(zone_deserialized)
        try:
            self.service.add_zone(zone)
        except ValueError as error:
            return Response(status=403, json_body={'error': error.args[0]})

        return {'id': zone.zones_id}

    @view_config(route_name='zone_delete_change_and_view', request_method='GET', renderer='json')
    def get_zone(self):
        id = self.request.matchdict['id']
        zone = self.service.get_zone_by_id(id)
        json = self.serializer.convert_object_to_json(zone)
        return json

    @view_config(route_name='zone_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_zone(self):
        id = self.request.matchdict['id']
        self.service.delete_zone_by_id(id)
        return {'id': id}

    @view_config(route_name='zone_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_zone(self):
        id = self.request.matchdict['id']
        try:
            zone_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        zone_deserialized["id"] = id
        zone = self.serializer.convert_schema_to_object(zone_deserialized)
        try:
            self.service.update_zone(zone)
        except ValueError as error:
            return Response(status=403, json_body={'error': error.args[0]})

        return {'id': id}
