import colander

from mks_backend.controllers.schemas.validator_utils import strip_space


class ProgressStatusSchema(colander.MappingSchema):

    fullname = colander.SchemaNode(
        colander.String(),
        name='fullName',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое название статуса хода работ!',
            max_err='Слишком длинное название статуса хода работ!'
        )
    )
