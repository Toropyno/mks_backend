from mks_backend.models.organizations.official import Official
from mks_backend.models import DBSession

from mks_backend.errors.db_basic_error import db_error_handler


class OfficialRepository:

    def __init__(self):
        self._query = DBSession.query(Official)

    @db_error_handler
    def add_official(self, official: Official) -> None:
        DBSession.add(official)
        DBSession.commit()

    @db_error_handler
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
