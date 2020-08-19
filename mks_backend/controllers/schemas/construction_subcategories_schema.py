import colander

strip_space = lambda v: v.strip(' \t\n\r') if v is not None else v


class ConstructionSubcategoriesSchema(colander.MappingSchema):
    fullname = colander.SchemaNode(
        colander.String(allow_empty=True),
        preparer=[strip_space],
        name='fullName',
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое "полное имя" подкатегории ИСП',
            max_err='Слишком длинное "полное имя" подкатегории ИСП')
    )
