class ConstructionCategoriesSerializer:

    def convert_object_to_json(self, construction_category):
        construction_category_dict = {
            'id': construction_category.construction_categories_id,
            'fullName': construction_category.fullname,

            # id from SubcategoriesList.subcategories_list_id, fullName from ConstructionSubcategories.fullname
            'subcategory': {
                'id': construction_category.subcategories_list[0].subcategories_list_id,
                'fullname': construction_category.subcategories_list[0].construction_subcategory.fullname
            }
            # end of shit
        }
        return construction_category_dict

    def convert_list_to_json(self, construction_categories_list):
        return list(map(self.convert_object_to_json, construction_categories_list))
