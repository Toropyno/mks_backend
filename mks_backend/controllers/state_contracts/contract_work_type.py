from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.serializers.state_contracts.contract_work_type import ContractWorkTypeSerializer
from mks_backend.services.state_contracts.contract_work_type import ContractWorkTypeService
from mks_backend.controllers.schemas.state_contracts.contract_work_type import ContractWorkTypeSchema

from mks_backend.errors.handle_controller_error import handle_colander_error, handle_db_error


@view_defaults(renderer='json')
class ContractWorkTypeController:

    def __init__(self, request: Request):
        self.request = request
        self.schema = ContractWorkTypeSchema()
        self.service = ContractWorkTypeService()
        self.serializer = ContractWorkTypeSerializer()

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_contract_work_type')
    def add(self):
        contract_w_t_deserialized = self.schema.deserialize(self.request.json_body)
        contract_w_t = self.service.to_object(contract_w_t_deserialized)

        self.service.add(contract_w_t)
        return {'id': contract_w_t.contract_work_types_id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_contract_work_type')
    def edit(self):
        id = self.get_id()
        contract_w_t_deserialized = self.schema.deserialize(self.request.json_body)
        contract_w_t_deserialized['id'] = id

        contract_w_t = self.service.to_object(contract_w_t_deserialized)
        self.service.update(contract_w_t)
        return {'id': id}

    @view_config(route_name='get_all_contract_work_types')
    def get_all(self):
        contract_work_types = self.service.get_all()
        return self.serializer.list_to_json(contract_work_types)

    @view_config(route_name='get_contract_work_type')
    def get(self):
        id = self.get_id()
        contract_w_t = self.service.get_by_id(id)
        return self.serializer.to_json(contract_w_t)

    @handle_db_error
    @view_config(route_name='delete_contract_work_type')
    def delete(self):
        id = self.get_id()
        self.service.delete_by_id(id)
        return {'id': id}

    def get_id(self):
        return int(self.request.matchdict['id'])
