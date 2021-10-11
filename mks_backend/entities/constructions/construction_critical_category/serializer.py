from mks_backend.errors import serialize_error_handler
from .model import ConstructionCriticalCategory


class ConstructionCriticalCategorySerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, construction_critical_category: ConstructionCriticalCategory) -> dict:
        return {
            'id': construction_critical_category.construction_critical_categories_id,
            'fullName': construction_critical_category.fullname,
        }

    def convert_schema_to_object(self, schema: dict) -> ConstructionCriticalCategory:
        construction_critical_category = ConstructionCriticalCategory()

        construction_critical_category.construction_critical_categories_id = schema.get('id')
        construction_critical_category.fullname = schema.get('fullName')

        return construction_critical_category

    def convert_list_to_json(self, construction_critical_categories_list: list) -> list:
        return list(map(self.convert_object_to_json, construction_critical_categories_list))


