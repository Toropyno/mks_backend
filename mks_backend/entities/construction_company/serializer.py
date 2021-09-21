from .model import ConstructionCompany

from mks_backend.errors import serialize_error_handler


class ConstructionCompanySerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, construction_company: ConstructionCompany) -> dict:
        return {
            'id': construction_company.construction_companies_id,
            'shortName': construction_company.shortname,
            'fullName': construction_company.fullname,
            'addressFull': construction_company.address_full,
            'phone': construction_company.phone,
            'email': construction_company.email,
            'people': construction_company.people,
            'equipment': construction_company.equipment,
            'services': construction_company.services,
            'fias': construction_company.fias,
        }

    def convert_list_to_json(self, construction_companys: list) -> list:
        return list(map(self.convert_object_to_json, construction_companys))

    def convert_schema_to_object(self, schema: dict) -> ConstructionCompany:
        construction_company = ConstructionCompany()

        construction_company.construction_companies_id = schema.get('id')
        construction_company.shortname = schema.get('shortName')
        construction_company.fullname = schema.get('fullName')

        return construction_company
