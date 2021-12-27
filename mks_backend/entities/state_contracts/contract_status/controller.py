from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import ContractStatusSchema
from .serializer import ContractStatusSerializer
from .service import ContractStatusService


@view_defaults(renderer='json')
class ContractStatusController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ContractStatusService()
        self.serializer = ContractStatusSerializer()
        self.schema = ContractStatusSchema()

    @view_config(route_name='get_all_contract_statuses')
    def get_all_contract_statuses(self):
        contract_statuses = self.service.get_all_contract_statuses()
        return self.serializer.convert_list_to_json(contract_statuses)

    @view_config(route_name='add_contract_status')
    def add_contract_status(self):
        contract_status_deserialized = self.schema.deserialize(self.request.json_body)
        contract_status = self.serializer.convert_schema_to_object(contract_status_deserialized)
        self.service.add_contract_status(contract_status)
        return {'id': contract_status.contract_statuses_id}

    @view_config(route_name='delete_contract_status')
    def delete_contract_status(self):
        id = self.get_id()
        self.service.delete_contract_status_by_id(id)
        return {'id': id}

    @view_config(route_name='edit_contract_status')
    def edit_contract_status(self):
        contract_status_deserialized = self.schema.deserialize(self.request.json_body)
        contract_status_deserialized['id'] = self.get_id()
        new_contract_status = self.serializer.convert_schema_to_object(contract_status_deserialized)
        self.service.update_contract_status(new_contract_status)
        return {'id': new_contract_status.contract_statuses_id}

    @view_config(route_name='get_contract_status')
    def get_contract_status(self):
        id = self.get_id()
        contract_status = self.service.get_contract_status_by_id(id)
        return self.serializer.to_json(contract_status)

    def get_id(self):
        return int(self.request.matchdict['id'])
