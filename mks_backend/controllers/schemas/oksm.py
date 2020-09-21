import colander


class OKSMSchema(colander.MappingSchema):
    code = colander.SchemaNode(
        colander.String(),
        name='code',
        validator=colander.Length(
            min=3,
            max=3,
            min_err='Слишком короткое название кода!',
            max_err='Слишком длинное название кода!'
        )
    )

    shortname = colander.SchemaNode(
        colander.String(),
        name='shortName',
        validator=colander.Length(
            min=1,
            max=80,
            min_err='Слишком короткое название страны даже для краткого названия!',
            max_err='Слишком длинное название страны для краткого названия!'
        )
    )

    fullname = colander.SchemaNode(
        colander.String(),
        name='fullName',
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое название страны!',
            max_err='Слишком длинное название страны!'
        ),
        missing=None
    )

    alpha2 = colander.SchemaNode(
        colander.String(),
        name='alpha2',
        validator=colander.Length(
            min=2,
            max=2,
            min_err='Слишком короткое название alpha2!',
            max_err='Слишком длинное название alpha2!'
        )
    )

    alpha3 = colander.SchemaNode(
        colander.String(),
        name='alpha3',
        validator=colander.Length(
            min=3,
            max=3,
            min_err='Слишком короткое название alpha2!',
            max_err='Слишком длинное название alpha2!'
        )
    )
