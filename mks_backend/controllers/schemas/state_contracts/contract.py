import colander

from mks_backend.controllers.schemas.validator_utils import date_validator, strip_space


class ContractSchema(colander.MappingSchema):

    contract_num = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='contractNum',
        validator=colander.Length(
            max=50,
            max_err='Слишком длинный номер контракта'
        ),
        missing=None
    )

    contract_date = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='contractDate',
        validator=date_validator
    )

    identifier = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='identifier',
        validator=colander.Length(
            max=25,
            max_err='Слишком длинный идентификатор'
        ),
        missing=None
    )

    subject = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='subject',
        validator=colander.Length(
            max=1000,
            max_err='Слишком длинный предмет контракта'
        ),
        missing=None
    )

    contract_sum = colander.SchemaNode(
        colander.Decimal(),
        name='contractSum',
        validator=colander.Range(
            min=0,
            min_err='Сумма не может быть меньше нуля'
        )
    )

    paid_sum = colander.SchemaNode(
        colander.Decimal(),
        name='paidSum',
        validator=colander.Range(
            min=0,
            min_err='Сумма не может быть меньше нуля'
        )
    )

    accepted_sum = colander.SchemaNode(
        colander.Decimal(),
        name='acceptedSum',
        validator=colander.Range(
            min=0,
            min_err='Сумма не может быть меньше нуля'
        )
    )

    receivables = colander.SchemaNode(
        colander.Decimal(),
        name='receivables',
        validator=colander.Range(
            min=0,
            min_err='Сумма не может быть меньше нуля'
        )
    )

    plan_sum = colander.SchemaNode(
        colander.Decimal(),
        name='planSum',
        validator=colander.Range(
            min=0,
            min_err='Сумма не может быть меньше нуля'
        )
    )

    construction_id = colander.SchemaNode(
        colander.Integer(),
        name='constructionId',
        validator=colander.Range(
            min=0,
            min_err='Такой организации не существует'
        )
    )

    contractor_id = colander.SchemaNode(
        colander.Integer(),
        name='contractorId',
        validator=colander.Range(
            min=0,
            min_err='Такой строительной организации не существует'
        )
    )

    subcontractor_id = colander.SchemaNode(
        colander.Integer(),
        name='subcontractorId',
        validator=colander.Range(
            min=0,
            min_err='Такой строительной не существует'
        ),
        misssing=None
    )

    contract_statuses_id = colander.SchemaNode(
        colander.Integer(),
        name='contractStatusId',
        validator=colander.Range(
            min=0,
            min_err='Такого статуса контрактов не существует'
        ),
    )
