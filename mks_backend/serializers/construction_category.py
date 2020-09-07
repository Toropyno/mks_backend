from mks_backend.models.construction_category import ConstructionCategory

from mks_backend.serializers.construction_subcategory import ConstructionSubcategorySerializer

from mks_backend.errors.serilize_error import serialize_error_handler


class ConstructionCategorySerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, construction_category: ConstructionCategory) -> dict:
        construction_category_dict = {
            'id': construction_category.construction_categories_id,
            'fullName': construction_category.fullname,

            'subcategory': [
                ConstructionSubcategorySerializer.convert_object_to_json(subcategory.construction_subcategory)
                for subcategory in construction_category.subcategories_list
            ],
        }
        return construction_category_dict

    def convert_list_to_json(self, construction_categories_list: list) -> list:
        return list(map(self.convert_object_to_json, construction_categories_list))

    def convert_schema_to_object(self, schema: dict) -> ConstructionCategory:
        construction_categories = ConstructionCategory()

        construction_categories.construction_categories_id = schema.get('id')
        construction_categories.fullname = schema.get('fullName')

        return construction_categories
