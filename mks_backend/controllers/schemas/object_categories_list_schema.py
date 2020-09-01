import colander


class ObjectCategoriesListSchema(colander.MappingSchema):

     zones_id = colander.SchemaNode(
          colander.Int(),
          name='zone',
          validator=colander.Range(
               min=0,
               min_err='Недопустимая зона военных городков'
          )
     )

     object_categories_id = colander.SchemaNode(
          colander.Int(),
          name='category',
          validator=colander.Range(
               min=0,
               min_err='Недопустимая категория объекта строительства'
          )
     )
