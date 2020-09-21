from mks_backend.models.construction_company import ConstructionCompany

from mks_backend.errors.serilize_error import serialize_error_handler


class ConstructionCompanySerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, construction_company: ConstructionCompany) -> dict:
        return {
            'id': construction_company.construction_companies_id,
            'shortName': construction_company.shortname,
            'fullName': construction_company.fullname
        }

    def convert_list_to_json(self, construction_companys: list) -> list:
        return list(map(self.convert_object_to_json, construction_companys))

    def convert_schema_to_object(self, schema: dict) -> ConstructionCompany:
        construction_company = ConstructionCompany()

        construction_company.construction_companies_id = schema.get('id')
        construction_company.shortname = schema.get('shortName')
        construction_company.fullname = schema.get('fullName')

        return construction_company
