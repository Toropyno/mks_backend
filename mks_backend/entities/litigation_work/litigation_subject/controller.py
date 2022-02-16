from pyramid.httpexceptions import HTTPCreated, HTTPNoContent
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.entities.constructions.construction import ConstructionSerializer

from .schema import LitigationSubjectSchema
from .serializer import LitigationSubjectSerializer
from .service import LitigationSubjectService


@view_defaults(renderer='json')
class LitigationSubjectController:

    def __init__(self, request: Request):
        self.request = request
        self.schema = LitigationSubjectSchema()
        self.service = LitigationSubjectService()
        self.construction_serializer = ConstructionSerializer()
        self.serializer = LitigationSubjectSerializer()

    @view_config(route_name='get_litigation_subjects_by_litigation')
    def get_litigation_subjects_by_litigation(self):
        litigation_id = int(self.request.matchdict.get('litigation_id'))
        litigation_subjects = self.service.get_litigation_subjects_by_litigation(litigation_id)
        return self.construction_serializer.convert_list_to_json(litigation_subjects)

    @view_config(route_name='delete_litigation_subject')
    def delete_litigation_subject(self):
        litigation_id = int(self.request.matchdict.get('litigation_id'))
        construction_id = int(self.request.matchdict.get('construction_id'))

        self.service.delete_litigation_subject(litigation_id, construction_id)
        return HTTPNoContent()

    @view_config(route_name='add_litigation_subject')
    def add_litigation_subject(self):
        litigation_id = int(self.request.matchdict.get('litigation_id'))

        litigation_subjects_deserialized = self.schema.deserialize(self.request.json_body)['constructions']
        litigation_subjects = self.serializer.convert_list_to_objects(
            litigation_id, litigation_subjects_deserialized
        )

        self.service.add_litigation_subjects(litigation_subjects)
        return HTTPCreated(json_body={'litigation_id': litigation_id})
