import colander

from mks_backend.controllers.schemas.validator_utils import date_validator, uuid_validator, strip_space


class ProtocolControllerSchema(colander.MappingSchema):

    protocol_num = colander.SchemaNode(
        colander.String(allow_empty=True),
        name='protocolNumber',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=20,
            min_err='Слишком короткий номер протокола',
            max_err='Слишком длинный номер протокола'
        )
    )

    protocol_date = colander.SchemaNode(
        colander.String(allow_empty=True),
        name='protocolDate',
        preparer=[strip_space],
        validator=date_validator)

    meetings_type_id = colander.SchemaNode(
        colander.Int(),
        name='meeting',
        validator=colander.Range(min=0, min_err='Неверный вид заседания'))

    protocol_name = colander.SchemaNode(
        colander.String(allow_empty=True),
        name='protocolName',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое имя протока',
            max_err='Слишком длинное имя протокола'
        )
    )

    note = colander.SchemaNode(
        colander.String(allow_empty=True),
        name='note',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=2000,
            min_err='Слишком короткое примечание',
            max_err='Недопустимое примечание'
        )
    )

    idfilestorage = colander.SchemaNode(
        colander.String(allow_empty=True),
        name='idFileStorage',
        preparer=[strip_space],
        msg='Недопустимая информация о файле',
        validator=uuid_validator)


class ProtocolControllerFilterSchema(colander.MappingSchema):
    protocol_num = colander.SchemaNode(
        colander.String(allow_empty=True),
        name='protocolNumber',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=20,
            min_err='Слишком короткий номер протокола',
            max_err='Слишком длинный номер протокола'),
        missing=None
    )

    meetings_type_id = colander.SchemaNode(
        colander.Int(),
        name='meeting',
        validator=colander.Range(min=0, min_err='Неверный вид заседания'),
        missing=None
    )

    protocol_name = colander.SchemaNode(
        colander.String(allow_empty=True),
        name='protocolName',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое имя протокола',
            max_err='Слишком длинное имя протокола'
        ),
        missing=None
    )

    date_start = colander.SchemaNode(
        colander.String(allow_empty=True),
        name='dateStart',
        preparer=[strip_space],
        validator=date_validator,
        missing=None)

    date_end = colander.SchemaNode(
        colander.String(allow_empty=True),
        name='dateEnd',
        preparer=[strip_space],
        validator=date_validator,
        missing=None)
