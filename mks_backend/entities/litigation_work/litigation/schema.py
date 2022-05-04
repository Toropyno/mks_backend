import colander

from mks_backend.utils.date_and_time import get_date_time_from_string
from mks_backend.utils.validator_utils import date_validator, organization_uuid, strip_space


class LitigationSchema(colander.MappingSchema):

    litigation_id = colander.SchemaNode(
        colander.Int(),
        name='id',
        validator=colander.Range(
            min=0,
            min_err='Слишком длинный идентификатор cудебного спора'
        ),
        missing=None
    )

    appeal_date = colander.SchemaNode(
        colander.String(),
        name='appealDate',
        validator=date_validator
    )

    courts_id = colander.SchemaNode(
        colander.Int(),
        name='court',
        validator=colander.Range(
            min=0,
            min_err='Слишком длинный идентификатор суда'
        )
    )

    organizations_id = colander.SchemaNode(
        colander.String(),
        name='organization',
        validator=organization_uuid
    )

    participant_statuses_id = colander.SchemaNode(
        colander.Int(),
        name='participantStatus',
        validator=colander.Range(
            min=0,
            min_err='Слишком длинный идентификатор статуса участника судебных споров'
        )
    )

    construction_companies_id = colander.SchemaNode(
        colander.Int(),
        name='constructionCompany',
        validator=colander.Range(
            min=0,
            min_err='Такого участника не существует'
        ),
        missing=None
    )

    participant_other = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='participantOther',
        validator=colander.Length(
            min=1,
            max=1000,
            min_err='Слишком короткое описание участника (иного лица)',
            max_err='Слишком длинное описание участника (иного лица)'
        ),
        missing=None
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
        ),
        missing=None
    )

    court_decisions_id = colander.SchemaNode(
        colander.Int(),
        name='courtDecision',
        validator=colander.Range(
            min=0,
            min_err='Слишком длинный идентификатор решения суда'
        ),
        missing=None
    )

    decision_date = colander.SchemaNode(
        colander.String(),
        name='decisionDate',
        validator=date_validator,
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

    def validator(self, node, cstruct):
        if not cstruct.get('constructionCompany') and not cstruct.get('participantOther'):
            raise colander.Invalid(node, 'Должен быть указан хотя бы один участник: со стороны подрядчика или иное лицо')

        if cstruct.get('decisionDate') and cstruct.get('decisionDate'):
            decision_date = get_date_time_from_string(cstruct.get('decisionDate'))
            appeal_date = get_date_time_from_string(cstruct.get('appealDate'))
            if decision_date < appeal_date:
                raise colander.Invalid(
                    node, 'Дата вынесения решения должна быть больше или равна дате обращения в суд'
                )


class LitigationFilterSchema(colander.MappingSchema):

    appeal_date_start = colander.SchemaNode(
        colander.String(),
        name='appealDateStart',
        validator=date_validator,
        missing=colander.drop
    )

    appeal_date_end = colander.SchemaNode(
        colander.String(),
        name='appealDateEnd',
        validator=date_validator,
        missing=colander.drop
    )

    decision_date_start = colander.SchemaNode(
        colander.String(),
        name='decisionDateStart',
        validator=date_validator,
        missing=colander.drop
    )

    decision_date_end = colander.SchemaNode(
        colander.String(),
        name='decisionDateEnd',
        validator=date_validator,
        missing=colander.drop
    )

    court = colander.SchemaNode(
        colander.Int(),
        name='court',
        validator=colander.Range(
            min=1,
            min_err='Идентификатор суда должен быть больше 0'
        ),
        missing=colander.drop
    )

    organization = colander.SchemaNode(
        colander.String(),
        name='organization',
        validator=organization_uuid,
        missing=colander.drop
    )

    participant_status = colander.SchemaNode(
        colander.Int(),
        name='participantStatus',
        validator=colander.Range(
            min=0,
            min_err='Идентификатор статуса участника судебных споров должен быть больше 0'
        ),
        missing=colander.drop
    )

    participant_other = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='participantOther',
        validator=colander.Length(
            min=1,
            max=1000,
            min_err='Слишком короткое описание участника(иного лица)',
            max_err='Слишком длинное описание участника(иного лица)'
        ),
        missing=colander.drop
    )

    project_code = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='projectСode',
        validator=colander.Length(
            min=1,
            max=1000,
            min_err='Слишком короткое описание объекта строительства',
            max_err='Слишком длинное описание  объекта строительства'
        ),
        missing=colander.drop
    )

    information = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='information',
        validator=colander.Length(
            min=1,
            min_err='Слишком короткое описание информации по делу',
            max=1000,
            max_err='Слишком длинное описание информации по делу'
        ),
        missing=colander.drop
    )

    court_decision = colander.SchemaNode(
        colander.Int(),
        name='courtDecision',
        validator=colander.Range(
            min=0,
            min_err='Идентификатор решения суда должен быть больше 0'
        ),
        missing=colander.drop
    )

    have_file = colander.SchemaNode(
        colander.Boolean(false_choices=['false', '0', 'False', 'none']),
        name='haveFile',
        missing=colander.drop
    )

    have_isp = colander.SchemaNode(
        colander.Boolean(false_choices=['false', '0', 'False', 'none']),
        name='haveIsp',
        missing=colander.drop
    )

    is_critical = colander.SchemaNode(
        colander.Boolean(false_choices=['false', '0', 'False', 'none']),
        name='isCritical',
        missing=colander.drop
    )

    fias_subject = colander.SchemaNode(
        colander.String(),
        name='fiasSubject',
        missing=colander.drop
    )

    construction_companies_id = colander.SchemaNode(
        colander.Int(),
        name='constructionCompany',
        validator=colander.Range(
            min=0,
            min_err='Такого участника не существует'
        ),
        missing=colander.drop
    )
