import colander

from mks_backend.utils.validator_utils import date_validator, strip_space, uuid_file_validator


class ProtocolControllerSchema(colander.MappingSchema):
    protocol_num = colander.SchemaNode(
        colander.String(),
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
        colander.String(),
        name='protocolDate',
        preparer=[strip_space],
        validator=date_validator)

    meetings_type_id = colander.SchemaNode(
        colander.Int(),
        name='meeting',
        validator=colander.Range(
            min=0,
            min_err='Неверный вид заседания'
        )
    )

    protocol_name = colander.SchemaNode(
        colander.String(),
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
        colander.String(),
        name='note',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=2000,
            min_err='Слишком короткое примечание',
            max_err='Недопустимое примечание'
        ),
        missing=None
    )

    idfilestorage = colander.SchemaNode(
        colander.String(),
        name='idFileStorage',
        preparer=[strip_space],
        validator=uuid_file_validator,
        missing=None
    )

    signatory = colander.SchemaNode(
        colander.String(),
        name='signatory',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое значение поля кем утвержден',
            max_err='Слишком длинное значение поля кем утвержден'
        ),
        missing=None
    )


class ProtocolControllerFilterSchema(colander.MappingSchema):
    protocol_num = colander.SchemaNode(
        colander.String(),
        name='protocolNumber',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=20,
            min_err='Слишком короткий номер протокола',
            max_err='Слишком длинный номер протокола'
        ),
        missing=None
    )

    meetings_type_id = colander.SchemaNode(
        colander.Int(),
        name='meeting',
        validator=colander.Range(
            min=0,
            min_err='Неверный вид заседания'
        ),
        missing=None
    )

    protocol_name = colander.SchemaNode(
        colander.String(),
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
        colander.String(),
        name='dateStart',
        preparer=[strip_space],
        validator=date_validator,
        missing=None
    )

    date_end = colander.SchemaNode(
        colander.String(),
        name='dateEnd',
        preparer=[strip_space],
        validator=date_validator,
        missing=None
    )

    signatory = colander.SchemaNode(
        colander.String(),
        name='signatory',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое значение поля кем утвержден',
            max_err='Слишком длинное значение поля кем утвержден'
        ),
        missing=None
    )
