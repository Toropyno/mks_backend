from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.controllers.schemas.constructions import CommissionSchema
from mks_backend.serializers.constructions.commision import CommissionSerializer
from mks_backend.services.constructions.commission import CommissionService

from mks_backend.errors import handle_db_error, handle_colander_error


@view_defaults(renderer='json')
class CommissionController:

    def __init__(self, request: Request):
        self.request = request
        self.service = CommissionService()
        self.serializer = CommissionSerializer()
        self.schema = CommissionSchema()

    @view_config(route_name='get_all_commissions')
    def get_all_commissions(self):
        commissions = self.service.get_all_commissions()
        return self.serializer.convert_list_to_json(commissions)

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='add_commission')
    def add_commission(self):
        commission_deserialized = self.schema.deserialize(self.request.json_body)
        commission = self.serializer.convert_schema_to_object(commission_deserialized)
        self.service.add_commission(commission)
        return {'id': commission.commission_id}

    @handle_db_error
    @view_config(route_name='delete_commission')
    def delete_commission(self):
        id = self.get_id()
        self.service.delete_commission_by_id(id)
        return {'id': id}

    @handle_db_error
    @handle_colander_error
    @view_config(route_name='edit_commission')
    def edit_commission(self):
        commission_deserialized = self.schema.deserialize(self.request.json_body)
        commission_deserialized['id'] = self.request.matchdict['id']

        new_commission = self.serializer.convert_schema_to_object(commission_deserialized)
        self.service.update_commission(new_commission)
        return {'id': new_commission.commission_id}

    @handle_db_error
    @view_config(route_name='get_commission')
    def get_commission(self):
        id = self.get_id()
        commission = self.service.get_commission_by_id(id)
        return self.serializer.convert_object_to_json(commission)

    def get_id(self):
        return int(self.request.matchdict['id'])
