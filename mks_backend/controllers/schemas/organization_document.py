import colander

from mks_backend.controllers.schemas.validator_utils import (
    strip_space,
    date_validator,
    uuid_validator,
    timestamp_validator,
)


class OrganizationDocumentSchema(colander.MappingSchema):

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

    upload_date = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='uploadDate',
        msg='Недопустимая информация о дате загрузки',
        validator=timestamp_validator,
        missing=None
    )

    doc_date = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='docDate',
        msg='Недопустимая информация о дате документа',
        validator=date_validator
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

    organizations_id = colander.SchemaNode(
        colander.Int(),
        name='organizationsId',
        validator=colander.Range(
            min=0,
            min_err='Неверный номер организации'
        )
    )

    doctypes_id = colander.SchemaNode(
        colander.Int(),
        name='docTypesId',
        validator=colander.Range(
            min=0,
            min_err='Неверный номер типа документов'
        )
    )

    idfilestorage = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='idFileStorage',
        msg='Недопустимая информация о файле',
        validator=uuid_validator,
        missing=None
    )
