from decimal import ROUND_UP

import colander

from mks_backend.controllers.schemas.validator_utils import date_validator, strip_space

CONTRACT_SUM_MAX = 1E+18  # precision = 20, scale = 2;


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
        colander.Decimal(quant='.00', rounding=ROUND_UP),
        name='contractSum',
        validator=colander.Range(
            min=0,
            max=CONTRACT_SUM_MAX,
            min_err='Сумма не может быть меньше нуля',
            max_err='Указанная сумма контракта слишком велика'
        )
    )

    paid_sum = colander.SchemaNode(
        colander.Decimal(quant='.00', rounding=ROUND_UP),
        name='paidSum',
        validator=colander.Range(
            min=0,
            max=CONTRACT_SUM_MAX,
            min_err='Сумма не может быть меньше нуля',
            max_err='Указанная сумма оплаты слишком велика'
        )
    )

    accepted_sum = colander.SchemaNode(
        colander.Decimal(quant='.00', rounding=ROUND_UP),
        name='acceptedSum',
        validator=colander.Range(
            min=0,
            max=CONTRACT_SUM_MAX,
            min_err='Сумма не может быть меньше нуля',
            max_err='Указанная принятая сумма слишком велика '
        )
    )

    receivables = colander.SchemaNode(
        colander.Decimal(quant='.00', rounding=ROUND_UP),
        name='receivables',
        validator=colander.Range(
            min=0,
            max=CONTRACT_SUM_MAX,
            min_err='Сумма не может быть меньше нуля',
            max_err='Указанная дебиторская задолженность слишком велика'
        )
    )

    plan_sum = colander.SchemaNode(
        colander.Decimal(quant='.00', rounding=ROUND_UP),
        name='planSum',
        validator=colander.Range(
            min=0,
            max=CONTRACT_SUM_MAX,
            min_err='Сумма не может быть меньше нуля',
            max_err='Указанная в плане финансирования сумма слишком велика'
        )
    )

    construction_id = colander.SchemaNode(
        colander.Integer(),
        name='constructionId',
        validator=colander.Range(
            min=0,
            min_err='Указанного ИСП не существует'
        )
    )

    contractor_id = colander.SchemaNode(
        colander.Integer(),
        name='contractorId',
        validator=colander.Range(
            min=0,
            min_err='Указанного генерального подрядчика не существует'
        )
    )

    subcontractor_id = colander.SchemaNode(
        colander.Integer(),
        name='subcontractorId',
        validator=colander.Range(
            min=0,
            min_err='Указанного субподрядчика не существует'
        ),
        misssing=None
    )

    contract_statuses_id = colander.SchemaNode(
        colander.Integer(),
        name='contractStatusId',
        validator=colander.Range(
            min=0,
            min_err='Указанного статуса контрактов не существует'
        ),
    )
