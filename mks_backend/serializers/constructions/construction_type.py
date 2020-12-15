from mks_backend.models.constructions import ConstructionType

from mks_backend.errors import serialize_error_handler


class ConstructionTypeSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, construction_type: ConstructionType) -> dict:
        return {
            'id': construction_type.construction_types_id,
            'fullName': construction_type.fullname
        }

    def convert_list_to_json(self, construction_types: list) -> list:
        return list(map(self.convert_object_to_json, construction_types))

    def convert_schema_to_object(self, schema: dict) -> ConstructionType:
        construction_type = ConstructionType()

        construction_type.construction_types_id = schema.get('id')
        construction_type.fullname = schema.get('fullName')

        return construction_type
