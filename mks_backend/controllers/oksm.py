from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.controllers.schemas.oksm import OKSMSchema
from mks_backend.serializers.oksm import OKSMSerializer
from mks_backend.services.oksm import OKSMService

from mks_backend.errors import handle_colander_error, handle_db_error


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

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_oksm')
    def add_oksm(self):
        oksm_deserialized = self.schema.deserialize(self.request.json_body)

        oksm = self.serializer.convert_schema_to_object(oksm_deserialized)
        self.service.add_oksm(oksm)
        return {'id': oksm.oksm_id}

    @view_config(route_name='delete_oksm')
    def delete_oksm(self):
        id = self.get_id()
        self.service.delete_oksm_by_id(id)
        return {'id': id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_oksm')
    def edit_oksm(self):
        oksm_deserialized = self.schema.deserialize(self.request.json_body)
        oksm_deserialized['id'] = self.get_id()

        new_oksm = self.serializer.convert_schema_to_object(oksm_deserialized)
        self.service.update_oksm(new_oksm)
        return {'id': new_oksm.oksm_id}

    @view_config(route_name='get_oksm')
    def get_oksm(self):
        id = self.get_id()
        oksm = self.service.get_oksm_by_id(id)
        return self.serializer.convert_object_to_json(oksm)

    def get_id(self):
        return int(self.request.matchdict['id'])
