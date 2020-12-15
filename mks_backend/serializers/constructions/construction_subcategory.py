from mks_backend.errors import serialize_error_handler
from mks_backend.models.constructions import ConstructionSubcategory


class ConstructionSubcategorySerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, construction_subcategory: ConstructionSubcategory) -> dict:
        return {
            'id': construction_subcategory.construction_subcategories_id,
            'fullName': construction_subcategory.fullname
        }

    def convert_list_to_json(self, construction_subcategories_list: list) -> list:
        return list(map(self.convert_object_to_json, construction_subcategories_list))

    def convert_schema_to_object(self, schema: dict) -> ConstructionSubcategory:
        construction_subcategories = ConstructionSubcategory()

        construction_subcategories.construction_subcategories_id = schema.get('id')
        construction_subcategories.fullname = schema.get('fullName')

        return construction_subcategories
