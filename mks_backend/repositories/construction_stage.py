from mks_backend.models.construction_stage import ConstructionStage
from mks_backend.models import DBSession

from mks_backend.errors import db_error_handler, DBBasicError


class ConstructionStageRepository:

    def __init__(self):
        self._query = DBSession.query(ConstructionStage)

    def get_construction_stage_by_id(self, id: int) -> ConstructionStage:
        return self._query.get(id)

    def get_all_construction_stages(self) -> list:
        return self._query.order_by(ConstructionStage.fullname).all()

    @db_error_handler
    def add_construction_stage(self, construction_stage: ConstructionStage) -> None:
        DBSession.add(construction_stage)
        DBSession.commit()

    def delete_construction_stage_by_id(self, id: int) -> None:
        construction_stage = self.get_construction_stage_by_id(id)
        DBSession.delete(construction_stage)
        DBSession.commit()

    @db_error_handler
    def update_construction_stage(self, construction_stage: ConstructionStage) -> None:
        if DBSession.merge(construction_stage) and not DBSession.new:
            DBSession.commit()
        else:
            DBSession.rollback()
            raise DBBasicError('construction_stage_ad')
