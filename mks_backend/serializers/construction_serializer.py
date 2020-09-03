from mks_backend.models.construction import Construction
from mks_backend.serializers.commision_serializer import CommissionSerializer
from mks_backend.serializers.construction_category_serializer import ConstructionCategoriesSerializer
from mks_backend.serializers.construction_subcategory_serializer import ConstructionSubcategoriesSerializer
from mks_backend.serializers.military_unit_serializer import MilitaryUnitSerializer


class ConstructionSerializer:

    def convert_object_to_json(self, construction):
        # return with all subcategories
        category = ConstructionCategoriesSerializer.convert_object_to_json(construction.construction_categories)

        if construction.subcategories_list:
            construction_subcategory = ConstructionSubcategoriesSerializer.convert_object_to_json(
                construction.subcategories_list.construction_subcategory
            )
            subcategory = {
                'id': construction.subcategories_list.subcategories_list_id,
                'fullName': construction_subcategory['fullName'],
            }
        else:
            subcategory = None

        commission = CommissionSerializer.convert_object_to_json(construction.commission)
        military_unit = MilitaryUnitSerializer.convert_object_to_json(construction.military_unit)

        return {
            'id': construction.construction_id,
            'code': construction.project_code,
            'name': construction.project_name,
            'category': category,
            'subcategory': subcategory,
            'isCritical': construction.is_critical,
            'commission': commission,
            'militaryUnit': military_unit,
            'contractDate': self.get_date_string(construction.contract_date),
            'objectsAmount': construction.object_amount,
            'plannedDate': self.get_date_string(construction.planned_date),
        }

    def convert_list_to_json(self, constructions):
        return list(map(self.convert_object_to_json, constructions))

    def get_date_string(self, date):
        return str(date.year) + ',' + str(date.month) + ',' + str(date.day)

    def convert_schema_to_object(self, schema):
        construction = Construction()

        construction.construction_id = schema.get('id')
        construction.project_code = schema.get('code')
        construction.project_name = schema.get('name')
        construction.construction_categories_id = schema.get('category')
        construction.subcategories_list_id = schema.get('subcategory')
        construction.is_critical = schema.get('isCritical')
        construction.commission_id = schema.get('commission')
        construction.idMU = schema.get('militaryUnit')
        construction.contract_date = schema.get('contractDate')
        construction.planned_date = schema.get('plannedDate')
        construction.object_amount = schema.get('objectsAmount')

        return construction
