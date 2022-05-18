import colander

from mks_backend.utils.validator_utils import strip_space


class ConstructionStageSchema(colander.MappingSchema):
    code = colander.SchemaNode(
        colander.String(),
        name='code',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=20,
            min_err='Слишком короткое краткое наименование',
            max_err='Слишком длинное краткое наименование'
        )
    )

    fullname = colander.SchemaNode(
        colander.String(),
        name='fullName',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое полное наименование',
            max_err='Слишком длинное полное наименование'
        )
    )

    hierarchy_level = colander.SchemaNode(
        colander.Integer(),
        name='hierarchyLevel',
        validator=colander.Range(
            min=1,
            min_err='Уровень иерархии не может быть меньше единицы'
        )
    )

    parent = colander.SchemaNode(
        colander.Integer(),
        name='parent',
        validator=colander.Range(
            min=0,
            min_err='Некорректный номер родителя'
        ),
        missing=colander.drop
    )
