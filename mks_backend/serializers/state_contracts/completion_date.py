from mks_backend.models.state_contracts.completion_date import CompletionDate
from mks_backend.serializers.state_contracts.contract_work_type import ContractWorkTypeSerializer


class CompletionDateSerializer:

    def to_json(self, completion_date: CompletionDate) -> dict:
        return {
            'id': completion_date.completion_dates_id,
            'contractId': 1,  # ContractSerializer.to_json(completion_date.contracts_id),
            'contractWorkTypeId': ContractWorkTypeSerializer().to_json(completion_date.contract_worktypes_id),
            'endDate': completion_date.end_date,
        }

    def list_to_json(self, completion_dates: list) -> list:
        return list(map(self.to_json, completion_dates))

    def to_object(self, schema: dict) -> CompletionDate:
        completion_date = CompletionDate()

        completion_date.completion_dates_id = schema.get('id')
        completion_date.contracts_id = schema.get('contractId')
        completion_date.contract_worktypes_id = schema.get('contractWorkTypeId')
        completion_date.end_date = schema.get('endDate')

        return completion_date
