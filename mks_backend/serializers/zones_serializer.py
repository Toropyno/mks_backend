class ZoneSerializer:

    def convert_object_to_json(self, zone):
        zone_dict = {
            'id': zone.zones_id,
            'fullName': zone.fullname,
        }
        return zone_dict

    def convert_list_to_json(self, zones):
        return list(map(self.convert_object_to_json, zones))
