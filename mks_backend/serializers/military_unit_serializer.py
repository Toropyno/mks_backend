from mks_backend.errors.serilize_error import serialize_error_handler


class MilitaryUnitSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, military_unit):
        return {
            'id': military_unit.idMU,
            'fullName': military_unit.vChNumber,
        }

    def convert_list_to_json(self, military_units):
        return list(map(self.convert_object_to_json, military_units))
