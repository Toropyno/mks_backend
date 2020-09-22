import colander


class ConstructionTypeSchema(colander.MappingSchema):
    fullname = colander.SchemaNode(
        colander.String(),
        name='fullName',
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое название типа проекта',
            max_err='Слишком длинное название проекта'
        )
    )
