import colander

from mks_backend.utils.validator_utils import date_validator, strip_space


class ConstructionDynamicSchema(colander.MappingSchema):

    construction_id = colander.SchemaNode(
        colander.Integer(),
        name='constructionId',
        validator=colander.Range(
            min=0,
            min_err='Такого проекта ИСП не существует'
        )
    )

    reporting_date = colander.SchemaNode(
        colander.String(),
        name='reportingDate',
        validator=date_validator
    )

    people_plan = colander.SchemaNode(
        colander.Integer(),
        name='peoplePlan',
        validator=colander.Range(
            min=0,
            min_err='Кол-во людей не может быть меньше нуля'
        )
    )

    people = colander.SchemaNode(
        colander.Integer(),
        name='people',
        validator=colander.Range(
            min=0,
            min_err='Кол-во людей не может быть меньше нуля'
        )
    )

    equipment_plan = colander.SchemaNode(
        colander.Integer(),
        name='equipmentPlan',
        validator=colander.Range(
            min=0,
            min_err='Кол-во снаряжения не может быть меньше нуля'
        )
    )

    equipment = colander.SchemaNode(
        colander.Integer(),
        name='equipment',
        validator=colander.Range(
            min=0,
            min_err='Кол-во снаряжения не может быть меньше нуля'
        )
    )

    description = colander.SchemaNode(
        colander.String(),
        name='description',
        preparer=[strip_space],
        validator=colander.Length(
            max=255,
            max_err='Слишком длинное описание хода СМР'
        ),
        missing=colander.drop
    )

    reason = colander.SchemaNode(
        colander.String(),
        name='reason',
        preparer=[strip_space],
        validator=colander.Length(
            max=100,
            max_err='Слишком длинная причина остановки СМР'
        ),
        missing=None
    )

    problems = colander.SchemaNode(
        colander.String(),
        name='problems',
        preparer=[strip_space],
        validator=colander.Length(
            max=1000,
            max_err='Слишком длинное содержание проблемных вопросов'
        ),
        missing=None
    )

    from_sakura = colander.SchemaNode(
        colander.Boolean(),
        name='fromSakura'
    )
