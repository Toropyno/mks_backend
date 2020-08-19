class ConstructionSubcategoriesSerializer:

    def convert_object_to_json(self, construction_subcategory):
        construction_subcategory_dict = {
            'id': construction_subcategory.construction_subcategories_id,
            'fullName': construction_subcategory.fullname
        }
        return construction_subcategory_dict

    def convert_list_to_json(self, construction_subcategories_list):
        return list(map(self.convert_object_to_json, construction_subcategories_list))
