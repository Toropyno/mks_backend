from mks_backend.models.construction_categories import ConstructionCategories


class ConstructionCategoriesSerializer:

    def convert_object_to_json(self, construction_category):
        construction_category_dict = {
            'id': construction_category.construction_categories_id,
            'fullName': construction_category.fullname
        }
        return construction_category_dict

    def convert_list_to_json(self, construction_categories_list):
        return list(map(self.convert_object_to_json, construction_categories_list))

    def convert_schema_to_object(self, schema):
        construction_categories = ConstructionCategories()

        construction_categories.construction_categories_id = schema.get('id')
        construction_categories.fullname = schema.get('fullName')

        return construction_categories
