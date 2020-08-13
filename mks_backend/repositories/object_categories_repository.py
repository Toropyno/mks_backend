from mks_backend.models.object_categories import ObjectCategories
from mks_backend.repositories import DBSession


class ObjectCategoryRepository(object):

    @classmethod
    def get_object_category_by_id(cls, id):
        return DBSession.query(ObjectCategories).get(id)

    def get_all_object_categories(self):
        return DBSession.query(ObjectCategories).all()

    def add_object_category(self, object_category):
        DBSession.add(object_category)
        DBSession.commit()

    def delete_object_category_by_id(self, id):
        object_category = self.get_object_category_by_id(id)
        DBSession.delete(object_category)
        DBSession.commit()

    def update_object_category(self, object_category):
        pass
