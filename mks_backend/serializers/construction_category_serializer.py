from mks_backend.models.construction_categories import ConstructionCategories

from mks_backend.serializers.construction_subcategory_serializer import ConstructionSubcategoriesSerializer

from mks_backend.errors.serilize_error import serialize_error_handler


class ConstructionCategoriesSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, construction_category: ConstructionCategories) -> dict:
        construction_category_dict = {
            'id': construction_category.construction_categories_id,
            'fullName': construction_category.fullname,

            'subcategory': [
                ConstructionSubcategoriesSerializer.convert_object_to_json(subcategory.construction_subcategory)
                for subcategory in construction_category.subcategories_list
            ],
        }
        return construction_category_dict

    def convert_list_to_json(self, construction_categories_list: list) -> list:
        return list(map(self.convert_object_to_json, construction_categories_list))

    def convert_schema_to_object(self, schema: dict) -> ConstructionCategories:
        construction_categories = ConstructionCategories()

        construction_categories.construction_categories_id = schema.get('id')
        construction_categories.fullname = schema.get('fullName')

        return construction_categories
