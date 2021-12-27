from .model import ConstructionCategory

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.entities.constructions.construction_subcategory import ConstructionSubcategorySerializer
from mks_backend.errors import serialize_error_handler


class ConstructionCategorySerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, construction_category: ConstructionCategory) -> dict:
        return {
            'id': construction_category.construction_categories_id,
            'fullName': construction_category.fullname,
            'subcategory': [
                ConstructionSubcategorySerializer.to_json(subcategory)
                for subcategory in construction_category.subcategories
            ],
        }

    @classmethod
    @serialize_error_handler
    def to_short_json(cls, construction_category: ConstructionCategory) -> dict:
        return {
            'id': construction_category.construction_categories_id,
            'fullName': construction_category.fullname
        }
