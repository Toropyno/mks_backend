import colander


class ObjectCategorySchema(colander.MappingSchema):

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
    note = colander.SchemaNode(
        colander.String(),
        name='note',
        validator=colander.Length(
            min=1,
            max=1000,
            min_err='Слишком короткое наименование',
            max_err='Слишком длинное наименование'
        ),
        missing=None
    )