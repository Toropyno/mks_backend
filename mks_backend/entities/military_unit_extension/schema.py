import colander

from mks_backend.utils.validator_utils import strip_space


class MilitaryUnitExtensionSchema(colander.MappingSchema):

    fullname = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='reportName',
        validator=colander.Length(
            min=1,
            max=1000,
            min_err='Слишком короткое дополнительное описание в/ч!',
            max_err='Слишком длинное дополнительное описание в/ч'
        )
    )

    idMU = colander.SchemaNode(
        colander.Int(),
        name='idMU',
        validator=colander.Range(
            min=0,
            min_err='Слишком длинный идентификатор в/ч'
        )
    )
