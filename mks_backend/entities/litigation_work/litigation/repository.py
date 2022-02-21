from sqlalchemy import desc, not_

from mks_backend.entities.construction_company import ConstructionCompany
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

    def get_all_litigations(self) -> list:
        return self._query.order_by(Litigation.litigation_id).all()

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

    def get_filtered_litigations(self, params: dict):
        filtered_litigations = self._query.outerjoin(ParticipantStatus). \
            outerjoin(Organization).outerjoin(ConstructionCompany).outerjoin(CourtDecision). \
            outerjoin(LitigationSubject).outerjoin(Construction).outerjoin(FIAS).outerjoin(Courts)

        if 'appeal_start' in params:
            appeal_start = params['appeal_start']
            filtered_litigations = filtered_litigations.filter(Litigation.appeal_date >= appeal_start)
        if 'appeal_end' in params:
            appeal_end = params['appeal_end']
            filtered_litigations = filtered_litigations.filter(Litigation.appeal_date <= appeal_end)
        if 'courts_id' in params:
            courts_id = params['courts_id']
            filtered_litigations = filtered_litigations.filter(Courts.courts_id == courts_id)
        if 'organizations_id' in params:
            organizations_id = params['organizations_id']
            filtered_litigations = filtered_litigations.filter(Organization.organizations_id == organizations_id)
        if 'participant_status_id' in params:
            participant_status_id = params['participant_status_id']
            filtered_litigations = filtered_litigations.filter(
                ParticipantStatus.participant_statuses_id == participant_status_id
            )
        if 'construction_companies_id' in params:
            construction_companies_id = params['construction_companies_id']
            filtered_litigations = filtered_litigations.filter(
                ConstructionCompany.construction_companies_id == construction_companies_id
            )
        if 'participant_other' in params:
            participant_other = params['participant_other']
            filtered_litigations = filtered_litigations.filter(
                Litigation.participant_other.ilike('%{}%'.format(participant_other))
            )
        if 'information' in params:
            information = params['information']
            filtered_litigations = filtered_litigations.filter(
                Litigation.information.ilike('%{}%'.format(information))
            )
        if 'court_decisions_id' in params:
            court_decisions_id = params['court_decisions_id']
            filtered_litigations = filtered_litigations.filter(Litigation.court_decisions_id == court_decisions_id)
        if 'have_file' in params:
            have_file = params['have_file']
            if have_file:
                filtered_litigations = filtered_litigations.filter(Litigation.litigation_documents)
            else:
                filtered_litigations = filtered_litigations.filter(not_(Litigation.litigation_documents.any()))
        if 'participant_status' in params:
            participant_status = params['participant_status']
            if participant_status:
                filtered_litigations = filtered_litigations.filter(Litigation.participant_status)
            else:
                filtered_litigations = filtered_litigations.filter(not_(Litigation.participant_status.has()))
        if 'have_isp' in params:
            have_isp = params['have_isp']
            if have_isp:
                filtered_litigations = filtered_litigations.filter(Litigation.litigation_subject == have_isp)
            else:
                filtered_litigations = filtered_litigations.filter(not_(Litigation.litigation_subject.any()))
        if 'project_code' in params:
            project_code = params['project_code']
            if project_code:
                filtered_litigations = filtered_litigations.filter(
                    Construction.project_code == project_code
                )
            else:
                filtered_litigations = filtered_litigations.filter(not_(Construction.project_code.any()))
        if 'is_critical' in params:
            is_critical = params['is_critical']
            if is_critical:
                filtered_litigations = filtered_litigations.filter(Construction.is_critical.is_(True))
            else:
                filtered_litigations = filtered_litigations.filter(Construction.is_critical.isnot(True))
        if 'decision_start' in params:
            decision_date_start = params['decision_date_start']
            filtered_litigations = filtered_litigations.filter(Litigation.decision_date >= decision_date_start)
        if 'decision_end' in params:
            decision_date_end = params['decision_date_end']
            filtered_litigations = filtered_litigations.filter(Litigation.decision_date <= decision_date_end)
        if 'note' in params:
            note = params['note']
            filtered_litigations = filtered_litigations.filter(Litigation.note.ilike('%{}%'.format(note)))
        if 'fias_subject' in params:
            filtered_litigations = filtered_litigations.filter(FIAS.region.ilike('%{}%'.format(params['fias_subject'])))

        return filtered_litigations.order_by(desc(Litigation.decision_date)).all()
