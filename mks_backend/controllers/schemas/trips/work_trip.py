import colander

from mks_backend.controllers.schemas.validator_utils import date_validator, strip_space


class WorkTripSchema(colander.MappingSchema):
    trip_date = colander.SchemaNode(
        colander.String(),
        name='date',
        validator=date_validator
    )

    trip_name = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='name',
        validator=colander.Length(
            max=255,
            max_err='Слишком длинное наименование поездки'
        )
    )

    escort_officer = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='escortOfficer',
        validator=colander.Length(
            max=100,
            max_err='Слишком длинное имя сопровождающего офицера'
        )
    )

    leadership_position = colander.SchemaNode(
        colander.Integer(),
        name='leadershipPosition',
        validator=colander.Range(
            min=0,
            min_err='Такой должности не существует'
        )
    )

    protocol_id = colander.SchemaNode(
        colander.Integer(),
        name='protocol',
        validator=colander.Range(
            min=0,
            min_err='Такого протокола не существует'
        ),
        missing=None
    )


class WorkTripFilterSchema(colander.MappingSchema):
    trip_date_start = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='tripDateStart',
        validator=date_validator,
        missing=None
    )

    trip_date_end = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='tripDateEnd',
        validator=date_validator,
        missing=None
    )

    leadership_position = colander.SchemaNode(
        colander.Int(),
        name='leadershipPosition',
        missing=None
    )

    escort_officer = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='escortOfficer',
        validator=colander.Length(
            max=100,
            max_err='Слишком длинное имя сопровождающего офицера'
        ),
        missing=None
    )

    trip_name = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='tripName',
        validator=colander.Length(
            max=255,
            max_err='Слишком длинное имя поездки'
        ),
        missing=None
    )

    # --------- protocols --------- #

    have_protocol = colander.SchemaNode(
        colander.Bool(),
        name='haveProtocol',
        missing=None
    )

    protocol_number = colander.SchemaNode(
        colander.String(),
        name='protocolNumber',
        preparer=[strip_space],
        validator=colander.Length(
            max=20,
            max_err='Слишком длинный номер протокола'
        ),
        missing=None
    )

    protocol_date_start = colander.SchemaNode(
        colander.String(),
        name='protocolDateStart',
        preparer=[strip_space],
        validator=date_validator,
        missing=None
    )

    protocol_date_end = colander.SchemaNode(
        colander.String(),
        name='protocolDateEnd',
        preparer=[strip_space],
        validator=date_validator,
        missing=None
    )

    # --------- constructions --------- #

    project_code = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='projectCode',
        validator=colander.Length(
            max=40,
            max_err='Слишком длинный код проекта'
        ),
        missing=None
    )

    is_critical = colander.SchemaNode(
        colander.Bool(),
        name='isCritical',
        missing=None
    )

    fias_subject = colander.SchemaNode(
        colander.Int(),
        name='fiasSubject',
        missing=None
    )
