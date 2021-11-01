from .model import Litigation
from mks_backend.errors import serialize_error_handler
from mks_backend.utils.date_and_time import get_date_string


class LitigationSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, litigation: Litigation) -> dict:
        return {
            'litigation_id': litigation.litigation_id,
            'appeal_date': get_date_string(litigation.appeal_date),
            'courts_id': litigation.courts_id,
            'organizations_id': litigation.organizations_id,
            'participant_statuses_id': litigation.participant_statuses_id,
            'construction_companies_id': litigation.construction_companies_id,
            'participant_other': litigation.participant_other,
            'information': litigation.information,
            'court_decisions_id': litigation.court_decisions_id,
            'decision_date': get_date_string(litigation.decision_date),
            'note': litigation.note
        }

    def convert_list_to_json(self, litigation: list) -> list:
        return list(map(self.convert_object_to_json, litigation))

    def convert_schema_to_object(self, schema: dict) -> Litigation:
        litigation = Litigation()
        litigation.litigation_id = schema.get('litigation_id')
        litigation.appeal_date = schema.get('appeal_date')
        litigation.courts_id = schema.get('courts_id')
        litigation.organizations_id = schema.get('organizations_id')
        litigation.participant_statuses_id = schema.get('participant_statuses_id')
        litigation.construction_companies_id = schema.get('construction_companies_id')
        litigation.participant_other = schema.get('participant_other')
        litigation.information = schema.get('information')
        litigation.court_decisions_id = schema.get('court_decisions_id')
        litigation.decision_date = schema.get('decision_date')
        litigation.note = schema.get('note')
        return litigation
