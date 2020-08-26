import colander


class SubcategoriesListSchema(colander.MappingSchema):
    construction_categories_id = colander.SchemaNode(
        colander.Integer(),
        name='constructionCategoriesId',
    )

    construction_subcategories_id = colander.SchemaNode(
        colander.Integer(),
        name='constructionSubcategoriesId',
    )
