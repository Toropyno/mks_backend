from sqlalchemy.exc import DBAPIError

from mks_backend.repositories.construction_objects_repository import ConstructionObjectRepository


class ConstructionObjectService:

    def __init__(self):
        self.repo = ConstructionObjectRepository()

    def get_all_construction_objects_by_construction_id(self, construction_id):
        return self.repo.get_all_construction_objects_by_construction_id(construction_id)

    def get_construction_object_by_id(self, id):
        return self.repo.get_construction_object_by_id(id)

    def add_construction_object(self, construction_object):
        try:
            self.repo.add_construction_object(construction_object)
        except DBAPIError as error:
            print(error.orig.pgerror)
            errortext = error.orig.pgerror[0]
            detail = error.orig.pgerror[1]
            if errortext.find('duplicate key value violates unique constraint'):
                if detail.find('object_code'):
                    raise ValueError('Объект строительства с таким кодом уже существует')
                else:
                    raise ValueError(error.args[0])

    def delete_construction_object_by_id(self, id):
        self.repo.delete_construction_object_by_id(id)

    def update_construction_object(self, new_construction_object):
        old_construction_object = self.repo.get_construction_object_by_id(new_construction_object.construction_objects_id)

        if old_construction_object.object_code != new_construction_object.object_code:
            if self.repo.get_construction_object_by_code(new_construction_object.object_code):
                raise ValueError('Объект строительства с таким кодом уже существует')
        self.repo.update_construction_object(new_construction_object)