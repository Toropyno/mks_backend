from pyramid.httpexceptions import HTTPNoContent
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import CourtDecisionSchema
from .serializer import CourtDecisionSerializer
from .service import CourtDecisionService


@view_defaults(renderer='json')
class CourtDecisionController:

    def __init__(self, request: Request):
        self.request = request
        self.service = CourtDecisionService()
        self.serializer = CourtDecisionSerializer()
        self.schema = CourtDecisionSchema()

    @view_config(route_name='get_all_court_decisions')
    def get_all_court_decisions(self):
        court_decisions = self.service.get_all_court_decisions()
        return self.serializer.convert_list_to_json(court_decisions)

    @view_config(route_name='add_court_decision')
    def add_court_decision(self):
        court_decision_deserialized = self.schema.deserialize(self.request.json_body)
        court_decision = self.serializer.to_mapped_object(court_decision_deserialized)
        self.service.add_court_decision(court_decision)
        return {'id': court_decision.court_decisions_id}

    @view_config(route_name='delete_court_decision')
    def delete_court_decision(self):
        id = self.get_id()
        self.service.delete_court_decision_by_id(id)
        return HTTPNoContent()

    @view_config(route_name='edit_court_decision')
    def edit_court_decision(self):
        court_decision_deserialized = self.schema.deserialize(self.request.json_body)
        court_decision_deserialized['id'] = self.get_id()
        new_court_decision = self.serializer.to_mapped_object(court_decision_deserialized)
        self.service.update_court_decision(new_court_decision)
        return {'id': new_court_decision.court_decisions_id}

    @view_config(route_name='get_court_decision')
    def get_court_decision(self):
        id = self.get_id()
        court_decision = self.service.get_court_decision_by_id(id)
        return self.serializer.to_json(court_decision)

    def get_id(self):
        return int(self.request.matchdict['id'])
