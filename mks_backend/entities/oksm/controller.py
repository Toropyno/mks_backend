from pyramid.httpexceptions import HTTPCreated, HTTPNoContent
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import OKSMSchema
from .serializer import OKSMSerializer
from .service import OKSMService


@view_defaults(renderer='json')
class OKSMController:

    def __init__(self, request: Request):
        self.request = request
        self.service = OKSMService()
        self.serializer = OKSMSerializer()
        self.schema = OKSMSchema()

    @view_config(route_name='get_all_oksms')
    def get_all_oksms(self):
        oksms = self.service.get_all_oksms()
        return self.serializer.convert_list_to_json(oksms)

    @view_config(route_name='add_oksm')
    def add_oksm(self):
        oksm_deserialized = self.schema.deserialize(self.request.json_body)

        oksm = self.serializer.to_mapped_object(oksm_deserialized)
        self.service.add_oksm(oksm)
        return HTTPCreated(json_body={'id': oksm.oksm_id})

    @view_config(route_name='delete_oksm')
    def delete_oksm(self):
        id_ = self.get_id()
        self.service.delete_oksm_by_id(id_)
        return HTTPNoContent()

    @view_config(route_name='edit_oksm')
    def edit_oksm(self):
        oksm_deserialized = self.schema.deserialize(self.request.json_body)
        oksm_deserialized['id'] = self.get_id()

        new_oksm = self.serializer.to_mapped_object(oksm_deserialized)
        self.service.update_oksm(new_oksm)
        return {'id': new_oksm.oksm_id}

    @view_config(route_name='get_oksm')
    def get_oksm(self):
        id_ = self.get_id()
        oksm = self.service.get_oksm_by_id(id_)
        return self.serializer.to_json(oksm)

    def get_id(self):
        return int(self.request.matchdict['id'])
