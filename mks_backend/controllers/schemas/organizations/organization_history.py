import colander

from mks_backend.controllers.schemas.validator_utils import strip_space, date_validator, organization_uuid


class OrganizationHistorySchema(colander.MappingSchema):

    shortname = colander.SchemaNode(
        colander.String(),
        name='shortname',
        preparer=strip_space,
        validator=colander.Length(
            max=255,
            max_err='Краткое наименование слишком большое'
        )
    )

    fullname = colander.SchemaNode(
        colander.String(),
        name='fullname',
        preparer=strip_space,
        validator=colander.Length(
            max=1000,
            max_err='Полное наименование слишком большое'
        )
    )

    address_legal = colander.SchemaNode(
        colander.String(),
        name='addressLegal',
        validator=colander.Length(
            max=1000,
            max_err='Слишком большой юридический адрес'
        ),
        missing=None
    )

    address_actual = colander.SchemaNode(
        colander.String(),
        name='addressActual',
        validator=colander.Length(
            max=1000,
            max_err='Слишком большой фактический адрес'
        ),
        missing=None
    )

    functions = colander.SchemaNode(
        colander.String(),
        name='functions',
        validator=colander.Length(
            max=2000,
            max_err='Слишком большой список функций'
        ),
        missing=None
    )

    inn = colander.SchemaNode(
        colander.String(),
        name='inn',
        validator=colander.Length(
            max=20,
            max_err='Слишком большой ИНН'
        ),
        missing=None
    )

    kpp = colander.SchemaNode(
        colander.String(),
        name='kpp',
        validator=colander.Length(
            max=20,
            max_err='Слишком большой КПП'
        ),
        missing=None
    )

    ogrn = colander.SchemaNode(
        colander.String(),
        name='ogrn',
        validator=colander.Length(
            max=20,
            max_err='Слишком большой ОГРН'
        ),
        missing=None
    )

    begin_date = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='beginDate',
        validator=date_validator
    )

    end_date = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='endDate',
        validator=date_validator,
        missing=None
    )

    organizations_id = colander.SchemaNode(
        colander.String(),
        name='organizationId',
        validator=organization_uuid,
        missing=None
    )
