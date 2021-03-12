from mks_backend.models.construction_objects.realty_type import RealtyType

from mks_backend.errors import serialize_error_handler


class RealtyTypeSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, realty_type: RealtyType) -> dict:
        return {
            'id': realty_type.realty_types_id,
            'fullName': realty_type.fullname
        }

    def convert_list_to_json(self, realty_types: list) -> list:
        return list(map(self.convert_object_to_json, realty_types))

    def convert_schema_to_object(self, schema: dict) -> RealtyType:
        realty_type = RealtyType()

        realty_type.realty_types_id = schema.get('id')
        realty_type.fullname = schema.get('fullName')

        return realty_type
