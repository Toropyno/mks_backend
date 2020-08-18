from mks_backend.models.construction_stages import ConstructionStages
from mks_backend.repositories import DBSession


class ConstructionStageRepository:

    @classmethod
    def get_construction_stage_by_id(cls, id):
        return DBSession.query(ConstructionStages).get(id)

    def get_all_construction_stages(self):
        return DBSession.query(ConstructionStages).all()

    def add_construction_stage(self, construction_stage):
        DBSession.add(construction_stage)
        DBSession.commit()

    def delete_construction_stage_by_id(self, id):
        construction_stage = self.get_construction_stage_by_id(id)
        DBSession.delete(construction_stage)
        DBSession.commit()

    def update_construction_stage(self, construction_stage):
        DBSession.query(ConstructionStages).filter_by(
            construction_stages_id=construction_stage.construction_stages_id).update(
            {'code': construction_stage.code,
             'fullname': construction_stage.fullname})
        DBSession.commit()
