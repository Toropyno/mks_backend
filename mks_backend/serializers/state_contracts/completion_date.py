from mks_backend.models.state_contracts.completion_date import CompletionDate
from mks_backend.serializers.state_contracts import ContractSerializer
from mks_backend.serializers.state_contracts.contract_work_type import ContractWorkTypeSerializer
from mks_backend.serializers.utils import get_date_string


class CompletionDateSerializer:

    def __init__(self):
        self.contract_serializer = ContractSerializer()
        self.contract_work_serializer = ContractWorkTypeSerializer()

    def to_json(self, completion_date: CompletionDate) -> dict:
        return {
            'id': completion_date.completion_dates_id,
            'contract': self.contract_serializer.to_json(completion_date.contract),
            'contractWorkType': self.contract_work_serializer.to_json(completion_date.contract_worktype),
            'endDate': get_date_string(completion_date.end_date),
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
