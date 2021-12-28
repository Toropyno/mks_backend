import colander

from mks_backend.utils.validator_utils import strip_space, date_validator, organization_uuid, uuid_file_validator


class OfficialSchema(colander.MappingSchema):
    organizations_id = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='organizationId',
        validator=organization_uuid
    )

    position_name = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='positionName',
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткая должность',
            max_err='Слишком длинная должность'
        )
    )

    military_ranks_id = colander.SchemaNode(
        colander.Int(),
        name='militaryRank',
        validator=colander.Range(
            min=0,
            min_err='Неверный номер воинского звания'
        ),
        missing=None
    )

    surname = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='surname',
        validator=colander.Length(
            min=1,
            max=40,
            min_err='Слишком короткая фамилия',
            max_err='Слишком длинная фамилия'
        )
    )

    firstname = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='firstName',
        validator=colander.Length(
            min=1,
            max=40,
            min_err='Слишком короткое имя',
            max_err='Слишком длинное имя'
        )
    )

    middlename = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='middleName',
        validator=colander.Length(
            min=1,
            max=40,
            min_err='Слишком короткое отчество',
            max_err='Слишком длинное отчество'
        ),
        missing=None
    )

    begin_date = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='beginDate',
        msg='Недопустимая информация о дате назначения на должность',
        validator=date_validator
    )

    end_date = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='endDate',
        msg='Недопустимая информация о дате освобождения должности',
        validator=date_validator,
        missing=None
    )

    phone = colander.SchemaNode(
        colander.String(),
        name='phone',
        missing=None
    )

    secure_channel = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='secureChannel',
        validator=colander.Length(
            min=1,
            max=40,
            min_err='Слишком короткое АТС-Р',
            max_err='Слишком длинное АТС-Р'
        ),
        missing=None
    )

    email = colander.SchemaNode(
        colander.String(),
        name='email',
        missing=None
    )

    note = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='note',
        validator=colander.Length(
            min=1,
            max=1000,
            min_err='Слишком короткое описание',
            max_err='Слишком длинное описание'
        ),
        missing=None
    )

    class_ranks_id = colander.SchemaNode(
        colander.Int(),
        name='classRank',
        validator=colander.Range(
            min=0,
            min_err='Неверный номер классного чина'
        ),
        missing=None
    )

    idfilestorage = colander.SchemaNode(
        colander.String(),
        name='filestorage',
        validator=uuid_file_validator,
        missing=None
    )


class OfficialFilterSchema(colander.MappingSchema):
    reflect_vacated_position = colander.SchemaNode(
        colander.Boolean(false_choices=['false', '0', 'False', 'none']),
        name='reflectVacatedPosition',
        missing=True
    )

    official_name = colander.SchemaNode(
        colander.Str(),
        preparer=[strip_space],
        name='officialName',
        missing=colander.drop
    )

    organization_uuid = colander.SchemaNode(
        colander.Str(),
        name='organization_uuid',
        validator=organization_uuid
    )
