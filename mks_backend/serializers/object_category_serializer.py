from mks_backend.models.object_categories import ObjectCategories

from mks_backend.errors.serilize_error import serialize_error_handler


class ObjectCategorySerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, object_category: ObjectCategories) -> dict:
        object_category_dict = {
            'id': object_category.object_categories_id,
            'fullName': object_category.fullname,
            'note': object_category.note,
        }
        return object_category_dict

    def convert_list_to_json(self, object_categories: list) -> list:
        return list(map(self.convert_object_to_json, object_categories))

    def convert_schema_to_object(self, schema: dict) -> ObjectCategories:
        object_category = ObjectCategories()
        if 'id' in schema:
            object_category.object_categories_id = schema['id']

        object_category.fullname = schema['fullName']
        object_category.note = schema['note']
        return object_category
