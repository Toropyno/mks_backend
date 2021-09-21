from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import ContractSchema
from .serializer import ContractSerializer
from .service import ContractService


@view_defaults(renderer='json')
class ContractController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ContractService()
        self.serializer = ContractSerializer()
        self.schema = ContractSchema()

    @view_config(route_name='get_all_contracts_by_construction_id')
    def get_all_contracts_by_construction_id(self):
        construction_id = self.request.matchdict.get('construction_id')
        contracts = self.service.get_all_by_construction_id(construction_id)
        return self.serializer.convert_list_to_json(contracts)

    @view_config(route_name='add_contract')
    def add_contract(self):
        contract_deserialized = self.schema.deserialize(self.request.json_body)
        contract = self.serializer.to_mapped_object(contract_deserialized)

        self.service.add_contract(contract)
        return {'id': contract.contracts_id}

    @view_config(route_name='delete_contract')
    def delete_contract(self):
        id_ = int(self.request.matchdict.get('id'))
        self.service.delete_contract(id_)
        return {'id': id_}

    @view_config(route_name='edit_contract')
    def edit_contract(self):
        contract_deserialized = self.schema.deserialize(self.request.json_body)
        contract_deserialized['id'] = int(self.request.matchdict.get('id'))

        contract = self.serializer.to_mapped_object(contract_deserialized)
        self.service.edit_contract(contract)
        return {'id': contract.contracts_id}

    @view_config(route_name='get_contract')
    def get_contract(self):
        id_ = int(self.request.matchdict.get('id'))
        contract = self.service.get_contract(id_)
        return self.serializer.to_json(contract)
