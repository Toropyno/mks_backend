from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .serializer import ReferenceHistorySerializer
from .service import ReferenceHistoryService


@view_defaults(renderer='json')
class ReferenceHistoryController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ReferenceHistoryService()
        self.serializer = ReferenceHistorySerializer()

    @view_config(route_name='get_reference_history_by_object')
    def get_reference_history_by_object(self):
        object_id = self.request.matchdict.get('id')
        reference_history = self.service.get_reference_history_by_construction_object_id(object_id)

        return self.serializer.convert_list_to_json(reference_history)
