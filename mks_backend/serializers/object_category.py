from mks_backend.errors import serialize_error_handler
from mks_backend.models.object_category import ObjectCategory


class ObjectCategorySerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, object_category: ObjectCategory) -> dict:
        return {
            'id': object_category.object_categories_id,
            'fullName': object_category.fullname,
            'note': object_category.note,
        }

    def convert_list_to_json(self, object_categories: list) -> list:
        return list(map(self.convert_object_to_json, object_categories))

    def convert_schema_to_object(self, schema: dict) -> ObjectCategory:
        object_category = ObjectCategory()
        if 'id' in schema:
            object_category.object_categories_id = schema['id']

        object_category.fullname = schema['fullName']
        object_category.note = schema['note']
        return object_category
