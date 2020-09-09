from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.construction_subcategory import ConstructionSubcategory
from mks_backend.repositories import DBSession


class ConstructionSubcategoryRepository:

    @classmethod
    def get_construction_subcategory_by_id(cls, id: int) -> ConstructionSubcategory:
        return DBSession.query(ConstructionSubcategory).get(id)

    def get_all_construction_subcategories(self) -> list:
        return DBSession.query(ConstructionSubcategory).all()

    @db_error_handler
    def add_construction_subcategory(self, construction_subcategory: ConstructionSubcategory):
        DBSession.add(construction_subcategory)
        DBSession.commit()

    def delete_construction_subcategory_by_id(self, id: int) -> None:
        construction_subcategory = self.get_construction_subcategory_by_id(id)
        DBSession.delete(construction_subcategory)
        DBSession.commit()

    @db_error_handler
    def update_construction_subcategory(self, construction_subcategory: ConstructionSubcategory) -> None:
        DBSession.query(ConstructionSubcategory).filter_by(
            construction_subcategories_id=construction_subcategory.construction_subcategories_id).update(
            {
                'fullname': construction_subcategory.fullname
            }
        )
        DBSession.commit()
