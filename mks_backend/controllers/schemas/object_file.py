import colander

from mks_backend.controllers.schemas.validator_utils import strip_space, uuid_validator, timestamp_validator


class ObjectFileSchema(colander.MappingSchema):

    construction_objects_id = colander.SchemaNode(
        colander.Int(),
        name='constructionObjects',
        validator=colander.Range(
            min=0,
            min_err='Недопустимое значение объекта'
        )
    )

    idfilestorage = colander.SchemaNode(
        colander.String(),
        name='idFileStorage',
        preparer=[strip_space],
        msg='Недопустимая информация о файле',
        validator=uuid_validator
    )

    upload_date = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='uploadDate',
        msg='Недопустимая информация о дате загрузки',
        validator=timestamp_validator,
        missing=None
    )

    note = colander.SchemaNode(
        colander.String(),
        name='note',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=1000,
            min_err='Слишком короткое наименование',
            max_err='Слишком длинное наименование'
        ),
        missing=None
    )
