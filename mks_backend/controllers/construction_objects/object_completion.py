from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.serializers.construction_objects.object_completion import ObjectCompletionSerializer
from mks_backend.services.construction_objects.object_completion import ObjectCompletionService


@view_defaults(renderer='json')
class ObjectCompletionController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ObjectCompletionService()
        self.serializer = ObjectCompletionSerializer()

    @view_config(route_name='get_object_completion_by_object')
    def get_object_completion_by_object(self):
        object_id = self.request.matchdict.get('id')
        object_completion = self.service.get_object_completion_by_construction_object_id(object_id)

        return self.serializer.convert_list_to_json(object_completion)
