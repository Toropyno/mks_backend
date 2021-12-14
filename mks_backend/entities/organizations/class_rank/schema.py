import colander

from mks_backend.utils.validator_utils import strip_space


class ClassRankSchema(colander.MappingSchema):

    id_ = colander.SchemaNode(
        colander.Integer(),
        name='id',
        validator=colander.Range(
            min=0,
            min_err='Такого классного чина не существует'
        ),
        missing=colander.drop
    )

    name = colander.SchemaNode(
        colander.String(),
        name='name',
        preparer=[strip_space],
        validator=colander.Length(
            max=255,
            max_err='Слишком длинное имя'
        )
    )
