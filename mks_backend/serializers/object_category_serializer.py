from mks_backend.models.object_categories import ObjectCategories

class ObjectCategorySerializer:

    def convert_object_to_json(self, object_category):
        object_category_dict = {
            'id': object_category.object_categories_id,
            'fullName': object_category.fullname,
            'note': object_category.note,
        }
        return object_category_dict

    def convert_list_to_json(self, object_categories):
        return list(map(self.convert_object_to_json, object_categories))

    def convert_schema_to_object(self, schema):
        object_category = ObjectCategories()

        return object_category
