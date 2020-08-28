from mks_backend.models.object_categories_list import ObjectCategoriesList
from mks_backend.repositories import DBSession
from mks_backend.errors.db_basic_error import db_error_handler


class ObjectCategoriesListRepository:

    @classmethod
    def get_object_categories_list_by_id(cls, id):
        return DBSession.query(ObjectCategoriesList).get(id)

    def get_all_object_categories_lists(self):
        return DBSession.query(ObjectCategoriesList).all()

    @db_error_handler
    def add_object_categories_list(self, object_categories_list):
        DBSession.add(object_categories_list)
        DBSession.commit()

    def delete_object_categories_list_by_id(self, id):
        object_categories_list = self.get_object_categories_list_by_id(id)
        DBSession.delete(object_categories_list)
        DBSession.commit()

    @db_error_handler
    def update_object_categories_list(self, object_categories_list):
        DBSession.query(ObjectCategoriesList).filter_by(
            object_categories_list_id=object_categories_list.object_categories_list_id).update(
            {
                'zones_id': object_categories_list.zones_id,
                'object_categories_id': object_categories_list.object_categories_id
            })
        DBSession.commit()
