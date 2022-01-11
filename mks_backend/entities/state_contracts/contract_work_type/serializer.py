from .model import ContractWorkType

from mks_backend.entities.BASE.serializer import BaseSerializer


class ContractWorkTypeSerializer(BaseSerializer):

    def to_json(self, contract_w_t: ContractWorkType) -> dict:
        return {
            'id': contract_w_t.contract_worktypes_id,
            'fullName': contract_w_t.fullname,
        }

    def to_mapped_object(self, schema: dict) -> ContractWorkType:
        contract_w_t = ContractWorkType()

        contract_w_t.contract_worktypes_id = schema.get('id')
        contract_w_t.fullname = schema.get('fullName')

        return contract_w_t
