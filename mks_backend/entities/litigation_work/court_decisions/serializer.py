from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler

from .model import CourtDecision


class CourtDecisionSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, court_decision: CourtDecision) -> dict:
        return {
            'id': court_decision.court_decisions_id,
            'fullName': court_decision.fullname,
        }

    def to_mapped_object(self, schema: dict) -> CourtDecision:
        court_decision = CourtDecision()

        court_decision.court_decisions_id = schema.get('id')
        court_decision.fullname = schema.get('fullName')

        return court_decision
