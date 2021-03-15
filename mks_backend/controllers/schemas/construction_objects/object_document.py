import colander


class ObjectDocumentSchema(colander.MappingSchema):

    documents = colander.SchemaNode(
        colander.List()
    )
