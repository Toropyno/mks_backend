from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler

from .model import ObjectCategory


class ObjectCategorySerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, object_category: ObjectCategory) -> dict:
        return {
            'id': object_category.object_categories_id,
            'fullName': object_category.fullname,
            'note': object_category.note,
        }

    def to_mapped_object(self, schema: dict) -> ObjectCategory:
        object_category = ObjectCategory()
        if 'id' in schema:
            object_category.object_categories_id = schema['id']

        object_category.fullname = schema['fullName']
        object_category.note = schema['note']
        return object_category
