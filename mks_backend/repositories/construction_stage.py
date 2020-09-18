from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.construction_stage import ConstructionStage
from mks_backend.repositories import DBSession


class ConstructionStageRepository:

    def get_construction_stage_by_id(self, id: int) -> ConstructionStage:
        return DBSession.query(ConstructionStage).get(id)

    def get_all_construction_stages(self) -> list:
        return DBSession.query(ConstructionStage).all()

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
        DBSession.query(ConstructionStage).filter_by(
            construction_stages_id=construction_stage.construction_stages_id).update(
            {
                'code': construction_stage.code,
                'fullname': construction_stage.fullname
            }
        )
        DBSession.commit()
