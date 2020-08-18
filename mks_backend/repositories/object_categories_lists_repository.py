from mks_backend.models.object_categories_list import ObjectCategoriesList
from mks_backend.repositories import DBSession


class ObjectCategoriesListRepository:

    @classmethod
    def get_object_categories_list_by_id(cls, id):
        return DBSession.query(ObjectCategoriesList).get(id)

    def get_all_object_categories_lists(self):
        return DBSession.query(ObjectCategoriesList).all()

    def add_object_categories_list(self, object_categories_list):
        DBSession.add(object_categories_list)
        DBSession.commit()

    def delete_object_categories_list_by_id(self, id):
        object_categories_list = self.get_object_categories_list_by_id(id)
        DBSession.delete(object_categories_list)
        DBSession.commit()

    def update_object_categories_list(self, object_categories_list):
        DBSession.query(ObjectCategoriesList).filter_by(
            object_categories_list_id=object_categories_list.object_categories_list_id).update(
            {'zones_id': object_categories_list.zones_id,
             'object_categories_id': object_categories_list.object_categories_id})
        DBSession.commit()

    def get_object_categories_list_by_zone_id(self, zones_id):
        return DBSession.query(ObjectCategoriesList).filter_by(zones_id=zones_id).first()

    def get_object_categories_list_by_object_categories_id(self, object_categories_id):
        return DBSession.query(ObjectCategoriesList).filter_by(object_categories_id=object_categories_id).first()

