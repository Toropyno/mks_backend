import colander


class VisitedObjectSchema(colander.MappingSchema):
    constructions = colander.SchemaNode(
        colander.List(),
        name='constructions',
    )
