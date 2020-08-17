import colander
from pyramid.view import view_config
from pyramid.response import Response

from mks_backend.services.construction_service import ConstructionService
from mks_backend.serializers.construction_serializer import ConstructionSerializer

# for colander validation
from datetime import datetime
from mks_backend.repositories.construction_categories_repository import ConstructionCategoryRepository
from mks_backend.repositories.construction_subcategories_repository import ConstructionSubcategoryRepository
from mks_backend.repositories.commission_repository import CommissionRepository
from mks_backend.repositories.military_unit_repository import MilitaryUnitRepository
# ------------------------


class ConstructionController:

    def __init__(self, request):
        self.request = request
        self.service = ConstructionService()
        self.serializer = ConstructionSerializer()

    @view_config(route_name='constructions', request_method='GET', renderer='json')
    def get_all_constructions(self):
        if self.request.params:
            constructions = self.service.get_all_constructions()  # TODO: refactor when filtration will be good
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
            constructions = self.service.get_all_constructions()

        json = self.serializer.convert_list_to_json(constructions)
        return json

    @view_config(route_name='add_construction', request_method='POST', renderer='json')
    def add_construction(self):
        construction_schema = ConstructionSchema()
        try:
            construction_deserialized = construction_schema.deserialize(self.request.json_body)
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())

        try:
            construction = self.service.convert_schema_to_object(construction_deserialized)
            self.service.add_construction(construction)
        except ValueError as error:
            return Response(status=403, json_body={'error': error.args[0]})

        return {'id': construction.construction_id}

    @view_config(route_name='construction_delete_change_and_view', request_method='DELETE', renderer='json')
    def delete_construction(self):
        id = self.request.matchdict['id']
        self.service.delete_construction_by_id(id)
        return {'id': id}

    @view_config(route_name='construction_delete_change_and_view', request_method='PUT', renderer='json')
    def edit_construction(self):
        construction_schema = ConstructionSchema()
        try:
            construction_deserialized = construction_schema.deserialize(self.request.json_body)
            construction_deserialized['id'] = self.request.matchdict['id']
        except colander.Invalid as error:
            return Response(status=403, json_body=error.asdict())

        try:
            new_construction = self.service.convert_schema_to_object(construction_deserialized)
            self.service.update_construction(new_construction)
        except ValueError as error:
            return Response(status=403, json_body={'error': error.args[0]})

        return {'id': new_construction.construction_id}

    @view_config(route_name='construction_delete_change_and_view', request_method='GET', renderer='json')
    def get_construction(self):
        id = self.request.matchdict['id']
        construction = self.service.get_construction_by_id(id)
        json = self.serializer.convert_object_to_json(construction)
        return json


def date_validator(node, value):
    try:
        value = datetime.strptime(value, '%a %b %d %Y')
    except ValueError:
        raise colander.Invalid(node, 'Неверный формат даты')


def construction_category_validator(node, value):
    if not ConstructionCategoryRepository.get_construction_category_by_id(value):
        raise colander.Invalid(node, 'Такой категории для проекта не существует')


def construction_subcategory_validator(node, value):
    if not ConstructionSubcategoryRepository.get_construction_subcategory_by_id(value):
        raise colander.Invalid(node, 'Такой подкатегории для проекта не существует')


def construction_commission_validator(node, value):
    if not CommissionRepository.get_commission_by_id(value):
        raise colander.Invalid(node, 'Такой комиссии пока не придумали')


def construction_military_unit_validator(node, value):
    if not MilitaryUnitRepository.get_military_unit_by_id(value):
        raise colander.Invalid(node, 'Такого военного формирования не существует')


class ConstructionSchema(colander.MappingSchema):

    project_code = colander.SchemaNode(
        colander.String(),
        name='code',
        validator=colander.Length(min=1, max=40, min_err='Слишком короткий код проекта',
                                  max_err='Слишком длинный код проекта')
    )

    project_name = colander.SchemaNode(
        colander.String(),
        name='name',
        validator=colander.Length(min=1, max=255, min_err='Слишком короткое имя проекта',
                                  max_err='Слишком длинное имя проекта')
    )

    construction_categories_id = colander.SchemaNode(
        colander.Int(),
        name='category',
        validator=construction_category_validator,
        missing=None
    )

    subcategories_list_id = colander.SchemaNode(
        colander.Int(),
        name='subcategory',
        validator=construction_subcategory_validator,
        missing=None
    )

    is_critical = colander.SchemaNode(
        colander.Bool(),
        name='isCritical',
        validator=colander.OneOf([True, False])
    )

    commission_id = colander.SchemaNode(
        colander.Int(),
        name='commission',
        validator=construction_commission_validator
    )

    idMU = colander.SchemaNode(
        colander.Int(),
        name='militaryUnit',
        validator=construction_military_unit_validator,
        missing=None
    )

    contract_date = colander.SchemaNode(
        colander.String(),
        name='contractDate',
        validator=date_validator
    )

    object_amount = colander.SchemaNode(
        colander.Int(),
        name='objectsAmount',
        validator=colander.Range(min=1)
    )

    planned_date = colander.SchemaNode(
        colander.String(),
        name='plannedDate',
        validator=date_validator
    )
