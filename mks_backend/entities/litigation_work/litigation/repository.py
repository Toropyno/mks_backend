from typing import List

from sqlalchemy import desc, not_

from mks_backend.entities.constructions.construction import Construction
from mks_backend.entities.litigation_work.court_decisions import CourtDecision
from mks_backend.entities.litigation_work.courts import Courts
from mks_backend.entities.litigation_work.litigation_subject import LitigationSubject
from mks_backend.entities.litigation_work.participant_statuses import ParticipantStatus
from mks_backend.entities.organizations.organization import Organization
from mks_backend.errors import DBBasicError
from mks_backend.FIAS import FIAS
from mks_backend.session import DBSession

from .model import Litigation


class LitigationRepository:
    def __init__(self):
        self._query = DBSession.query(Litigation)

    def add_litigation(self, litigation: Litigation) -> None:
        DBSession.add(litigation)
        DBSession.commit()

    def delete_litigation_by_id(self, id: int) -> None:
        self._query.filter(Litigation.litigation_id == id).delete()
        DBSession.commit()

    def update_litigation(self, litigation: Litigation) -> None:
        if DBSession.merge(litigation) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('litigation_ad')

    def get_litigation_by_id(self, id_: int) -> Litigation:
        litigation = self._query.get(id_)
        if not litigation:
            raise DBBasicError('litigation_nf')
        return litigation

    def get_litigations(self, params: dict) -> List[Litigation]:
        if params:
            litigations = self._query.outerjoin(ParticipantStatus). \
                outerjoin(Organization).outerjoin(CourtDecision). \
                outerjoin(LitigationSubject).outerjoin(Construction).outerjoin(FIAS).outerjoin(Courts)
            if 'appealDateStart' in params:
                appeal_start = params['appealDateStart']
                litigations = litigations.filter(Litigation.appeal_date >= appeal_start)
            if 'appealDateEnd' in params:
                appeal_end = params['appealDateEnd']
                litigations = litigations.filter(Litigation.appeal_date <= appeal_end)
            if 'court' in params:
                courts_id = params['court']
                litigations = litigations.filter(Courts.courts_id == courts_id)
            if 'organization' in params:
                organizations_id = params['organization']
                litigations = litigations.filter(Organization.organizations_id == organizations_id)
            if 'participantStatus' in params:
                participant_status_id = params['participantStatus']
                litigations = litigations.filter(
                    ParticipantStatus.participant_statuses_id == participant_status_id
                )
            if 'participantOther' in params:
                participant_other = params['participantOther']
                litigations = litigations.filter(
                    Litigation.participant_other.ilike('%{}%'.format(participant_other))
                )
            if 'information' in params:
                information = params['information']
                litigations = litigations.filter(
                    Litigation.information.ilike('%{}%'.format(information))
                )
            if 'courtDecision' in params:
                court_decisions_id = params['courtDecision']
                litigations = litigations.filter(Litigation.court_decisions_id == court_decisions_id)
            if 'haveFile' in params:
                have_file = params['haveFile']
                if have_file:
                    litigations = litigations.filter(Litigation.litigation_documents)
                else:
                    litigations = litigations.filter(not_(Litigation.litigation_documents.any()))
            if 'haveIsp' in params:
                have_isp = params['haveIsp']
                if have_isp:
                    litigations = litigations.filter(Litigation.litigation_subject)
                else:
                    litigations = litigations.filter(not_(Litigation.litigation_subject.any()))
            if 'projectСode' in params:
                project_code = params['projectСode']
                if project_code:
                    litigations = litigations.filter(Construction.project_code.ilike('%{}%'.format(project_code)))
                else:
                    litigations = litigations.filter(not_(Construction.project_code.any()))
            if 'isCritical' in params:
                is_critical = params['isCritical']
                if is_critical:
                    litigations = litigations.filter(Construction.is_critical.is_(True))
                else:
                    litigations = litigations.filter(Construction.is_critical.isnot(True))
            if 'decisionDateStart' in params:
                decision_date_start = params['decisionDateStart']
                litigations = litigations.filter(Litigation.decision_date >= decision_date_start)
            if 'decisionDateEnd' in params:
                decision_date_end = params['decisionDateEnd']
                litigations = litigations.filter(Litigation.decision_date <= decision_date_end)
            if 'fiasSubject' in params:
                litigations = litigations.filter(FIAS.region.ilike('%{}%'.format(params['fiasSubject'])))
            if 'constructionCompany' in params:
                litigations = litigations.filter(Litigation.construction_companies_id == params['constructionCompany'])

        else:
            litigations = self._query

        return litigations.order_by(desc(Litigation.decision_date)).all()
