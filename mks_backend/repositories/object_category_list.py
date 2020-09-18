from mks_backend.errors.db_basic_error import db_error_handler
from mks_backend.models.object_category_list import ObjectCategoryList
from mks_backend.repositories import DBSession


class ObjectCategoryListRepository:

    def get_object_categories_list_by_id(self, id: int) -> ObjectCategoryList:
        return DBSession.query(ObjectCategoryList).get(id)

    def get_all_object_categories_lists(self) -> list:
        return DBSession.query(ObjectCategoryList).all()

    @db_error_handler
    def add_object_categories_list(self, object_categories_list: ObjectCategoryList) -> None:
        DBSession.add(object_categories_list)
        DBSession.commit()

    def delete_object_categories_list_by_id(self, id: int) -> None:
        object_categories_list = self.get_object_categories_list_by_id(id)
        DBSession.delete(object_categories_list)
        DBSession.commit()

    @db_error_handler
    def update_object_categories_list(self, object_categories_list: ObjectCategoryList) -> None:
        DBSession.query(ObjectCategoryList).filter_by(
            object_categories_list_id=object_categories_list.object_categories_list_id).update(
            {
                'zones_id': object_categories_list.zones_id,
                'object_categories_id': object_categories_list.object_categories_id
            }
        )
        DBSession.commit()

    def get_object_categories_list_by_relations(self, zone_id, object_category_id) -> ObjectCategoryList:
        return DBSession.query(ObjectCategoryList).filter(
            ObjectCategoryList.zones_id == zone_id,
            ObjectCategoryList.object_categories_id == object_category_id
        ).first()
