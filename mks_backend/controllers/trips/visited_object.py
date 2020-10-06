from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.controllers.schemas.trips.visited_object import VisitedObjectSchema
from mks_backend.serializers.construction import ConstructionSerializer
from mks_backend.serializers.trips.visited_object import VisitedObjectSerializer
from mks_backend.services.trips.visited_object import VisitedObjectService


@view_defaults(renderer='json')
class VisitedObjectController:

    def __init__(self, request: Request):
        self.request = request
        self.schema = VisitedObjectSchema()
        self.service = VisitedObjectService()
        self.construction_serializer = ConstructionSerializer()
        self.serializer = VisitedObjectSerializer()

    @view_config(route_name='get_visited_objects_by_work_trip')
    def get_visited_objects_by_work_trip(self):
        work_trip_id = int(self.request.matchdict.get('work_trip_id'))
        visited_objects = self.service.get_visited_objects_by_work_trip(work_trip_id)
        return self.construction_serializer.convert_list_to_json(visited_objects)

    @view_config(route_name='delete_visited_object')
    def delete_visited_object(self):
        work_trip_id = int(self.request.matchdict.get('work_trip_id'))
        construction_id = int(self.request.matchdict.get('construction_id'))
        self.service.delete_visited_object(work_trip_id, construction_id)
        return {
            'id': '{work_trip_id}, {construction_id}'.format(work_trip_id=work_trip_id, construction_id=construction_id)
        }

    @view_config(route_name='add_visited_object')
    def add_visited_object(self):
        work_trip_id = int(self.request.matchdict.get('work_trip_id'))

        visited_objects = self.serializer.convert_list_to_objects(
            work_trip_id, self.schema.deserialize(self.request.json_body)['constructions']
        )
        self.service.add_visited_objects(visited_objects)
        return {'work_trip_id': work_trip_id}
