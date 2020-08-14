from mks_backend.models.military_unit import MilitaryUnit
from mks_backend.repositories import DBSession

class MilitaryUnitRepository:

    def get_all_military_units(self):
        return DBSession.query(MilitaryUnit).all()

    def add_military_unit(self, military_unit):
        DBSession.add(military_unit)
        DBSession.commit()

    def update_military_unit(self, military_unit):
        DBSession.query(MilitaryUnit).filter_by(idMU=military_unit.idMU).update(
            {'pidMU': military_unit.pidMU,
             'vChNumber': military_unit.vChNumber,
             'idNameMU': military_unit.idNameMU})
            #'idPurpose': military_unit.idPurpose,
            #'idMilitaryCity': military_unit.idMilitaryCity,
            #'idSortAF': military_unit.idSortAF,
            #'idCombatArm': military_unit.idCombatArm,
            #'codeNameMU': military_unit.codeNameMU
        DBSession.commit()


    def delete_military_unit_by_id(self, id):
        military_unit = self.get_military_unit_by_id(id)
        DBSession.delete(military_unit)
        DBSession.commit()


    @classmethod
    def get_military_unit_by_id(cls, id):
        return DBSession.query(MilitaryUnit).get(id)
