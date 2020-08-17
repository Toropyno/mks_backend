class ObjectCategorySerializer:

    def convert_object_to_json(self, object_category):
        object_category_dict = {
            'id': object_category.object_categories_id,
            'fullName': object_category.fullname,
            'note': object_category.note,
        }
        return object_category_dict

    def convert_list_to_json(self, object_categories):
        object_categories_array = []

        for object_category in object_categories:
            object_category_dict = self.convert_object_to_json(object_category)
            object_categories_array.append(object_category_dict)

        return object_categories_array
