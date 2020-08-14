from pyramid.view import view_config


class ConstructionController:

    def __init__(self, request):
        self.request = request
        # self.serializer = ConstructionSerializer()
        # self.service = ConstructionService()

    @view_config(route_name='constructions', request_method='GET', renderer='json')
    def get_all_constructions(self):
        if self.request.params:
            message = 'Request to get all constructions by GET with query params (filter)'
            # params_schema = ConstructionControllerFilterSchema()
            # try:
            #     params_deserialized = params_schema.deserialize(self.request.GET)
            # except colander.Invalid as error:
            #     return Response(status=403, json_body=error.asdict())
            # except ValueError as date_parse_error:
            #     return Response(status=403, json_body=date_parse_error.args)
            # params = self.service.get_params_from_schema(params_deserialized)
            # constructions = self.service.filter_constructions(params)
        else:
            message = 'Request to get all constructions by GET without query params'
            # constructions = self.service.get_all_constructions()

        # json = self.serializer.convert_list_to_json(constructions)
        # return json
        return message

    @view_config(route_name='add_construction', request_method='POST', renderer='json')
    def add_construction(self):
        # construction_schema = ConstructionControllerSchema()
        # try:
        #     construction_deserialized = construction_schema.deserialize(self.request.json_body)
        # except colander.Invalid as error:
        #     return Response(status=403, json_body=error.asdict())
        # except ValueError as date_parse_error:
        #     return Response(status=403, json_body=date_parse_error.args)
        # construction = self.serializer.convert_schema_to_object(construction_deserialized)
        # self.service.add_construction(construction)
        return {'id': 'construction.construction_id'}

    @view_config(route_name='construction_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_construction(self):
        # id = self.request.matchdict['id']
        # self.service.delete_construction_by_id(id)
        return {'id': 'deleted id'}

    @view_config(route_name='construction_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_construction(self):
        # construction_schema = ConstructionControllerSchema()
        # id = self.request.matchdict['id']
        # try:
        #     construction_deserialized = construction_schema.deserialize(self.request.json_body)
        # except colander.Invalid as error:
        #     return Response(status=403, json_body=error.asdict())
        # except ValueError as date_parse_error:
        #     return Response(status=403, json_body=date_parse_error.args)
        # construction_deserialized['id'] = id
        # new_construction = self.serializer.convert_schema_to_object(construction_deserialized)
        # new_construction = self.service.update_construction(new_construction)
        return {'id': 'new_construction.construction_id'}

    @view_config(route_name='construction_delete_change_and_view', request_method='GET', renderer='json')
    def get_construction(self):
        # id = self.request.matchdict['id']
        # construction = self.service.get_construction_by_id(id)
        # json = self.serializer.convert_object_to_json(construction)
        return {'some_object_to_json'}
