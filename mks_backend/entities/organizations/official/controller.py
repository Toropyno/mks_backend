from pyramid.view import view_config, view_defaults
from pyramid.request import Request

from .schema import OfficialSchema, OfficialFilterSchema
from .serializer import OfficialSerializer
from .service import OfficialService


@view_defaults(renderer='json')
class OfficialController:

    def __init__(self, request: Request):
        self.request = request
        self.service = OfficialService()
        self.serializer = OfficialSerializer()

        self.schema = OfficialSchema()
        self.filter_schema = OfficialFilterSchema()

    @view_config(route_name='add_official')
    def add_official(self):
        official_deserialized = self.schema.deserialize(self.request.json_body)
        official = self.serializer.to_mapped_object(official_deserialized)

        self.service.add_official(official)
        return {'id': official.officials_id}

    @view_config(route_name='edit_official')
    def edit_official(self):
        id_ = self.get_id()
        official_deserialized = self.schema.deserialize(self.request.json_body)
        official_deserialized['id'] = id_

        official = self.serializer.to_mapped_object(official_deserialized)

        self.service.update_official(official)
        return {'id': id_}

    @view_config(route_name='delete_official')
    def delete_official(self):
        id_ = self.get_id()
        self.service.delete_official_by_id(id_)
        return {'id': id_}

    @view_config(route_name='get_officials_by_organization')
    def get_officials_by_organization(self):
        filter_fields = self.filter_schema.deserialize({**self.request.params, **self.request.matchdict})
        officials = self.service.get_officials_by_organization(filter_fields)
        return self.serializer.convert_list_to_json(officials)

    @view_config(route_name='get_official_by_id')
    def get_official(self):
        official = self.service.get_official(self.get_id())
        return self.serializer.to_json(official)

    def get_id(self):
        return int(self.request.matchdict.get('id'))
