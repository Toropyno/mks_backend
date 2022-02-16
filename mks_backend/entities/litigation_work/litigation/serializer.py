from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.entities.construction_company import ConstructionCompanySerializer
from mks_backend.entities.litigation_work.court_decisions.serializer import CourtDecisionSerializer
from mks_backend.entities.litigation_work.courts.serializer import CourtSerializer
from mks_backend.entities.litigation_work.participant_statuses import ParticipantStatusSerializer
from mks_backend.entities.organizations.organization import OrganizationSerializer
from mks_backend.errors import serialize_error_handler
from mks_backend.utils.date_and_time import get_date_string

from .model import Litigation


class LitigationSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, litigation: Litigation) -> dict:
        return {
            'id': litigation.litigation_id,
            'appealDate': get_date_string(litigation.appeal_date),
            'court': CourtSerializer.to_json(litigation.court),
            'organization': OrganizationSerializer.to_simple_json(litigation.organization),
            'participantStatus': ParticipantStatusSerializer.to_json(litigation.participant_status),
            'constructionCompany': ConstructionCompanySerializer.to_json(litigation.construction_company),
            'participantOther': litigation.participant_other,
            'information': litigation.information,
            'courtDecision': CourtDecisionSerializer.to_json(litigation.court_decision),
            'decisionDate': get_date_string(litigation.decision_date),
            'note': litigation.note
        }

    def to_mapped_object(self, schema: dict) -> Litigation:
        litigation = Litigation()
        litigation.litigation_id = schema.get('id')
        litigation.appeal_date = schema.get('appealDate')
        litigation.courts_id = schema.get('court')
        litigation.organizations_id = schema.get('organization')
        litigation.participant_statuses_id = schema.get('participantStatus')
        litigation.construction_companies_id = schema.get('constructionCompany')
        litigation.participant_other = schema.get('participantOther')
        litigation.information = schema.get('information')
        litigation.court_decisions_id = schema.get('courtDecision')
        litigation.decision_date = schema.get('decisionDate')
        litigation.note = schema.get('note')
        return litigation
