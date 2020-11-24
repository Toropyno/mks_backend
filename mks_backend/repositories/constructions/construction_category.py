from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.constructions import ConstructionCategory
from mks_backend.repositories import DBSession


class ConstructionCategoryRepository:

    def get_construction_category_by_id(self, id: int) -> ConstructionCategory:
        return DBSession.query(ConstructionCategory).get(id)

    def get_all_construction_categories(self) -> list:
        return DBSession.query(ConstructionCategory).order_by(ConstructionCategory.fullname).all()

    @db_error_handler
    def add_construction_category(self, construction_category: ConstructionCategory) -> None:
        DBSession.add(construction_category)
        DBSession.commit()

    def delete_construction_category_by_id(self, id: int) -> None:
        construction_category = self.get_construction_category_by_id(id)
        DBSession.delete(construction_category)
        DBSession.commit()

    @db_error_handler
    def update_construction_category(self, construction_category: ConstructionCategory) -> None:
        DBSession.commit()
