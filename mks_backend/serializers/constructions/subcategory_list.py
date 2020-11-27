from mks_backend.models.constructions import SubcategoryList


class SubcategoryListSerializer:

    def convert_object_to_json(self, subcategories_list: SubcategoryList) -> dict:
        return {
            'id': subcategories_list.subcategories_list_id,
            'constructionCategoriesId': subcategories_list.construction_categories_id,
            'constructionSubcategoriesId': subcategories_list.construction_subcategories_id
        }

    def convert_list_to_json(self, subcategories_list_list: list) -> list:
        return list(map(self.convert_object_to_json, subcategories_list_list))
