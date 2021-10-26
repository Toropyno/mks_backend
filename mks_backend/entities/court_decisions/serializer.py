from .model import CourtDecision

from mks_backend.errors import serialize_error_handler


class CourtDecisionSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, court_decision: CourtDecision) -> dict:
        return {
            'id': court_decision.court_decisions_id,
            'fullName': court_decision.fullname,
        }

    def convert_list_to_json(self, court_decision: list) -> list:
        return list(map(self.convert_object_to_json, court_decision))

    def convert_schema_to_object(self, schema: dict) -> CourtDecision:
        court_decision = CourtDecision()

        court_decision.court_decisions_id = schema.get('id')
        court_decision.fullname = schema.get('fullName')

        return court_decision
