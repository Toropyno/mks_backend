from mks_backend.models.state_contracts.contract_work_type import ContractWorkType


class ContractWorkTypeSerializer:

    def to_json(self, contract_w_t: ContractWorkType) -> dict:
        return {
            'id': contract_w_t.contract_worktypes_id,
            'fullName': contract_w_t.fullname,
        }

    def list_to_json(self, contract_w_ts: list) -> list:
        return list(map(self.to_json, contract_w_ts))

    def to_object(self, schema: dict) -> ContractWorkType:
        contract_w_t = ContractWorkType()

        contract_w_t.contract_worktypes_id = schema.get('id')
        contract_w_t.fullname = schema.get('fullName')

        return contract_w_t
