from pyramid.request import Request
from pyramid.view import view_config

from mks_backend.serializers.organizations.military_rank import MilitaryRankSerializer
from mks_backend.services.organizations.military_rank import MilitaryRankService
from mks_backend.controllers.schemas.organizations.military_rank import MilitaryRankSchema

from mks_backend.errors.handle_controller_error import handle_colander_error, handle_db_error


class MilitaryRankController:

    def __init__(self, request: Request):
        self.request = request
        self.service = MilitaryRankService()
        self.serializer = MilitaryRankSerializer()
        self.schema = MilitaryRankSchema()

    @view_config(route_name='get_all_military_ranks', renderer='json')
    def get_all_military_ranks(self):
        military_ranks = self.service.get_all_military_ranks()
        return self.serializer.convert_list_to_json(military_ranks)

    @view_config(route_name='get_military_rank', renderer='json')
    def get_military_rank(self):
        id = self.get_id()
        military_rank = self.service.get_military_rank_by_id(id)
        return self.serializer.to_json(military_rank)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_military_rank', renderer='json')
    def add_military_rank(self):
        military_rank_deserialized = self.schema.deserialize(self.request.json_body)
        military_rank = self.serializer.convert_schema_to_object(military_rank_deserialized)

        self.service.add_military_rank(military_rank)
        return {'id': military_rank.military_ranks_id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_military_rank', renderer='json')
    def edit_military_rank(self):
        id = self.get_id()
        military_rank_deserialized = self.schema.deserialize(self.request.json_body)
        military_rank_deserialized['id'] = id

        military_rank = self.serializer.convert_schema_to_object(military_rank_deserialized)
        self.service.update_military_rank(military_rank)
        return {'id': id}

    @view_config(route_name='delete_military_rank', renderer='json')
    def delete_military_rank(self):
        id = self.get_id()
        self.service.delete_military_rank_by_id(id)
        return {'id': id}

    def get_id(self):
        return int(self.request.matchdict.get('id'))
