import colander

from mks_backend.utils.validator_utils import strip_space


class ParticipantStatusSchema(colander.MappingSchema):

    fullname = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='fullName',
        validator=colander.Length(
            min=1,
            max=1000,
            min_err='Слишком короткие статусы участников судебных споров!',
            max_err='Слишком длинные статусы участников судебных споров!'
        )
    )
