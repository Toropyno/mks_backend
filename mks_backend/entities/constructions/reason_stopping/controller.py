from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .schema import ReasonStoppingSchema
from .serializer import ReasonStoppingSerializer
from .service import ReasonStoppingService


@view_defaults(renderer='json')
class ReasonStoppingController:

    def __init__(self, request: Request):
        self.request = request
        self.service = ReasonStoppingService()
        self.serializer = ReasonStoppingSerializer()
        self.schema = ReasonStoppingSchema()

    @view_config(route_name='get_all_reason_stoppings')
    def get_all_reason_stoppings(self):
        reason_stoppings = self.service.get_all_reason_stoppings()
        return self.serializer.convert_list_to_json(reason_stoppings)

    @view_config(route_name='add_reason_stopping')
    def add_reason_stopping(self):
        reason_stopping_deserialized = self.schema.deserialize(self.request.json_body)
        reason_stopping = self.serializer.convert_schema_to_object(reason_stopping_deserialized)
        self.service.add_reason_stopping(reason_stopping)
        return {'id': reason_stopping.reasons_stopping_id}

    @view_config(route_name='delete_reason_stopping')
    def delete_reason_stopping(self):
        id_ = self.get_id()
        self.service.delete_reason_stopping_by_id(id_)
        return {'id': id_}

    @view_config(route_name='edit_reason_stopping')
    def edit_reason_stopping(self):
        reason_stopping_deserialized = self.schema.deserialize(self.request.json_body)
        reason_stopping_deserialized['id'] = self.get_id()
        new_reason_stopping = self.serializer.convert_schema_to_object(reason_stopping_deserialized)
        self.service.update_reason_stopping(new_reason_stopping)
        return {'id': new_reason_stopping.reasons_stopping_id}

    @view_config(route_name='get_reason_stopping')
    def get_reason_stopping(self):
        id_ = self.get_id()
        reason_stopping = self.service.get_reason_stopping_by_id(id_)
        return self.serializer.to_json(reason_stopping)

    def get_id(self):
        return int(self.request.matchdict['id'])
