import colander

from mks_backend.utils.validator_utils import strip_space


class InspectionFileSchema(colander.MappingSchema):
    inspection_id = colander.SchemaNode(
        colander.Int(),
        name='inspectionId',
        validator=colander.Range(
            min=0,
            min_err='Такой проверки не существует'
        )
    )

    note = colander.SchemaNode(
        colander.String(),
        name='note',
        preparer=[strip_space],
        validator=colander.Length(
            max=2000,
            max_err='Превышена максимальная длинна примечания'
        ),
        missing=None
    )

    idfilestorage = colander.SchemaNode(
        colander.List(),
        name='ids',
    )
