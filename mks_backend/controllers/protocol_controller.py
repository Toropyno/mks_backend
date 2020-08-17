import re
from datetime import datetime

import colander
from pyramid.view import view_config
from pyramid.response import Response

from mks_backend.serializers.protocol_serializer import ProtocolSerializer
from mks_backend.services.protocol_service import ProtocolService


class ProtocolController(object):

    def __init__(self, request):
        self.request = request
        self.serializer = ProtocolSerializer()
        self.service = ProtocolService()

    @view_config(route_name='protocols', request_method='GET', renderer='json')
    def get_all_protocols(self):
        if self.request.params:
            params_schema = ProtocolControllerFilterSchema()
            try:
                params_deserialized = params_schema.deserialize(self.request.GET)
            except colander.Invalid as error:
                return Response(status=403, json_body=error.asdict())
            except ValueError as date_parse_error:
                return Response(status=403, json_body=date_parse_error.args)
            params = self.service.get_params_from_schema(params_deserialized)
            protocols = self.service.filter_protocols(params)
        else:
            protocols = self.service.get_all_protocols()

        json = self.serializer.convert_list_to_json(protocols)
        return json

    @view_config(route_name='add_protocol', request_method='POST', renderer='json')
    def add_protocol(self):
        protocol_schema = ProtocolControllerSchema()
        try:
            protocol_deserialized = protocol_schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        except ValueError as date_parse_error:
            return Response(status=403, json_body=date_parse_error.args)
        protocol = self.serializer.convert_schema_to_object(protocol_deserialized)
        self.service.add_protocol(protocol)
        return {'id': protocol.protocol_id}

    @view_config(route_name='protocols_delete_change_and_view', request_method='GET', renderer='json')
    def get_protocol(self):
        id = self.request.matchdict['id']
        protocol = self.service.get_protocol_by_id(id)
        json = self.serializer.convert_object_to_json(protocol)
        return json

    @view_config(route_name='protocols_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_protocol(self):
        id = self.request.matchdict['id']
        self.service.delete_protocol_by_id_with_filestorage_cascade(id)
        return {'id': id}

    @view_config(route_name='protocols_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_protocol(self):
        protocol_schema = ProtocolControllerSchema()
        id = self.request.matchdict['id']
        try:
            protocol_deserialized = protocol_schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())
        except ValueError as date_parse_error:
            return Response(status=403, json_body=date_parse_error.args)
        protocol_deserialized['id'] = id
        new_protocol = self.serializer.convert_schema_to_object(protocol_deserialized)
        new_protocol = self.service.update_protocol(new_protocol)
        return {'id': new_protocol.protocol_id}


def date_validator(node, value):
    try:
        value = datetime.strptime(value, '%a %b %d %Y')
    except ValueError:
        raise colander.Invalid(node, 'Неверный формат даты')


def uuid_validator(node, value):
    pattern = '^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[4][0-9a-fA-F]{3}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
    res = re.match(pattern, value)
    if res is None:
        raise colander.Invalid(node, 'Недопустимая информация о файле')


class ProtocolControllerSchema(colander.MappingSchema):

    protocol_num = colander.SchemaNode(
        colander.String(),
        name='protocolNumber',
        validator=colander.Length(min=1, max=20, min_err='Слишком короткий номер протокола',
                                  max_err='Слишком длинный номер протокола'))

    protocol_date = colander.SchemaNode(
        colander.String(),
        name='protocolDate',
        validator=date_validator)

    meetings_type_id = colander.SchemaNode(
        colander.Int(),
        name='meeting',
        validator=colander.Range(min=0, min_err='Неверный вид заседания'))

    protocol_name = colander.SchemaNode(
        colander.String(),
        name='protocolName',
        validator=colander.Length(min=1, max=255, min_err='Слишком короткое имя протока',
                                  max_err='Слишком длинное имя протокола'))

    note = colander.SchemaNode(
        colander.String(),
        name='note',
        validator=colander.Length(min=1, max=2000, min_err='Слишком короткое примечание',
                                  max_err='Недопустимое примечание'))

    idfilestorage = colander.SchemaNode(
        colander.String(),
        name='idFileStorage',
        msg='Недопустимая информация о файле',
        validator=uuid_validator)


class ProtocolControllerFilterSchema(colander.MappingSchema):
    protocol_num = colander.SchemaNode(
        colander.String(),
        name='protocolNumber',
        validator=colander.Length(min=1, max=20, min_err='Слишком короткий номер протокола',
                                  max_err='Слишком длинный номер протокола'),
        missing=None)

    meetings_type_id = colander.SchemaNode(
        colander.Int(),
        name='meeting',
        validator=colander.Range(min=0, min_err='Неверный вид заседания'),
        missing=None)

    protocol_name = colander.SchemaNode(
        colander.String(),
        name='protocolName',
        validator=colander.Length(min=1, max=255, min_err='Слишком короткое имя протокола',
                                  max_err='Слишком длинное имя протокола'),
        missing=None)

    date_start = colander.SchemaNode(
        colander.String(),
        name='dateStart',
        validator=date_validator,
        missing=None)

    date_end = colander.SchemaNode(
        colander.String(),
        name='dateEnd',
        validator=date_validator,
        missing=None)
