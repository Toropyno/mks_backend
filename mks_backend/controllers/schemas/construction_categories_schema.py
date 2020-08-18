import colander


class ConstructionCategoriesSchema(colander.MappingSchema):

    fullname = colander.SchemaNode(
        colander.String(),
        name='fullName',
        validator=colander.Length(
            min=1, max=255, min_err='Слишком короткое "полное имя" объекта',
            max_err='Слишком длинное "полное имя" объекта')
    )
