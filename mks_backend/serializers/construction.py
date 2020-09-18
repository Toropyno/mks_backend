from datetime import date as Date

from mks_backend.models.construction import Construction
from mks_backend.serializers.commision import CommissionSerializer
from mks_backend.serializers.construction_category import ConstructionCategorySerializer
from mks_backend.serializers.construction_subcategory import ConstructionSubcategorySerializer
from mks_backend.serializers.location import LocationSerializer
from mks_backend.serializers.military_unit import MilitaryUnitSerializer


class ConstructionSerializer:

    def convert_object_to_json(self, construction: Construction) -> dict:
        # return with all subcategories
        category = ConstructionCategorySerializer.convert_object_to_json(
            construction.construction_category
        )

        if construction.subcategories_list:
            subcategory = ConstructionSubcategorySerializer.convert_object_to_json(
                construction.subcategories_list.subcategory
            )
        else:
            subcategory = None

        commission = CommissionSerializer.convert_object_to_json(construction.commission)
        military_unit = MilitaryUnitSerializer.convert_object_to_json(construction.military_unit)

        location = LocationSerializer.convert_object_to_json(construction.location)

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
            'constructionType': {
                'id': 1,
                'fullName': 'Наименование типа проекта'
            },
            'locationType': {
                'id': 1,
                'fullName': 'Наименование типа местоположения'
            },
            'constructionCompany': {
                'id': 1,
                'fullName': 'Название компании-исполнителя'
            },
            'oksm': {
                'id': 1,
                'fullName': 'Краткое наименование страны по ОКСМ'
            },
            'fias': {
                'subject': {
                    'id': 1,
                    'fullName': 'Название субъекта по ФИАС'
                },
                'district': {
                    'id': 11,
                    'fullName': 'Название района по ФИАС'
                },
                'city': {
                    'id': 17,
                    'fullName': 'Наименование города по ФИАС'
                },
                'locality': {
                    'id': 1,
                    'fullName': 'Наименование населенного пункта по ФИАС'
                }
            },
            'address': 'Не формализованный адрес проекта',
            'note': 'Примечание к проекту',
            'location': location,
        }

    def convert_list_to_json(self, constructions: list) -> list:
        return list(map(self.convert_object_to_json, constructions))

    def get_date_string(self, date: Date) -> str:
        return str(date.year) + ',' + str(date.month) + ',' + str(date.day)
