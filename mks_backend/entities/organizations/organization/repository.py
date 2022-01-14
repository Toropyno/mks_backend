from typing import List

from sqlalchemy import func, or_

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
        instance = self.get_by_id(organization_uuid)
        DBSession.delete(instance)
        DBSession.commit()

    def get_roots(self) -> List[Organization]:
        return self._query.join(OrganizationHistory).filter(
            Organization.parent_organizations_id.is_(None)
        ).order_by(Organization.par_number, OrganizationHistory.shortname).all()

    def get_all_organizations(self, filter_fields: dict = None) -> List[str]:
        """
        Параметр organization_name фильтрует организации по краткому и полному наименованию связанных сущностей в
            таблице "История изменения организации"

        Параметр official_name фильтрует организации по ФИО должностных лиц, фигурирующих в них. Для этого формируется
            подзапрос, который конкатенирует фамилию, имя и отчество сотрудников

        Параметр reflect_vacated_position фильтрует должностные лица на предмет освобождения должности. Если true -
            отображать все должностные лица, иначе - только те, которые не освободили должность

        :return: List[str] Список идентификаторов организаций, удовлетворяющих параметрам фильтрации
        """
        organization_name = filter_fields.get('organizationName')
        official_name = filter_fields.get('officialName')
        reflect_vacated_position = filter_fields.get('reflectVacatedPosition')

        organizations = DBSession.query(Organization.organizations_id)

        if organization_name:
            organizations = organizations.join(OrganizationHistory).filter(or_(
                OrganizationHistory.shortname.ilike('%{}%'.format(organization_name)),
                OrganizationHistory.fullname.ilike('%{}%'.format(organization_name))
            ))
        if official_name:
            organizations = organizations.join(Official).filter(
                func.CONCAT_WS(
                    ' ', Official.surname, Official.firstname, Official.middlename
                ).ilike('%{}%'.format(official_name))
            )
            if not reflect_vacated_position:
                organizations = organizations.filter(Official.end_date.is_(None))

        return [organization[0] for organization in organizations.distinct().all()]
