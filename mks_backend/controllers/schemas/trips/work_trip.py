import colander

from mks_backend.controllers.schemas.validator_utils import date_validator


class WorkTripSchema(colander.MappingSchema):

    trip_date = colander.SchemaNode(
        colander.String(),
        name='date',
        validator=date_validator
    )

    trip_name = colander.SchemaNode(
        colander.String(),
        name='name',
        validator=colander.Length(
            max=255,
            max_err='Слишком длинное наименование поездки'
        )
    )

    escort_officer = colander.SchemaNode(
        colander.String(),
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
        )
    )
