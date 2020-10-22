from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from mks_backend.controllers.schemas.fias import FIASSchema
from mks_backend.errors.handle_controller_error import handle_db_error, handle_colander_error
from mks_backend.models.fias import FIAS
from mks_backend.serializers.fias import FIASSerializer
from mks_backend.services.fias_entity.api import FIASAPIService
from mks_backend.services.fias_entity.fias import FIASService
from mks_backend.services.fias_entity.utils import get_search_address


@view_defaults(renderer='json')
class FIASController:

    def __init__(self, request: Request):
        self.request = request
        self.schema = FIASSchema()
        self.service = FIASService()
        self.serializer = FIASSerializer()
        self.service_api = FIASAPIService()

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_fias')
    def add_fias(self):
        fias = self.get_fias_serialized()

        search_address = get_search_address(fias)
        if search_address == '':
            return [
                {'status': 403},
                {
                    'json_body': {
                        'code': 'not_full_address',
                        'message': 'Адрес заполнен не полностью'
                    }
                }
            ]

        aoid = self.service_api.get_AOID(search_address)

        fias_db = self.service.get_fias_by_aoid(aoid)
        if not fias_db:
            fias.aoid = aoid
            self.service.add_fias(fias)
            return {'id': fias.id}

        return {'id': fias_db.id}

    @handle_db_error
    @view_config(route_name='get_fias')
    def get_fias(self):
        id = self.get_id()
        fias = self.service.get_fias_by_id(id)
        return self.serializer.convert_object_to_json(fias)

    @handle_db_error
    @view_config(route_name='get_all_fiases')
    def get_all_fiases(self):
        fiases = self.service.get_all_fiases()
        return self.serializer.convert_list_to_json(fiases)

    @handle_db_error
    @view_config(route_name='delete_fias')
    def delete_fias(self):
        id = int(self.request.matchdict['id'])
        construction_id = int(self.request.matchdict['constructionId'])
        self.service.delete_last_fias_by_id_and_construction_id(id, construction_id)
        return {'id': id}

    def get_fias_serialized(self) -> FIAS:
        fias_deserialized = self.schema.deserialize(self.request.json_body)
        return self.serializer.convert_schema_to_object(fias_deserialized)

    def get_id(self):
        return int(self.request.matchdict['id'])
