from mks_backend.errors import serialize_error_handler
from .model import CriticalCategory


class CriticalCategorySerializer:

    @classmethod
    @serialize_error_handler
    def to_json(cls, critical_category: CriticalCategory) -> dict:
        return {
            'id': critical_category.critical_categories_id,
            'fullName': critical_category.fullname,
        }

    def to_object(self, schema: dict) -> CriticalCategory:
        critical_category = CriticalCategory()

        critical_category.critical_categories_id = schema.get('id')
        critical_category.fullname = schema.get('fullName')

        return critical_category

    def list_to_json(self, critical_category_list: list) -> list:
        return list(map(self.to_json, critical_category_list))
