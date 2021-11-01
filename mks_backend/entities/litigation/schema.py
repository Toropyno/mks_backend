import colander
from mks_backend.utils.validator_utils import strip_space, organization_uuid, date_validator


class LitigationSchema(colander.MappingSchema):

    litigation_id = colander.SchemaNode(
        colander.Int(),
        name='litigation_id',
        validator=colander.Range(
            min=0,
            min_err='Слишком длинный идентификатор cудебного спора'
            ),
        missing=None
    )

    appeal_date = colander.SchemaNode(
        colander.String(),
        name='appeal_date',
        validator=date_validator
    )

    courts_id = colander.SchemaNode(
        colander.Int(),
        name='courts_id',
        validator=colander.Range(
            min=0,
            min_err='Слишком длинный идентификатор суда'
            )
        )

    organizations_id = colander.SchemaNode(
        colander.String(),
        name='organizations_id',
        validator=organization_uuid
    )

    participant_statuses_id = colander.SchemaNode(
        colander.Int(),
        name='participant_statuses_id',
        validator=colander.Range(
            min=0,
            min_err='Слишком длинный идентификатор статуса участника судебных споров'
            )
        )

    construction_companies_id = colander.SchemaNode(
        colander.Int(),
        name='construction_companies_id',
        validator=colander.Range(
            min=0,
            min_err='Слишком длинный идентификатор строительной организации'
            )
        )

    participant_other = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='participant_other',
        validator=colander.Length(
            min=1,
            max=1000,
            min_err='Слишком короткое описание участника(иного лица)',
            max_err='Слишком длинное описание участника(иного лица)'
        )
    )

    information = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='information',
        validator=colander.Length(
            min=1,
            max=1000,
            min_err='Слишком короткое описание информации по делу',
            max_err='Слишком длинное описание информации по делу'
        )
    )

    court_decisions_id = colander.SchemaNode(
        colander.Int(),
        name='court_decisions_id',
        validator=colander.Range(
            min=0,
            min_err='Слишком длинный идентификатор решения суда'
            )
        )

    decision_date = colander.SchemaNode(
        colander.String(),
        name='decision_date',
        validator=date_validator
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
        )
    )
