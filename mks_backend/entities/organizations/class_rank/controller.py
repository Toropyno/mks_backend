from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from .service import ClassRankService
from .serializer import ClassRankSerializer
from .schema import ClassRankSchema


@view_defaults(renderer='json')
class ClassRankController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ClassRankService()
        self.serializer = ClassRankSerializer()
        self.schema = ClassRankSchema()

    @view_config(route_name='get_all_class_ranks')
    def get_all_class_ranks(self):
        class_ranks = self.service.get_all_class_ranks()
        return self.serializer.convert_list_to_json(class_ranks)

    @view_config(route_name='add_class_rank')
    def add_class_rank(self):
        class_rank_deserialized = self.schema.deserialize(self.request.json_body)
        class_rank = self.serializer.convert_schema_to_object(class_rank_deserialized)

        self.service.add_class_rank(class_rank)
        return {'id': class_rank.class_ranks_id}

    @view_config(route_name='update_class_rank')
    def update_class_rank(self):
        class_rank_deserialized = self.schema.deserialize(self.request.json_body)
        class_rank_deserialized['id'] = self.get_id()
        new_class_rank = self.serializer.convert_schema_to_object(class_rank_deserialized)
        self.service.update_class_rank(new_class_rank)
        return {'id': new_class_rank.class_ranks_id}

    @view_config(route_name='get_class_rank')
    def get_class_rank(self):
        id = self.get_id()
        class_rank = self.service.get_class_rank(id)
        return self.serializer.to_json(class_rank)

    @view_config(route_name='delete_class_rank')
    def delete_class_rank(self):
        id_ = self.get_id()
        self.service.delete_class_rank(id_)
        return {'id': int(id_)}

    def get_id(self):
        return int(self.request.matchdict.get('id'))
