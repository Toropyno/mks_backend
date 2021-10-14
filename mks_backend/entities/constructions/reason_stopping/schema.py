import colander

from mks_backend.utils.validator_utils import strip_space


class ReasonStoppingSchema(colander.MappingSchema):
    fullname = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='fullName',
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое название организации',
            max_err='Слишком длинное название организации'
            )
        )
