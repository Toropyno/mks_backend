import colander

# some shit
from mks_backend.repositories.construction_categories_repository import ConstructionCategoryRepository
from mks_backend.repositories.construction_subcategories_repository import ConstructionSubcategoryRepository
from mks_backend.repositories.commission_repository import CommissionRepository
from mks_backend.repositories.military_unit_repository import MilitaryUnitRepository
# end of shit

from mks_backend.controllers.schemas.validator_utils import date_validator


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
        validator=colander.Length(
            min=1, max=255, min_err='Слишком короткое имя проекта',
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
