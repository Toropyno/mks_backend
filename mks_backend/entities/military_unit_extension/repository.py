from datetime import date

from sqlalchemy import desc

from mks_backend.errors import DBBasicError
from mks_backend.session import DBSession

from .model import MilitaryUnitExtension


class MilitaryUnitExtensionRepository:
    def __init__(self):
        self._query = DBSession.query(MilitaryUnitExtension)

    def get_all_military_unit_extensions(self) -> list:
        return self._query.order_by(MilitaryUnitExtension.report_name).all()

    def add_military_unit_extension(self, military_unit_extension: MilitaryUnitExtension) -> None:
        DBSession.add(military_unit_extension)
        DBSession.commit()

    def delete_military_unit_extension_by_id(self, id: int, date: date) -> None:
        self._query.filter(MilitaryUnitExtension.idMU == id, MilitaryUnitExtension.start_date == date).delete()
        DBSession.commit()

    def update_military_unit_extension(self, new_military_unit_extension: MilitaryUnitExtension) -> None:
        if DBSession.merge(new_military_unit_extension) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('military_unit_extension_ad')

    def get_military_unit_extension_by_id(self, id: int):
        military_unit_extension = self._query.filter(
            MilitaryUnitExtension.idMU == id
        ).order_by(desc(MilitaryUnitExtension.start_date)).first()
        if not military_unit_extension:
            raise DBBasicError('military_unit_extension_nf')
        return military_unit_extension
