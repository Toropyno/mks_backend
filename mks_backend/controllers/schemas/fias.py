import colander


class FIASSchema(colander.MappingSchema):

    subject = colander.SchemaNode(
        colander.List(),
        missing=None
    )

    district = colander.SchemaNode(
        colander.List(),
        missing=None
    )
