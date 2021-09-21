from .model import ObjectCategory
from mks_backend.session import DBSession


class ObjectCategoryRepository:

    def __init__(self):
        self._query = DBSession.query(ObjectCategory)

    def get_object_category_by_id(self, id: int) -> ObjectCategory:
        return self._query.get(id)

    def get_all_object_categories(self) -> list:
        return self._query.order_by(ObjectCategory.fullname).all()

    def get_many_object_categories_by_id(self, ids: list) -> list:
        return self._query.filter(
            ObjectCategory.object_categories_id.in_(ids)
        ).all()

    def add_object_category(self, object_category: ObjectCategory) -> None:
        DBSession.add(object_category)
        DBSession.commit()

    def delete_object_category_by_id(self, id: int) -> None:
        object_category = self.get_object_category_by_id(id)
        DBSession.delete(object_category)
        DBSession.commit()

    def update_object_category(self, object_category: ObjectCategory) -> None:
        self._query.filter_by(
            object_categories_id=object_category.object_categories_id).update(
            {
                'note': object_category.note,
                'fullname': object_category.fullname
            }
        )
        DBSession.commit()
