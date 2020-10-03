from mks_backend.models.contract_status import ContractStatus

from mks_backend.errors.serilize_error import serialize_error_handler


class ContractStatusSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, contract_status: ContractStatus) -> dict:
        return {
            'id': contract_status.contract_statuses_id,
            'fullName': contract_status.fullname,
        }

    def convert_list_to_json(self, contract_statuses: list) -> list:
        return list(map(self.convert_object_to_json, contract_statuses))

    def convert_schema_to_object(self, schema: dict) -> ContractStatus:
        contract_status = ContractStatus()

        contract_status.contract_statuses_id = schema.get('id')
        contract_status.fullname = schema.get('fullName')

        return contract_status
