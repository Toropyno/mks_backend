import colander


class CommissionSchema(colander.MappingSchema):
    code = colander.SchemaNode(
        colander.String(),
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
        name='fullName',
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое название комиссии',
            max_err='Слишком длинное название комиссии'
        )
    )
