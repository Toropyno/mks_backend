from typing import List

from sqlalchemy import func

from mks_backend.session import DBSession

from .model import Official


class OfficialRepository:

    def __init__(self):
        self._query = DBSession.query(Official)

    def add_official(self, official: Official) -> None:
        DBSession.add(official)
        DBSession.commit()

    def update_official(self, official: Official) -> None:
        self._query.filter_by(officials_id=official.officials_id).update(
            {
                'position_name': official.position_name,
                'organizations_id': official.organizations_id,
                'military_ranks_id': official.military_ranks_id,
                'class_ranks_id': official.class_ranks_id,
                'surname': official.surname,
                'firstname': official.firstname,
                'middlename': official.middlename,
                'begin_date': official.begin_date,
                'end_date': official.end_date,
                'phone': official.phone,
                'email': official.email,
                'secure_channel': official.secure_channel,
                'note': official.note,
                'idfilestorage': official.idfilestorage
            }
        )
        DBSession.commit()

    def delete_official(self, id_: int) -> None:
        official = self.get_official(id_)
        DBSession.delete(official)
        DBSession.commit()

    def get_official(self, id_: int) -> Official:
        return self._query.filter_by(officials_id=id_).first()

    def get_officials_by_organization(self, filter_fields: dict) -> List[Official]:
        organization_uuid = filter_fields.get('organization_uuid')
        reflect_vacated_position = filter_fields.get('reflectVacatedPosition')
        official_name = filter_fields.get('officialName')

        officials = self._query.filter(Official.organizations_id == organization_uuid)

        if not reflect_vacated_position:
            officials = officials.filter(Official.end_date.is_(None))

        if official_name:
            officials = officials.filter(
                func.CONCAT_WS(
                    ' ', Official.surname, Official.firstname, Official.middlename
                ).ilike('%{}%'.format(official_name))
            )
        return officials
