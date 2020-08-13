from mks_backend.models.construction_objects import ConstructionObjects
from mks_backend.repositories import DBSession


class ConstructionObjectRepository(object):

    @classmethod
    def get_construction_object_by_id(cls, id):
        return DBSession.query(ConstructionObjects).get(id)

    def get_all_construction_objects(self):
        return DBSession.query(ConstructionObjects).all()

    def add_construction_object(self, construction_object):
        DBSession.add(construction_object)
        DBSession.commit()

    def delete_construction_object_by_id(self, id):
        construction_object = self.get_construction_object_by_id(id)
        DBSession.delete(construction_object)
        DBSession.commit()

    # def update_construction_object(self, construction_object):
    #     DBSession.query(ConstructionObjects).filter_by(construction_object_id=construction_object.construction_object_id).update(
    #         {'construction_object_num': construction_object.construction_object_num,
    #          'construction_object_date': construction_object.construction_object_date,
    #          'meetings_type_id': construction_object.meetings_type_id,
    #          'construction_object_name': construction_object.construction_object_name,
    #          'note': construction_object.note,
    #          'idfilestorage': construction_object.idfilestorage})
    #     DBSession.commit()
    #
    # def filter_construction_objects(self, params):
    #     meetings_type_id = params.get('meeting')
    #     construction_object_name = params.get('construction_objectName')
    #     construction_object_num = params.get('construction_objectNumber')
    #     date_start = params.get('dateStart')
    #     date_end = params.get('dateEnd')
    #
    #     construction_objects = DBSession.query(ConstructionObjects)
    #
    #     if meetings_type_id:
    #         construction_objects = construction_objects.filter_by(meetings_type_id=meetings_type_id)
    #     if construction_object_name:
    #         construction_object_name = '%' + construction_object_name + '%'
    #         construction_objects = construction_objects.filter(ConstructionObjects.construction_object_name.ilike(construction_object_name))
    #     if construction_object_num:
    #         construction_object_num = '%' + construction_object_num + '%'
    #         construction_objects = construction_objects.filter(ConstructionObjects.construction_object_num.ilike(construction_object_num))
    #     if date_start:
    #         construction_objects = construction_objects.filter(ConstructionObjects.construction_object_date >= date_start)
    #     if date_end:
    #         construction_objects = construction_objects.filter(ConstructionObjects.construction_object_date <= date_end)
    #
    #     return construction_objects.all()
