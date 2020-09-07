from mks_backend.models.object_categories import ObjectCategories
from mks_backend.repositories import DBSession
from mks_backend.errors.db_basic_error import db_error_handler


class ObjectCategoryRepository:

    def get_object_category_by_id(cls, id: int) -> ObjectCategories:
        return DBSession.query(ObjectCategories).get(id)

    def get_all_object_categories(self) -> list:
        return DBSession.query(ObjectCategories).all()

    @db_error_handler
    def add_object_category(self, object_category: ObjectCategories) -> None:
        DBSession.add(object_category)
        DBSession.commit()

    def delete_object_category_by_id(self, id: int) -> None:
        object_category = self.get_object_category_by_id(id)
        DBSession.delete(object_category)
        DBSession.commit()

    @db_error_handler
    def update_object_category(self, object_category: ObjectCategories) -> None:
        DBSession.query(ObjectCategories).filter_by(
            object_categories_id=object_category.object_categories_id).update(
            {
                'note': object_category.note,
                'fullname': object_category.fullname
            }
        )
        DBSession.commit()
