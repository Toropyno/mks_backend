class MilitaryUnitSerializer:
    def convert_object_to_json(self, military_unit):
        return {
            'id': military_unit.pidMU,
            'fullName': military_unit.vChNumber,
        }

    def convert_list_to_json(self, military_units):
        return list(map(self.convert_object_to_json, military_units))
