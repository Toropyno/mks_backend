from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.entities.state_contracts.contract import ContractSerializer
from mks_backend.entities.state_contracts.contract_work_type import ContractWorkTypeSerializer
from mks_backend.utils.date_and_time import get_date_string

from .model import CompletionDate


class CompletionDateSerializer(BaseSerializer):

    def __init__(self):
        self.contract_serializer = ContractSerializer()
        self.contract_work_serializer = ContractWorkTypeSerializer()

    def to_json(self, completion_date: CompletionDate) -> dict:
        return {
            'id': completion_date.completion_dates_id,
            'contractId': completion_date.contracts_id,
            'contractWorkType': self.contract_work_serializer.to_json(completion_date.contract_worktype),
            'endDate': get_date_string(completion_date.end_date),
        }

    def to_mapped_object(self, schema: dict) -> CompletionDate:
        completion_date = CompletionDate()

        completion_date.completion_dates_id = schema.get('id')
        completion_date.contracts_id = schema.get('contractId')
        completion_date.contract_worktypes_id = schema.get('contractWorkTypeId')
        completion_date.end_date = schema.get('endDate')

        return completion_date
