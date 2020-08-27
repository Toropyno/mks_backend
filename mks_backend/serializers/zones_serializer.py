from mks_backend.models.zones import Zones

from mks_backend.errors.serilize_error import serialize_error_handler


class ZoneSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, zone):
        zone_dict = {
            'id': zone.zones_id,
            'fullName': zone.fullname,
        }
        return zone_dict

    def convert_list_to_json(self, zones):
        return list(map(self.convert_object_to_json, zones))

    def convert_schema_to_object(self, schema):
        zone = Zones()
        if 'id' in schema:
            zone.zones_id = schema['id']

        zone.fullname = schema['fullName']
        return zone