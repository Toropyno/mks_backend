import colander


class InspectedObjectSchema(colander.MappingSchema):

    constructions = colander.SchemaNode(
        colander.List(),
        name='constructions',
    )
