from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .serializer import CompletionDateSerializer
from .service import CompletionDateService
from .schema import CompletionDateSchema


@view_defaults(renderer='json')
class CompletionDateController:

    def __init__(self, request: Request):
        self.request = request
        self.schema = CompletionDateSchema()
        self.service = CompletionDateService()
        self.serializer = CompletionDateSerializer()

    @view_config(route_name='add_completion_date')
    def add(self):
        completion_date_deserialized = self.schema.deserialize(self.request.json_body)
        completion_date = self.serializer.to_mapped_object(completion_date_deserialized)

        self.service.add(completion_date)
        return {'id': completion_date.completion_dates_id}

    @view_config(route_name='edit_completion_date')
    def edit(self):
        id = self.get_id()
        completion_date_deserialized = self.schema.deserialize(self.request.json_body)
        completion_date_deserialized['id'] = id
        completion_date = self.serializer.to_mapped_object(completion_date_deserialized)

        self.service.update(completion_date)
        return {'id': id}

    @view_config(route_name='get_all_completion_dates_by_contract')
    def get_all(self):
        contract_id = self.request.matchdict.get('id')
        completion_dates = self.service.get_all_completion_dates_by_contract_id(contract_id)
        return self.serializer.convert_list_to_json(completion_dates)

    @view_config(route_name='get_completion_date')
    def get(self):
        id = self.get_id()
        completion_date = self.service.get_by_id(id)
        return self.serializer.to_json(completion_date)

    @view_config(route_name='delete_completion_date')
    def delete(self):
        id = self.get_id()
        self.service.delete_by_id(id)
        return {'id': id}

    def get_id(self):
        return int(self.request.matchdict.get('id'))
