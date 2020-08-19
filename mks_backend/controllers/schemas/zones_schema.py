import colander


class ZonesSchema(colander.MappingSchema):

    fullname = colander.SchemaNode(
        colander.String(),
        name='fullName',
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое наименование',
            max_err='Слишком длинное наименование'
        )
    )