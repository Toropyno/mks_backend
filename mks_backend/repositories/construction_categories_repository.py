from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.construction_categories import ConstructionCategories
from mks_backend.repositories import DBSession


class ConstructionCategoryRepository:

    @classmethod
    def get_construction_category_by_id(cls, id):
        return DBSession.query(ConstructionCategories).get(id)

    def get_all_construction_categories(self):
        return DBSession.query(ConstructionCategories).all()

    @db_error_handler
    def add_construction_category(self, construction_category):
        DBSession.add(construction_category)
        DBSession.commit()

    def delete_construction_category_by_id(self, id):
        construction_category = self.get_construction_category_by_id(id)
        DBSession.delete(construction_category)
        DBSession.commit()

    @db_error_handler
    def update_construction_category(self, construction_category):
        DBSession.query(ConstructionCategories).filter_by(
            construction_categories_id=construction_category.construction_categories_id).update(
            {
                'fullname': construction_category.fullname
            })
        DBSession.commit()
