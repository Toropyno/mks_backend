from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler

from .model import ContractStatus


class ContractStatusSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, contract_status: ContractStatus) -> dict:
        return {
            'id': contract_status.contract_statuses_id,
            'fullName': contract_status.fullname,
        }

    def to_mapped_object(self, schema: dict) -> ContractStatus:
        contract_status = ContractStatus()

        contract_status.contract_statuses_id = schema.get('id')
        contract_status.fullname = schema.get('fullName')

        return contract_status
