import colander

from mks_backend.controllers.schemas.validator_utils import strip_space


class CommissionSchema(colander.MappingSchema):
    code = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='code',
        validator=colander.Length(
            min=1,
            max=20,
            min_err='Слишком короткий код комиссиии',
            max_err='Слишком длинный код комиссии'
        )
    )

    fullname = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='fullName',
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое название комиссии',
            max_err='Слишком длинное название комиссии'
        )
    )
