from mks_backend.models.construction_subcategories import ConstructionSubcategories

from mks_backend.errors.serilize_error import serialize_error_handler


class ConstructionSubcategoriesSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, construction_subcategory):
        construction_subcategory_dict = {
            'id': construction_subcategory.construction_subcategories_id,
            'fullName': construction_subcategory.fullname
        }
        return construction_subcategory_dict

    def convert_list_to_json(self, construction_subcategories_list):
        return list(map(self.convert_object_to_json, construction_subcategories_list))

    def convert_schema_to_object(self, schema):
        construction_subcategories = ConstructionSubcategories()

        construction_subcategories.construction_subcategories_id = schema.get('id')
        construction_subcategories.fullname = schema.get('fullName')

        return construction_subcategories
