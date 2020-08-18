import colander

class ConstructionStagesSchema(colander.MappingSchema):

    code = colander.SchemaNode(
        colander.String(),
        name='code',
        validator=colander.Length(min=1, max=20, min_err='Слишком короткое краткое наименование',
                                  max_err='Слишком длинное краткое наименование')
    )
    fullname = colander.SchemaNode(
        colander.String(),
        name='fullname',
        validator=colander.Length(min=1, max=255, min_err='Слишком короткое полное наименование',
                                  max_err='Слишком длинное полное наименование')
    )
