from .model import ObjectCategoryList

from mks_backend.entities.BASE.serializer import BaseSerializer


class ObjectCategoryListSerializer(BaseSerializer):

    def to_json(self, object_categories_list: ObjectCategoryList) -> dict:
        return {
            'id': object_categories_list.object_categories_list_id,
            'zone': object_categories_list.zones_id,
            'category': object_categories_list.object_categories_id
        }
