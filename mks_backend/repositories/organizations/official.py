from mks_backend.models.organizations.official import Official
from mks_backend.session import DBSession


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
                'surname': official.surname,
                'firstname': official.firstname,
                'middlename': official.middlename,
                'begin_date': official.begin_date,
                'end_date': official.end_date,
                'phone': official.phone,
                'email': official.email,
                'secure_channel': official.secure_channel,
                'note': official.note,
            }
        )
        DBSession.commit()

    def delete_official(self, id: int) -> None:
        self._query.filter_by(officials_id=id).delete()
        DBSession.commit()

    def get_official(self, id_: int):
        return self._query.filter_by(officials_id=id_).first()
