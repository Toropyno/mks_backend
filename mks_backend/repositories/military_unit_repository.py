from mks_backend.models.military_unit import MilitaryUnit
from mks_backend.repositories import DBSession


class MilitaryUnitRepository:

    def get_root_military_units(self):
        return DBSession.query(MilitaryUnit).filter(MilitaryUnit.pidMU==None)

    @classmethod
    def get_military_unit_by_id(cls, id):
        return DBSession.query(MilitaryUnit).get(id)
