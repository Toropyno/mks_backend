from typing import List

from mks_backend.models.organizations.organization import Organization
from mks_backend.models.organizations.organization_history import OrganizationHistory
from mks_backend.session import DBSession

from mks_backend.errors.db_basic_error import DBBasicError


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

    def delete(self, organization_uuid: str):
        self._query.filter(Organization.organizations_id == organization_uuid).delete()
        DBSession.commit()

    def get_rootes(self) -> List[Organization]:
        DBSession.commit()
        rootes = self._query.join(OrganizationHistory).filter(Organization.parent_organizations_id == None). \
            order_by(Organization.par_number.asc(), OrganizationHistory.shortname).all()
        return rootes
