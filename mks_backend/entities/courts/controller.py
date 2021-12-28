from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import CourtSchema
from .serializer import CourtSerializer
from .service import CourtService


@view_defaults(renderer='json')
class CourtController:

    def __init__(self, request: Request):
        self.request = request
        self.service = CourtService()
        self.serializer = CourtSerializer()
        self.schema = CourtSchema()

    @view_config(route_name='get_all_courts')
    def get_all_courts(self):
        courts = self.service.get_all_courts()
        return self.serializer.convert_list_to_json(courts)

    @view_config(route_name='add_court')
    def add_court(self):
        court_deserialized = self.schema.deserialize(self.request.json_body)
        court = self.serializer.to_mapped_object(court_deserialized)
        self.service.add_court(court)
        return {'id': court.courts_id}

    @view_config(route_name='delete_court')
    def delete_court(self):
        id_ = self.get_id()
        self.service.delete_court_by_id(id_)
        return {'id': id_}

    @view_config(route_name='edit_court')
    def edit_court(self):
        court_deserialized = self.schema.deserialize(self.request.json_body)
        court_deserialized['id'] = self.get_id()

        new_court = self.serializer.to_mapped_object(court_deserialized)
        self.service.update_court(new_court)
        return {'id': new_court.courts_id}

    @view_config(route_name='get_court')
    def get_court(self):
        id_ = self.get_id()
        court = self.service.get_court_by_id(id_)
        return self.serializer.to_json(court)

    def get_id(self):
        return int(self.request.matchdict['id'])
