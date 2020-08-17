from pyramid.view import view_config


class CommissionController:

    def __init__(self, request):
        self.request = request
        # self.serializer = CommissionSerializer()
        # self.service = CommissionService()

    @view_config(route_name='commissions', request_method='GET', renderer='json')
    def get_all_commissions(self):
        if self.request.params:
            message = 'Request to get all commissions by GET with query params (filter)'
            # params_schema = CommissionControllerFilterSchema()
            # try:
            #     params_deserialized = params_schema.deserialize(self.request.GET)
            # except colander.Invalid as error:
            #     return Response(status=403, json_body=error.asdict())
            # except ValueError as date_parse_error:
            #     return Response(status=403, json_body=date_parse_error.args)
            # params = self.service.get_params_from_schema(params_deserialized)
            # commissions = self.service.filter_commissions(params)
        else:
            message = 'Request to get all commissions by GET without query params'
            # commissions = self.service.get_all_commissions()

        # json = self.serializer.convert_list_to_json(commissions)
        # return json
        return message

    @view_config(route_name='add_commission', request_method='POST', renderer='json')
    def add_commission(self):
        # commission_schema = CommissionControllerSchema()
        # try:
        #     commission_deserialized = commission_schema.deserialize(self.request.json_body)
        # except colander.Invalid as error:
        #     return Response(status=403, json_body=error.asdict())
        # except ValueError as date_parse_error:
        #     return Response(status=403, json_body=date_parse_error.args)
        # commission = self.serializer.convert_schema_to_object(commission_deserialized)
        # self.service.add_commission(commission)
        return {'id': 'commission.commission_id'}

    @view_config(route_name='commission_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_commission(self):
        # id = self.request.matchdict['id']
        # self.service.delete_commission_by_id(id)
        return {'id': 'deleted id'}

    @view_config(route_name='commission_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_commission(self):
        # commission_schema = CommissionControllerSchema()
        id = self.request.matchdict['id']
        # try:
        #     commission_deserialized = commission_schema.deserialize(self.request.json_body)
        # except colander.Invalid as error:
        #     return Response(status=403, json_body=error.asdict())
        # except ValueError as date_parse_error:
        #     return Response(status=403, json_body=date_parse_error.args)
        # commission_deserialized['id'] = id
        # new_commission = self.serializer.convert_schema_to_object(commission_deserialized)
        # new_commission = self.service.update_commission(new_commission)
        return {'id': id}

    @view_config(route_name='commission_delete_change_and_view', request_method='GET', renderer='json')
    def get_commission(self):
        # id = self.request.matchdict['id']
        # commission = self.service.get_commission_by_id(id)
        # json = self.serializer.convert_object_to_json(commission)
        return {'some_object_to_json'}
