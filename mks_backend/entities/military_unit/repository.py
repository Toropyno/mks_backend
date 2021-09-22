from .models.military_unit import MilitaryUnit
from mks_backend.session import DBSession


class MilitaryUnitRepository:

    def get_root_military_units(self) -> list:
        return DBSession.query(MilitaryUnit).filter(MilitaryUnit.pidMU.is_(None)).all()
