from .model import ObjectCategoryList
from mks_backend.session import DBSession


class ObjectCategoryListRepository:

    def __init__(self):
        self._query = DBSession.query(ObjectCategoryList)

    def get_object_categories_list_by_id(self, id: int) -> ObjectCategoryList:
        return self._query.get(id)

    def get_all_object_categories_lists(self) -> list:
        return self._query.all()

    def add_object_categories_list(self, object_categories_list: ObjectCategoryList) -> None:
        DBSession.add(object_categories_list)
        DBSession.commit()

    def delete_object_categories_list_by_id(self, id: int) -> None:
        object_categories_list = self.get_object_categories_list_by_id(id)
        DBSession.delete(object_categories_list)
        DBSession.commit()

    def update_object_categories_list(self, object_categories_list: ObjectCategoryList) -> None:
        self._query.filter_by(
            object_categories_list_id=object_categories_list.object_categories_list_id).update(
            {
                'zones_id': object_categories_list.zones_id,
                'object_categories_id': object_categories_list.object_categories_id
            }
        )
        DBSession.commit()

    def get_object_categories_list_by_relations(self, zone_id, object_category_id) -> ObjectCategoryList:
        return self._query.filter(
            ObjectCategoryList.zones_id == zone_id,
            ObjectCategoryList.object_categories_id == object_category_id
        ).first()
