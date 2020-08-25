from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.construction_subcategories import ConstructionSubcategories
from mks_backend.repositories import DBSession


class ConstructionSubcategoryRepository:

    @classmethod
    def get_construction_subcategory_by_id(cls, id):
        return DBSession.query(ConstructionSubcategories).get(id)

    def get_all_construction_subcategories(self):
        return DBSession.query(ConstructionSubcategories).all()

    @db_error_handler
    def add_construction_subcategory(self, construction_subcategory):
        DBSession.add(construction_subcategory)
        DBSession.commit()

    def delete_construction_subcategory_by_id(self, id):
        construction_subcategory = self.get_construction_subcategory_by_id(id)
        DBSession.delete(construction_subcategory)
        DBSession.commit()

    @db_error_handler
    def update_construction_subcategory(self, construction_subcategory):
        DBSession.query(ConstructionSubcategories).filter_by(
            construction_subcategory_id=construction_subcategory.construction_subcategory_id).update(
            {'fullname': construction_subcategory.fullname})
        DBSession.commit()
