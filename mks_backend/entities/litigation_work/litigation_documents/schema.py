import colander

from mks_backend.utils.validator_utils import date_validator, strip_space, timestamp_validator, uuid_file_validator


class LitigationDocumentSchema(colander.MappingSchema):
    litigation_id = colander.SchemaNode(
        colander.Int(),
        name='litigationId',
        validator=colander.Range(
            min=0,
            min_err='Неверный номер проекта'
        )
    )

    doctypes_id = colander.SchemaNode(
        colander.Int(),
        name='docType',
        validator=colander.Range(
            min=0,
            min_err='Неверный номер типа документов'
        )
    )

    doc_number = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='docNumber',
        validator=colander.Length(
            min=1,
            max=40,
            min_err='Слишком короткий номер документа',
            max_err='Слишком длинный номер документа'
        )
    )

    doc_date = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='docDate',
        msg='Недопустимая информация о дате документа',
        validator=date_validator
    )

    doc_name = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='docName',
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое имя документа',
            max_err='Слишком длинное имя документа'
        ),
        missing=None
    )

    note = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='note',
        validator=colander.Length(
            min=1,
            max=1000,
            min_err='Слишком короткое примечание',
            max_err='Слишком длинное примечание'
        ),
        missing=None
    )

    idfilestorage = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='idFileStorage',
        validator=uuid_file_validator,
        missing=None
    )

    upload_date = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='uploadDate',
        msg='Недопустимая информация о дате загрузки',
        validator=timestamp_validator,
        missing=None
    )

    valid_until = colander.SchemaNode(
        colander.String(),
        name='validUntil',
        validator=date_validator,
        missing=None
    )
