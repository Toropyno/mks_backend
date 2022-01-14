import colander

from mks_backend.utils.validator_utils import (date_validator, inn_validator, kpp_validator, ogrn_validator,
                                               organization_uuid, strip_space)


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
        validator=inn_validator,
        missing=None
    )

    kpp = colander.SchemaNode(
        colander.String(),
        name='kpp',
        validator=kpp_validator,
        missing=None
    )

    ogrn = colander.SchemaNode(
        colander.String(),
        name='ogrn',
        validator=ogrn_validator,
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
