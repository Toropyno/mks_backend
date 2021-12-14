from pyramid.request import Request
from pyramid.view import view_defaults, view_config

from .service import ClassRankService

from .model import ClassRank
from .serializer import ClassRankSerializer


@view_defaults(renderer='json')
class ClassRankController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ClassRankService(ClassRank)
        self.serializer = ClassRankSerializer()

    @view_config(route_name='get_all_class_ranks')
    def get_all_class_ranks(self):
        return self.service.get_all_class_ranks()

    @view_config(route_name='add_class_rank')
    def add_class_rank(self):
        class_rank = self.serializer.to_mapped_object(self.request.json_body)
        self.service.add_class_rank(class_rank)
        return {'id': class_rank.id}

    @view_config(route_name='edit_class_rank')
    def edit_class_rank(self):
        form_data = self.request.json_body
        form_data['id'] = self.request.matchdict.get('id')

        class_rank = self.serializer.to_mapped_object(form_data)
        self.service.edit_class_rank(class_rank)
        return {'id': class_rank.id}

    @view_config(route_name='get_class_rank')
    def get_class_rank(self):
        id = self.get_id()
        class_rank = self.service.get_class_rank(id)
        return self.serializer.to_json(class_rank)

    @view_config(route_name='delete_class_rank')
    def delete_class_rank(self):
        id_ = self.request.matchdict.get('id')
        self.service.delete_class_rank(id_)
        return {'id': int(id_)}

    def get_id(self):
        return int(self.request.matchdict.get('id'))
