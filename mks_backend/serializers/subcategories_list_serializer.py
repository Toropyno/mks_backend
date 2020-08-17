class SubcategoriesListSerializer:

    def convert_object_to_json(self, subcategories_list):
        subcategories_list_dict = {
            'id': subcategories_list.subcategories_list_id,
            'constructionCategoriesId': subcategories_list.construction_categories_id,
            'constructionSubcategoriesId': subcategories_list.construction_subcategories_id
        }
        return subcategories_list_dict

    def convert_list_to_json(self, subcategories_list_list):
        return list(map(self.convert_object_to_json, subcategories_list_list))
