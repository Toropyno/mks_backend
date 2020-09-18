from mks_backend.errors.serilize_error import serialize_error_handler
from mks_backend.models.construction_category import ConstructionCategory
from mks_backend.serializers.construction_subcategory import ConstructionSubcategorySerializer


class ConstructionCategorySerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, construction_category: ConstructionCategory) -> dict:
        construction_category_dict = {
            'id': construction_category.construction_categories_id,
            'fullName': construction_category.fullname,

            'subcategory': [
                ConstructionSubcategorySerializer.convert_object_to_json(subcategory)
                for subcategory in construction_category.subcategories
            ],
        }
        return construction_category_dict

    def convert_list_to_json(self, construction_categories_list: list) -> list:
        return list(map(self.convert_object_to_json, construction_categories_list))
