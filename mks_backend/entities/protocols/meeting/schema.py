import colander

from mks_backend.utils.validator_utils import strip_space


class MeetingSchema(colander.MappingSchema):
    fullname = colander.SchemaNode(
        colander.String(),
        name='fullName',
        preparer=[strip_space],
        validator=colander.Length(
            min=1,
            max=255,
            min_err='Слишком короткое наименование типа митинга',
            max_err='Слишком длинное наименование типа митинга'
        )
    )
