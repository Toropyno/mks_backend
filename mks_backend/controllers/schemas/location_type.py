import colander


class LocationTypeSchema(colander.MappingSchema):
    fullname = colander.SchemaNode(
        colander.String(),
        name='fullName',
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое название типа местоположения',
            max_err='Слишком длинное название местоположения'
        )
    )
