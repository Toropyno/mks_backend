from mks_backend.models.military_unit import MilitaryUnit
from mks_backend.repositories import DBSession


class MilitaryUnitRepository:

    def get_all_military_units(self):
        return DBSession.query(MilitaryUnit).all()
