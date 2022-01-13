import colander

from mks_backend.entities.organizations.organization_history import OrganizationHistorySchema
from mks_backend.utils.validator_utils import organization_parent_uuid, organization_uuid, strip_space


class OrganizationSchema(colander.MappingSchema):
    organization_uuid = colander.SchemaNode(
        colander.String(),
        name='organizationId',
        validator=organization_uuid,
        missing=colander.drop
    )

    parent = colander.SchemaNode(
        colander.String(),
        name='parentId',
        validator=organization_parent_uuid,
        missing=None
    )

    par_number = colander.SchemaNode(
        colander.Integer(),
        name='parentNumber',
        validator=colander.Range(
            min=1,
            min_err='Номер в пределах родителя не может быть меньше 1'
        ),
        missing=None
    )

    org_sign = colander.SchemaNode(
        colander.Boolean(false_choices=['false', '0', 'False', 'none']),
        name='isLegal'
    )

    history = OrganizationHistorySchema(missing=colander.drop)


class OrganizationFilterSchema(colander.MappingSchema):
    organization_name = colander.SchemaNode(
        colander.Str(),
        preparer=[strip_space],
        name='organizationName',
        missing=colander.drop
    )

    official_name = colander.SchemaNode(
        colander.Str(),
        preparer=[strip_space],
        name='officialName',
        missing=colander.drop
    )

    reflect_vacated_position = colander.SchemaNode(
        colander.Boolean(false_choices=['false', '0', 'False', 'none']),
        name='reflectVacatedPosition',
        missing=True
    )
