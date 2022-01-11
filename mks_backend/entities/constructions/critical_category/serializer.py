from .model import CriticalCategory

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler


class CriticalCategorySerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, critical_category: CriticalCategory) -> dict:
        return {
            'id': critical_category.critical_categories_id,
            'fullName': critical_category.fullname,
        }

    def to_mapped_object(self, schema: dict) -> CriticalCategory:
        critical_category = CriticalCategory()

        critical_category.critical_categories_id = schema.get('id')
        critical_category.fullname = schema.get('fullName')

        return critical_category
