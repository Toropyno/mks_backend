import colander

from mks_backend.controllers.schemas.organizations.organization_history import OrganizationHistorySchema
from mks_backend.controllers.schemas.validator_utils import organization_parent_uuid, organization_uuid


class OrganizationSchema(colander.MappingSchema):

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

    history = OrganizationHistorySchema()


class OrganizationPatchSchema(colander.MappingSchema):

    organization_uuid = colander.SchemaNode(
        colander.String(),
        name='organizationId',
        validator=organization_uuid
    )

    new_parent_uuid = colander.SchemaNode(
        colander.String(),
        name='parentId',
        validator=organization_parent_uuid
    )


class OrganizationFilterSchema(colander.MappingSchema):

    reflect_disbanded = colander.SchemaNode(
        colander.Boolean(false_choices=['false', '0', 'False', 'none']),
        name='reflectDisbanded',
        missing=colander.drop
    )

