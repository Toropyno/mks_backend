from mks_backend.models.object_category_list import ObjectCategoryList


class ObjectCategoryListSerializer:

    def convert_object_to_json(self, object_categories_list: ObjectCategoryList) -> dict:
        return {
            'id': object_categories_list.object_categories_list_id,
            'zone': object_categories_list.zones_id,
            'category': object_categories_list.object_categories_id
        }

    def convert_list_to_json(self, object_categories_lists: list) -> list:
        return list(map(self.convert_object_to_json, object_categories_lists))
