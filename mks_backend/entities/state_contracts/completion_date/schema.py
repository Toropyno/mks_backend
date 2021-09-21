import colander

from mks_backend.utils.validator_utils import strip_space, date_validator


class CompletionDateSchema(colander.MappingSchema):
    contracts_id = colander.SchemaNode(
        colander.Int(),
        name='contractId',
        validator=colander.Range(
            min=0,
            min_err='Неверный номер контракта'
        )
    )

    contract_worktypes_id = colander.SchemaNode(
        colander.Int(),
        name='contractWorkTypeId',
        validator=colander.Range(
            min=0,
            min_err='Неверный номер видов мероприятий'
        )
    )

    end_date = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='endDate',
        msg='Недопустимая информация о сроке исполнения',
        validator=date_validator
    )
