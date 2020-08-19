import colander


class ConstructionSubcategoriesSchema(colander.MappingSchema):

    fullname = colander.SchemaNode(
        colander.String(),
        name='fullName',
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое "полное имя" подкатегории ИСП',
            max_err='Слишком длинное "полное имя" подкатегории ИСП')
    )
