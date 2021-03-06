from pyramid.httpexceptions import HTTPCreated, HTTPNoContent
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import LitigationFilterSchema, LitigationSchema
from .serializer import LitigationSerializer
from .service import LitigationService


@view_defaults(renderer='json')
class LitigationController:

    def __init__(self, request: Request):
        self.request = request
        self.service = LitigationService()
        self.serializer = LitigationSerializer()
        self.schema = LitigationSchema()
        self.filter_schema = LitigationFilterSchema()

    @view_config(route_name='get_all_litigations')
    def get_all_litigations(self):
        filter_params = self.filter_schema.deserialize(self.request.params)
        litigations = self.service.get_litigations(filter_params)
        return self.serializer.convert_list_to_json(litigations)

    @view_config(route_name='add_litigation')
    def add_litigation(self):
        litigation_deserialized = self.schema.deserialize(self.request.json_body)
        litigation = self.serializer.to_mapped_object(litigation_deserialized)
        self.service.add_litigation(litigation)
        return HTTPCreated(json_body={'id': litigation.litigation_id})

    @view_config(route_name='delete_litigation')
    def delete_litigation(self):
        id_ = self.get_id()
        self.service.delete_litigation_by_id(id_)
        return HTTPNoContent()

    @view_config(route_name='edit_litigation')
    def edit_litigation(self):
        litigation_deserialized = self.schema.deserialize(self.request.json_body)
        litigation_deserialized['id'] = self.get_id()
        litigation = self.serializer.to_mapped_object(litigation_deserialized)
        self.service.update_litigation(litigation)
        return {'id': litigation.litigation_id}

    @view_config(route_name='get_litigation')
    def get_litigation(self):
        id_ = self.get_id()
        litigation = self.service.get_litigation_by_id(id_)
        return self.serializer.to_json(litigation)

    def get_id(self):
        return int(self.request.matchdict['id'])
