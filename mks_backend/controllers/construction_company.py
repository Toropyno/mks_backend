from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.controllers.schemas.construction_company import ConstructionCompanySchema
from mks_backend.serializers.construction_company import ConstructionCompanySerializer
from mks_backend.services.construction_company import ConstructionCompanyService

from mks_backend.errors import handle_colander_error, handle_db_error


@view_defaults(renderer='json')
class ConstructionCompanyController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ConstructionCompanyService()
        self.serializer = ConstructionCompanySerializer()
        self.schema = ConstructionCompanySchema()

    @view_config(route_name='get_all_construction_companies')
    def get_all_construction_companies(self):
        construction_companies = self.service.get_all_construction_companies()
        return self.serializer.convert_list_to_json(construction_companies)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_construction_company')
    def add_construction_company(self):
        construction_company_deserialized = self.schema.deserialize(self.request.json_body)

        construction_company = self.serializer.convert_schema_to_object(construction_company_deserialized)
        self.service.add_construction_company(construction_company)
        return {'id': construction_company.construction_companies_id}

    @view_config(route_name='delete_construction_company')
    def delete_construction_company(self):
        id = self.get_id()
        self.service.delete_construction_company_by_id(id)
        return {'id': id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_construction_company')
    def edit_construction_company(self):
        construction_company_deserialized = self.schema.deserialize(self.request.json_body)
        construction_company_deserialized['id'] = self.get_id()

        new_construction_company = self.serializer.convert_schema_to_object(construction_company_deserialized)
        self.service.update_construction_company(new_construction_company)
        return {'id': new_construction_company.construction_companies_id}

    @view_config(route_name='get_construction_company')
    def get_construction_company(self):
        id = self.get_id()
        construction_company = self.service.get_construction_company_by_id(id)
        return self.serializer.convert_object_to_json(construction_company)

    def get_id(self):
        return int(self.request.matchdict['id'])
