import colander

from mks_backend.controllers.schemas.validator_utils import uuid_validator, strip_space


class InspectionFileSchema(colander.MappingSchema):

    inspection_id = colander.SchemaNode(
        colander.Int(),
        name='inspection',
        validator=colander.Range(
            min=0,
            min_err='Такой проверки не существует'
        )
    )

    note = colander.SchemaNode(
        colander.String(),
        name='note',
        preparer=[strip_space],
        validator=colander.Length(
            max=2000,
            max_err='Недопустимое примечание'
        )
    )

    idfilestorage = colander.SchemaNode(
        colander.String(),
        name='idFileStorage',
        preparer=[strip_space],
        msg='Недопустимая информация о файле',
        validator=uuid_validator
    )
