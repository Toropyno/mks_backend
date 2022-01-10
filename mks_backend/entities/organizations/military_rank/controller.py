from pyramid.httpexceptions import HTTPNoContent
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .serializer import MilitaryRankSerializer
from .service import MilitaryRankService
from .schema import MilitaryRankSchema


@view_defaults(renderer='json')
class MilitaryRankController:

    def __init__(self, request: Request):
        self.request = request
        self.service = MilitaryRankService()
        self.serializer = MilitaryRankSerializer()
        self.schema = MilitaryRankSchema()

    @view_config(route_name='get_all_military_ranks')
    def get_all_military_ranks(self):
        military_ranks = self.service.get_all_military_ranks()
        return self.serializer.convert_list_to_json(military_ranks)

    @view_config(route_name='get_military_rank')
    def get_military_rank(self):
        id_ = self.get_id()
        military_rank = self.service.get_military_rank_by_id(id_)
        return self.serializer.to_json(military_rank)

    @view_config(route_name='add_military_rank')
    def add_military_rank(self):
        military_rank_deserialized = self.schema.deserialize(self.request.json_body)
        military_rank = self.serializer.to_mapped_object(military_rank_deserialized)

        self.service.add_military_rank(military_rank)
        return {'id': military_rank.military_ranks_id}

    @view_config(route_name='edit_military_rank')
    def edit_military_rank(self):
        id_ = self.get_id()
        military_rank_deserialized = self.schema.deserialize(self.request.json_body)
        military_rank_deserialized['id'] = id_

        military_rank = self.serializer.to_mapped_object(military_rank_deserialized)
        self.service.update_military_rank(military_rank)
        return {'id': id_}

    @view_config(route_name='delete_military_rank')
    def delete_military_rank(self):
        id_ = self.get_id()
        self.service.delete_military_rank_by_id(id_)
        return HTTPNoContent()

    def get_id(self):
        return int(self.request.matchdict.get('id'))
