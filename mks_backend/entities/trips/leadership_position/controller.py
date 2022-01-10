from pyramid.httpexceptions import HTTPNoContent
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import LeadershipPositionSchema
from .serializer import LeadershipPositionSerializer
from .service import LeadershipPositionService


@view_defaults(renderer='json')
class LeadershipPositionController:

    def __init__(self, request: Request):
        self.request = request
        self.service = LeadershipPositionService()
        self.serializer = LeadershipPositionSerializer()
        self.schema = LeadershipPositionSchema()

    @view_config(route_name='get_all_leadership_positions')
    def get_all_leadership_positions(self):
        leadership_positions = self.service.get_all_leadership_positions()
        return self.serializer.convert_list_to_json(leadership_positions)

    @view_config(route_name='add_leadership_position')
    def add_leadership_position(self):
        leadership_position_deserialized = self.schema.deserialize(self.request.json_body)

        leadership_position = self.serializer.to_mapped_object(leadership_position_deserialized)
        self.service.add_leadership_position(leadership_position)
        return {'id': leadership_position.leadership_positions_id}

    @view_config(route_name='delete_leadership_position')
    def delete_leadership_position(self):
        id_ = self.get_id()
        self.service.delete_leadership_position_by_id(id_)
        return HTTPNoContent()

    @view_config(route_name='edit_leadership_position')
    def edit_leadership_position(self):
        leadership_position_deserialized = self.schema.deserialize(self.request.json_body)
        leadership_position_deserialized['id'] = self.get_id()

        new_leadership_position = self.serializer.to_mapped_object(leadership_position_deserialized)
        self.service.update_leadership_position(new_leadership_position)
        return {'id': new_leadership_position.leadership_positions_id}

    @view_config(route_name='get_leadership_position')
    def get_leadership_position(self):
        id_ = self.get_id()
        leadership_position = self.service.get_leadership_position_by_id(id_)
        return self.serializer.to_json(leadership_position)

    def get_id(self) -> int:
        return int(self.request.matchdict['id'])
