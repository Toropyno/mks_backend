from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.controllers.schemas.zone import ZoneSchema
from mks_backend.serializers.zone import ZoneSerializer
from mks_backend.services.zone import ZoneService


@view_defaults(renderer='json')
class ZoneController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ZoneService()
        self.serializer = ZoneSerializer()
        self.schema = ZoneSchema()

    @view_config(route_name='get_all_zones')
    def get_all_zones(self):
        zones = self.service.get_all_zones()
        return self.serializer.convert_list_to_json(zones)

    @view_config(route_name='add_zone')
    def add_zone(self):
        zone_deserialized = self.schema.deserialize(self.request.json_body)
        zone = self.service.convert_schema_to_object(zone_deserialized)

        self.service.add_zone(zone)
        return {'id': zone.zones_id}

    @view_config(route_name='get_zone')
    def get_zone(self):
        id = self.get_id()
        zone = self.service.get_zone_by_id(id)
        return self.serializer.convert_object_to_json(zone)

    @view_config(route_name='delete_zone')
    def delete_zone(self):
        id = self.get_id()
        self.service.delete_zone_by_id(id)
        return {'id': id}

    @view_config(route_name='edit_zone')
    def edit_zone(self):
        id = self.get_id()
        zone_deserialized = self.schema.deserialize(self.request.json_body)
        zone_deserialized['id'] = id

        zone = self.service.convert_schema_to_object(zone_deserialized)
        self.service.update_zone(zone)
        return {'id': id}

    def get_id(self):
        return int(self.request.matchdict['id'])
