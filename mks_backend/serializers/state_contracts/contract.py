from mks_backend.models.state_contracts.contract import Contract

from mks_backend.serializers.state_contracts.contract_status import ContractStatusSerializer
from mks_backend.serializers.construction_company import ConstructionCompanySerializer

from mks_backend.serializers.utils import get_date_string, decimal_to_str


class ContractSerializer:

    def __init__(self):
        self.status_serializer = ContractStatusSerializer()
        self.construction_company_serializer = ConstructionCompanySerializer()

    def convert_list_to_json(self, contracts: list) -> list:
        return list(map(self.to_json, contracts))

    def to_json(self, contract: Contract) -> dict:
        return {
            'contractId': contract.contracts_id,
            'contractNum': contract.contract_num,
            'constructionId': contract.construction_id,
            'contractDate': get_date_string(contract.contract_date),
            'identifier': contract.identifier,
            'subject': contract.subject,

            'contractSum': decimal_to_str(contract.contract_sum),
            'paidSum': decimal_to_str(contract.paid_sum),
            'acceptedSum': decimal_to_str(contract.accepted_sum),
            'receivables': decimal_to_str(contract.receivables),
            'planSum': decimal_to_str(contract.plan_sum),

            'contractor': self.construction_company_serializer.convert_object_to_json(contract.contractor),
            'subcontractor': self.construction_company_serializer.convert_object_to_json(contract.subcontractor),
            'status': self.status_serializer.convert_object_to_json(contract.status),
        }

    def to_mapped_object(self, schema: dict) -> Contract:
        return Contract(
            contracts_id=schema.get('contractId'),
            contract_num=schema.get('contractNum'),
            contract_date=schema.get('contractDate'),
            identifier=schema.get('identifier'),
            subject=schema.get('subject'),

            contract_sum=schema.get('contractSum'),
            paid_sum=schema.get('paidSum'),
            accepted_sum=schema.get('acceptedSum'),
            receivables=schema.get('receivables'),
            plan_sum=schema.get('planSum'),

            construction_id=schema.get('constructionId'),
            contractor_id=schema.get('contractorId'),
            subcontractor_id=schema.get('subcontractorId'),
            contract_statuses_id=schema.get('contractStatusId'),
        )
