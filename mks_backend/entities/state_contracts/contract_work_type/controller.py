from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .serializer import ContractWorkTypeSerializer
from .service import ContractWorkTypeService
from .schema import ContractWorkTypeSchema


@view_defaults(renderer='json')
class ContractWorkTypeController:

    def __init__(self, request: Request):
        self.request = request
        self.schema = ContractWorkTypeSchema()
        self.service = ContractWorkTypeService()
        self.serializer = ContractWorkTypeSerializer()

    @view_config(route_name='add_contract_work_type')
    def add(self):
        contract_w_t_deserialized = self.schema.deserialize(self.request.json_body)
        contract_w_t = self.serializer.to_mapped_object(contract_w_t_deserialized)

        self.service.add(contract_w_t)
        return {'id': contract_w_t.contract_worktypes_id}

    @view_config(route_name='edit_contract_work_type')
    def edit(self):
        id = self.get_id()
        contract_w_t_deserialized = self.schema.deserialize(self.request.json_body)
        contract_w_t_deserialized['id'] = id
        contract_w_t = self.serializer.to_mapped_object(contract_w_t_deserialized)

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

    @view_config(route_name='delete_contract_work_type')
    def delete(self):
        id = self.get_id()
        self.service.delete_by_id(id)
        return {'id': id}

    def get_id(self):
        return int(self.request.matchdict['id'])
