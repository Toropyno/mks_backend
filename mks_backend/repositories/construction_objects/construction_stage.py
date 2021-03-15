from mks_backend.models.construction_objects.construction_stage import ConstructionStage
from mks_backend.session import DBSession

from mks_backend.errors import DBBasicError


class ConstructionStageRepository:

    def __init__(self):
        self._query = DBSession.query(ConstructionStage)

    def get_construction_stage_by_id(self, id_: int) -> ConstructionStage:
        return self._query.get(id_)

    def get_all_construction_stages(self) -> list:
        return self._query.order_by(ConstructionStage.fullname).all()

    def add_construction_stage(self, construction_stage: ConstructionStage) -> None:
        self.check_parent(construction_stage)
        DBSession.add(construction_stage)
        DBSession.commit()

    def delete_construction_stage_by_id(self, id_: int) -> None:
        construction_stage = self.get_construction_stage_by_id(id_)
        DBSession.delete(construction_stage)
        DBSession.commit()

    def update_construction_stage(self, construction_stage: ConstructionStage) -> None:
        self.check_parent(construction_stage)
        if DBSession.merge(construction_stage) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('construction_stage_ad')

    def check_parent(self, construction_stage: ConstructionStage):
        if construction_stage.construction_stages_id == construction_stage.ref_construction_stages_id:
            raise DBBasicError('construction_stage_logical')
