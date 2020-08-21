import colander

strip_space = lambda v: v.strip(' \t\n\r') if v is not None else v


class ConstructionCategoriesSchema(colander.MappingSchema):
    fullname = colander.SchemaNode(
        colander.String(allow_empty=True),
        preparer=[strip_space],
        name='fullName',
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое наименование объекта',
            max_err='Слишком длинное наименование объекта')
    )
