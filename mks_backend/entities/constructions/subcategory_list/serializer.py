from .model import SubcategoryList

from mks_backend.entities.BASE.serializer import BaseSerializer


class SubcategoryListSerializer(BaseSerializer):

    def to_json(self, subcategories_list: SubcategoryList) -> dict:
        return {
            'id': subcategories_list.subcategories_list_id,
            'constructionCategoriesId': subcategories_list.construction_categories_id,
            'constructionSubcategoriesId': subcategories_list.construction_subcategories_id
        }
