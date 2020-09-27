import colander

from mks_backend.controllers.schemas.validator_utils import strip_space, uuid_validator, date_validator


class ObjectFileSchema(colander.MappingSchema):

    idfilestorage = colander.SchemaNode(
        colander.String(),
        name='idFileStorage',
        preparer=[strip_space],
        msg='Недопустимая информация о файле в файлах зданий и сооружений',
        validator=uuid_validator)

    construction_objects_id = colander.SchemaNode(
        colander.Int(),
        name='constructionObjects',
        validator=colander.Range(
            min=0,
            min_err='Недопустимое значение объектов строительства в файлах зданий и сооружений'
        )
    )

    note = colander.SchemaNode(
        colander.String(),
        name='note',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=1000,
            min_err='Слишком короткое примечание файлов зданий и сооружений',
            max_err='Слишком длинное примечание файлов зданий и сооружений'
        ),
        missing=None
    )

    upload_date = colander.SchemaNode(
        colander.String(),
        name='uploadDate',
        validator=date_validator,
        msg='Недопустимая информация о дате загрузки в файлах зданий и сооружений',
    )
