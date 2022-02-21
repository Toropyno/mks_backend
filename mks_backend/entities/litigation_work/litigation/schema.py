import colander

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
            min_err='Слишком длинный идентификатор строительной организации'
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
            raise colander.Invalid(node, 'Участник со стороны подрядчика или Участник (иное лицо) не заполнено')

        if cstruct.get('decisionDate'):
            if cstruct.get('decisionDate') < cstruct.get('appealDate'):
                raise colander.Invalid(
                    node, 'Дата окончания судебного разбирательства должна быть больше или равна дате начала'
                )
