from typing import List

from .model import Litigation
from .repository import LitigationRepository


class LitigationService:

    def __init__(self):
        self.repo = LitigationRepository()

    def get_all_litigations(self) -> list:
        return self.repo.get_all_litigations()

    def get_litigation_by_id(self, id_: int) -> Litigation:
        return self.repo.get_litigation_by_id(id_)

    def add_litigation(self, litigation) -> None:
        self.repo.add_litigation(litigation)

    def update_litigation(self, litigation) -> None:
        self.repo.update_litigation(litigation)

    def delete_litigation_by_id(self, id_: int) -> None:
        self.repo.delete_litigation_by_id(id_)

    def get_litigations(self, filter_params=None) -> List[Litigation]:
        if filter_params:
            params = self.switch_case(filter_params)
            return self.repo.get_filtered_litigations(params)
        else:
            return self.repo.get_all_litigations()

    def switch_case(self, filter_params: dict) -> dict:
        case_switcher = {
            'litigationId': 'litigation_id',
            'appealStart': 'appeal_start',
            'appealEnd': 'appeal_end',
            'courtsId': 'courts_id',
            'organizationsId': 'organizations_id',
            'participantStatusId': 'participant_status_id',
            'constructionCompaniesId': 'construction_companies_id',
            'participantOther': 'participant_other',
            'information': 'information',
            'courtDecisionsId': 'court_decisions_id',
            'participantStatus': 'participant_status',
            'haveFile': 'have_file',
            'haveIsp': 'have_isp',
            'decisionStart': 'decision_start',
            'decisionEnd': 'decision_end',
            'isCritical': 'is_critical',
            'note': 'note',
            'fiasSubject': 'fias_subject',
            'projectCode': 'project_code'
        }

        params = dict()
        for key in filter_params:
            params[case_switcher[key]] = filter_params[key]

        return params
