from .model import ConstructionSubcategory

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler


class ConstructionSubcategorySerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, construction_subcategory: ConstructionSubcategory) -> dict:
        return {
            'id': construction_subcategory.construction_subcategories_id,
            'fullName': construction_subcategory.fullname
        }

    def convert_schema_to_object(self, schema: dict) -> ConstructionSubcategory:
        construction_subcategories = ConstructionSubcategory()

        construction_subcategories.construction_subcategories_id = schema.get('id')
        construction_subcategories.fullname = schema.get('fullName')

        return construction_subcategories
