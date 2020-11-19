# from pyramid.request import Request
# from pyramid.view import view_config
#
# from mks_backend.controllers.schemas.state_contracts.contract import ContractSchema
# from mks_backend.serializers.state_contracts.contract import ContractSerializer
# from mks_backend.services.state_contracts.contract import ContractService
#
# from mks_backend.errors.handle_controller_error import handle_db_error, handle_colander_error
#
#
# class ContractController:
#
#     def __init__(self, request: Request):
#         self.request = request
#         self.service = ContractService()
#         self.serializer = ContractSerializer()
#         self.schema = ContractSchema()
#
#     @view_config(route_name='get_all_contracts', renderer='json')
#     def get_all_contracts(self):
#         contracts = self.service.get_all_contracts()
#         return self.serializer.convert_list_to_json(contracts)
#
#     @handle_db_error
#     @handle_colander_error
#     @view_config(route_name='add_contract', renderer='json')
#     def add_contract(self):
#         contract_deserialized = self.schema.deserialize(self.request.json_body)
#         contract = self.serializer.to_mapped_object(contract_deserialized)
#
#         self.service.add_contract(contract)
#         return {'id': contract.contracts_id}
#
#     @view_config(route_name='delete_contract', renderer='json')
#     def delete_contract(self):
#         id_ = int(self.request.matchdict['id'])
#         self.service.delete_contract_by_id(id_)
#         return {'id': id_}
#
#     @handle_db_error
#     @handle_colander_error
#     @view_config(route_name='edit_contract', renderer='json')
#     def edit_contract(self):
#         contract_deserialized = self.schema.deserialize(self.request.json_body)
#         contract_deserialized['id'] = int(self.request.matchdict['id'])
#
#         new_contract = self.serializer.to_mapped_object(contract_deserialized)
#         self.service.update_contract(new_contract)
#         return {'id': new_contract.contracts_id}
#
#     @view_config(route_name='get_contract', renderer='json')
#     def get_contract(self):
#         id_ = int(self.request.matchdict['id'])
#         contract = self.service.get_contract(id_)
#         return self.serializer.to_json(contract)
