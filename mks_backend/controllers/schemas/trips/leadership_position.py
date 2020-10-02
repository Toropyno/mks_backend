import colander


class LeadershipPositionSchema(colander.MappingSchema):

    code = colander.SchemaNode(
        colander.String(),
        name='code',
        validator=colander.Length(
            max=25,
            max_err='Слишком длинный код для должности'
        )
    )

    fullname = colander.SchemaNode(
        colander.String(),
        name='fullName',
        validator=colander.Length(
            max=255,
            max_err='Слишком длинное наименование должности'
        )
    )
