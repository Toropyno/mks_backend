import colander

from mks_backend.controllers.schemas.validator_utils import strip_space


class FIASSchema(colander.MappingSchema):
    subject = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='subject',
        validator=colander.Length(
            min=1,
            max=100,
            min_err='Слишком короткое название области или республики',
            max_err='Слишком длинное название области или республики'
        ),
        missing=None
    )

    district = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='district',
        validator=colander.Length(
            min=1,
            max=100,
            min_err='Слишком короткое название района',
            max_err='Слишком длинное название района'
        ),
        missing=None
    )

    city = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='city',
        validator=colander.Length(
            min=1,
            max=100,
            min_err='Слишком короткое название города',
            max_err='Слишком длинное название города'
        ),
        missing=None
    )

    locality = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='locality',
        validator=colander.Length(
            min=1,
            max=100,
            min_err='Слишком короткое название поселения',
            max_err='Слишком длинное название поселения'
        ),
        missing=None
    )

    remaining_address = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='remainingAddress',
        validator=colander.Length(
            min=1,
            max=100,
            min_err='Слишком короткое название улицы',
            max_err='Слишком длинное название улицы'
        ),
        missing=None
    )

    aoid = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='aoid',
        validator=colander.Length(
            min=1,
            max=100,
            min_err='Слишком короткий aoid',
            max_err='Слишком длинный aoid'
        ),
        missing=None
    )


class FIASAPISchema(colander.MappingSchema):
    full_fias = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='fullFias',
        validator=colander.Length(
            min=1,
            max=300,
            min_err='Слишком короткий адрес',
            max_err='Слишком длинный адрес'
        ),
        missing=None
    )
