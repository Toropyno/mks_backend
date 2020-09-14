import colander
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.request import Request

from mks_backend.services.commission import CommissionService
from mks_backend.serializers.commision import CommissionSerializer
from mks_backend.controllers.schemas.commission import CommissionSchema
from mks_backend.errors.db_basic_error import DBBasicError
from mks_backend.errors.colavder_error import get_dictionary_with_errors_correct_format


class CommissionController:

    def __init__(self, request: Request):
        self.request = request
        self.service = CommissionService()
        self.serializer = CommissionSerializer()
        self.schema = CommissionSchema()

    @view_config(route_name='commissions', request_method='GET', renderer='json')
    def get_all_commissions(self):
        commissions = self.service.get_all_commissions()
        return self.serializer.convert_list_to_json(commissions)

    @view_config(route_name='add_commission', request_method='POST', renderer='json')
    def add_commission(self):
        try:
            commission_deserialized = self.schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=get_dictionary_with_errors_correct_format(error.asdict()))

        commission = self.serializer.convert_schema_to_object(commission_deserialized)
        try:
            self.service.add_commission(commission)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': commission.commission_id}

    @view_config(route_name='commission_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_commission(self):
        id = int(self.request.matchdict['id'])
        self.service.delete_commission_by_id(id)
        return {'id': id}

    @view_config(route_name='commission_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_commission(self):
        try:
            commission_deserialized = self.schema.deserialize(self.request.json_body)
            commission_deserialized['id'] = self.request.matchdict['id']
        except colander.Invalid as error:
            return Response(status=403,json_body=get_dictionary_with_errors_correct_format(error.asdict()))

        new_commission = self.serializer.convert_schema_to_object(commission_deserialized)
        try:
            self.service.update_commission(new_commission)
        except DBBasicError as error:
            return Response(
                status=403,
                json_body={
                    'code': error.code,
                    'message': error.message
                }
            )

        return {'id': new_commission.commission_id}

    @view_config(route_name='commission_delete_change_and_view', request_method='GET', renderer='json')
    def get_commission(self):
        id = int(self.request.matchdict['id'])
        commission = self.service.get_commission_by_id(id)
        return self.serializer.convert_object_to_json(commission)
