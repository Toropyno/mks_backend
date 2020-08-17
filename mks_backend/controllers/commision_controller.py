import colander
from pyramid.view import view_config
from pyramid.response import Response

from mks_backend.services.commission_service import CommissionService
from mks_backend.serializers.commision_serializer import CommissionSerializer


class CommissionController:

    def __init__(self, request):
        self.request = request
        self.service = CommissionService()
        self.serializer = CommissionSerializer()

    @view_config(route_name='commissions', request_method='GET', renderer='json')
    def get_all_commissions(self):
        commissions = self.service.get_all_commissions()
        json = self.serializer.convert_list_to_json(commissions)
        return json

    @view_config(route_name='add_commission', request_method='POST', renderer='json')
    def add_commission(self):
        commission_schema = CommissionSchema()
        try:
            commission_deserialized = commission_schema.deserialize(self.request.json_body)
            commission = self.service.convert_schema_to_object(commission_deserialized)
            self.service.add_commission(commission)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        except ValueError as error:
            return Response(status=403, json_body={'error': error.args[0]})

        return {'id': commission.commission_id}

    @view_config(route_name='commission_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_commission(self):
        id = self.request.matchdict['id']
        self.service.delete_commission_by_id(id)
        return {'id': id}

    @view_config(route_name='commission_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_commission(self):
        commission_schema = CommissionSchema()
        id = self.request.matchdict['id']
        try:
            commission_deserialized = commission_schema.deserialize(self.request.json_body)
            commission_deserialized['id'] = id

            new_commission = self.service.convert_schema_to_object(commission_deserialized)
            self.service.update_commission(new_commission)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        except ValueError as error:
            return Response(status=403, json_body={'error': error.args[0]})

        return {'id': new_commission.commission_id}

    @view_config(route_name='commission_delete_change_and_view', request_method='GET', renderer='json')
    def get_commission(self):
        id = self.request.matchdict['id']
        commission = self.service.get_commission_by_id(id)
        json = self.serializer.convert_object_to_json(commission)
        return json


class CommissionSchema(colander.MappingSchema):
    code = colander.SchemaNode(
        colander.String(),
        name='code',
        validator=colander.Length(min=1, max=20, min_err='Слишком короткий код комиссиии',
                                  max_err='Слишком длинный код комиссии')
    )

    fullname = colander.SchemaNode(
        colander.String(),
        name='fullName',
        validator=colander.Length(min=1, max=255, min_err='Слишком короткое название комиссии',
                                  max_err='Слишком длинное название комиссии')
    )
