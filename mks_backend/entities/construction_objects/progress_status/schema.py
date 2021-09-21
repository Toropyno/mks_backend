import colander

from mks_backend.utils.validator_utils import strip_space


class ProgressStatusSchema(colander.MappingSchema):
    fullname = colander.SchemaNode(
        colander.String(),
        name='fullName',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое наименование статуса хода работ!',
            max_err='Слишком длинное наименование статуса хода работ!'
        )
    )
