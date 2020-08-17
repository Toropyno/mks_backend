from mks_backend.models.construction_categories import ConstructionCategories
from mks_backend.repositories import DBSession


class ConstructionCategoryRepository:

    @classmethod
    def get_construction_category_by_id(cls, id):
        return DBSession.query(ConstructionCategories).get(id)

    def get_all_construction_categories(self):
        return DBSession.query(ConstructionCategories).all()

    def add_construction_category(self, construction_category):
        DBSession.add(construction_category)
        DBSession.commit()

    def delete_construction_category_by_id(self, id):
        construction_category = self.get_construction_category_by_id(id)
        DBSession.delete(construction_category)
        DBSession.commit()

    def update_construction_category(self, construction_category):
        DBSession.query(ConstructionCategories).filter_by(
            construction_category_id=construction_category.construction_category_id).update(
            {'fullname': construction_category.fullname})
        DBSession.commit()