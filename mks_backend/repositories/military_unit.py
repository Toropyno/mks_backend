from mks_backend.models.military_unit import MilitaryUnit
from mks_backend.repositories import DBSession


class MilitaryUnitRepository:

    def get_root_military_units(self) -> list:
        return DBSession.query(MilitaryUnit).filter(MilitaryUnit.pidMU == None).all()
