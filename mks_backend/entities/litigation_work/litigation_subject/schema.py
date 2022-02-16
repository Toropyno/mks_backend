import colander


class LitigationSubjectSchema(colander.MappingSchema):
    constructions = colander.SchemaNode(
        colander.List(),
        name='constructions',
    )
