import colander

from mks_backend.controllers.schemas.validator_utils import strip_space


class ContractStatusSchema(colander.MappingSchema):

    fullname = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='fullName',
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое наименование статуса госконтрактов',
            max_err='Слишком длинное наименование статуса госконтрактов'
        )
    )
