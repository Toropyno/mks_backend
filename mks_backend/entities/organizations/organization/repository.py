from typing import List

from sqlalchemy import func, and_, or_

from .model import Organization
from .model import OrganizationHistory
from mks_backend.session import DBSession

from mks_backend.errors.db_basic_error import DBBasicError
from mks_backend.entities.organizations.official import Official


class OrganisationRepository:

    def __init__(self):
        self._query = DBSession.query(Organization)

    def add(self, organization: Organization):
        DBSession.add(organization)
        DBSession.commit()

    def update(self, organization: Organization):
        if organization.parent_organizations_id == organization.organizations_id:
            raise DBBasicError('organization_parent_logical')

        if DBSession.merge(organization) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('organization_ad')

    def get_by_id(self, uuid: str) -> Organization:
        organization = self._query.get(uuid)
        if not organization:
            raise DBBasicError('organization_nf')
        return organization

    def delete(self, organization_uuid: str) -> None:
        self._query.filter(Organization.organizations_id == organization_uuid).delete()
        DBSession.commit()

    def get_roots(self) -> List[Organization]:
        return self._query.join(OrganizationHistory).filter(
            Organization.parent_organizations_id.is_(None)
        ).order_by(Organization.par_number, OrganizationHistory.shortname).all()

    def get_all_organizations(self, filter_fields: dict = None) -> List[str]:
        reflect_disbanded = filter_fields.get('reflectDisbanded')
        organization_name = filter_fields.get('organizationName')
        official_name = filter_fields.get('officialName')

        organizations = DBSession.query(Organization.organizations_id).join(
            OrganizationHistory, isouter=True
        ).distinct()
        if reflect_disbanded:
            max_begin_date = DBSession.query(
                func.max(OrganizationHistory.begin_date).label('begin_date'), OrganizationHistory.organizations_id
            ).join(Organization).group_by(
                OrganizationHistory.organizations_id
            ).subquery()
            organizations = organizations.join(
                max_begin_date, and_(
                    max_begin_date.c.organizations_id == OrganizationHistory.organizations_id,
                    max_begin_date.c.begin_date == OrganizationHistory.begin_date)
            ).filter(
                OrganizationHistory.end_date.is_(None)
            )
        if organization_name:
            organizations = organizations.filter(or_(
                OrganizationHistory.shortname.ilike('%{}%'.format(organization_name)),
                OrganizationHistory.fullname.ilike('%{}%'.format(organization_name))
            ))
        if official_name:
            organizations = organizations.join(Official).filter(
                func.CONCAT_WS(
                    ' ', Official.surname, Official.firstname, Official.middlename
                ).ilike('%{}%'.format(official_name))
            )

        return [organization[0] for organization in organizations.all()]
