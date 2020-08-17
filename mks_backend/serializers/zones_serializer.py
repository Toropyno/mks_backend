class ZoneSerializer:

    def convert_object_to_json(self, zone):
        zone_dict = {
            'id': zone.zones_id,
            'fullName': zone.fullname,
        }
        return zone_dict

    def convert_list_to_json(self, zones):
        zones_array = []

        for zone in zones:
            zone_dict = self.convert_object_to_json(zone)
            zones_array.append(zone_dict)

        return zones_array
