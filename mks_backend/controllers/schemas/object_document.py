import colander


class ObjectDocumentSchema(colander.MappingSchema):

    construction_objects_id = colander.SchemaNode(
        colander.Integer(),
        name='constructionObjectId',
    )

    construction_documents_id = colander.SchemaNode(
        colander.Integer(),
        name='constructionDocumentId',
    )
