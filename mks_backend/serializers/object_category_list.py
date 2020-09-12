from mks_backend.models.object_category_list import ObjectCategoryList


class ObjectCategoryListSerializer:

    def convert_object_to_json(self, object_categories_list: ObjectCategoryList) -> dict:
        object_categories_list_dict = {
            'id': object_categories_list.object_categories_list_id,
            'zone': object_categories_list.zone.zones_id,
            'category': object_categories_list.object_category.object_categories_id
        }
        return object_categories_list_dict

    def convert_list_to_json(self, object_categories_lists: list) -> list:
        return list(map(self.convert_object_to_json, object_categories_lists))

    def convert_schema_to_object(self, schema: dict) -> ObjectCategoryList:
        object_categories_list = ObjectCategoryList()
        if 'id' in schema:
            object_categories_list.object_categories_list_id = schema['id']

        object_categories_list.zones_id = schema['zone']
        object_categories_list.object_categories_id = schema['category']
        return object_categories_list
