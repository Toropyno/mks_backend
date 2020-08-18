import colander


class ObjectCategoriesListSchema(colander.MappingSchema):

     zones_id = colander.SchemaNode(
          colander.Int(),
          name='zoneId',
          validator=colander.Range(
               min=0,
               min_err='Недопустимая зона военных городков'
          )
     )
     object_categories_id = colander.SchemaNode(
          colander.Int(),
          name='objectCategoriesId',
          validator=colander.Range(
               min=0,
               min_err='Недопустимая категория объекта строительства'
          )
     )