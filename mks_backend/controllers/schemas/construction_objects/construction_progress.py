import colander

from mks_backend.controllers.schemas.validator_utils import date_validator, strip_space


class ConstructionProgressSchema(colander.MappingSchema):
    construction_objects_id = colander.SchemaNode(
        colander.Int(),
        name='constructionObjects',
        validator=colander.Range(
            min=0,
            min_err='Недопустимое значение объектов строительства'
        )
    )

    reporting_date = colander.SchemaNode(
        colander.String(),
        name='reportingDate',
        preparer=[strip_space],
        validator=date_validator
    )

    readiness = colander.SchemaNode(
        colander.Decimal(),
        name='readiness',
        validator=colander.Range(
            min=1,
            max=100,
            min_err='Недопустимый процент готовности объекта'
        ),
    )

    people = colander.SchemaNode(
        colander.Int(),
        name='people',
        validator=colander.Range(
            min=0,
            min_err='Недопустимое значение количества рабочих'
        )
    )

    equipment = colander.SchemaNode(
        colander.Int(),
        name='equipment',
        validator=colander.Range(
            min=0,
            min_err='Недопустимое значение количества техники'
        )
    )

    people_plan = colander.SchemaNode(
        colander.Int(),
        name='peoplePlan',
        validator=colander.Range(
            min=0,
            min_err='Недопустимое значение количества рабочих'
        )
    )

    equipment_plan = colander.SchemaNode(
        colander.Int(),
        name='equipmentPlan',
        validator=colander.Range(
            min=0,
            min_err='Недопустимое значение количества техники'
        )
    )

    progress_statuses_id = colander.SchemaNode(
        colander.Int(),
        name='progressStatus',
        validator=colander.Range(
            min=0,
            min_err='Недопустимое значение статуса хода работ'
        )
    )

    update_datetime = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='updateDatetime',
        validator=date_validator,
        missing=None
    )
