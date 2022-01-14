from mks_backend.session import DBSession

from .models.military_unit import MilitaryUnit


class MilitaryUnitRepository:

    def get_root_military_units(self) -> list:
        return DBSession.query(MilitaryUnit).filter(MilitaryUnit.pidMU.is_(None)).all()
