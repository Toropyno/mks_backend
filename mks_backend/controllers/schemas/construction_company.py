import colander

from mks_backend.controllers.schemas.validator_utils import strip_space


class ConstructionCompanySchema(colander.MappingSchema):
    shortname = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='shortName',
        validator=colander.Length(
            min=1,
            max=100,
            min_err='Слишком короткое название организации даже для краткого названия!',
            max_err='Слишком длинное название организации для краткого названия!'
        )
    )

    fullname = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='fullName',
        validator=colander.Length(
            min=1,
            max=1000,
            min_err='Слишком короткое название организации!',
            max_err='Слишком длинное название организации'
        )
    )
