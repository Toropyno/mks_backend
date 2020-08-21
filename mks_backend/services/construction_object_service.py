from sqlalchemy.exc import DBAPIError

from mks_backend.repositories.construction_objects_repository import ConstructionObjectRepository
from mks_backend.errors.db_basic_error import DBBasicError


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
            raise DBBasicError(error)
            #raise ValueError('Объект строительства с таким кодом уже существует')


    def delete_construction_object_by_id(self, id):
        self.repo.delete_construction_object_by_id(id)

    def update_construction_object(self, new_construction_object):
        #raise ValueError('Объект строительства с таким кодом уже существует')
        try:
            self.repo.update_construction_object(new_construction_object)
        except DBAPIError as error:
            raise DBBasicError(error)