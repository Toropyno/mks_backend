import colander

from mks_backend.utils.validator_utils import strip_space


class WorkTripFilesShema(colander.MappingSchema):
    idfilestorage = colander.SchemaNode(
        colander.List(),
        name='id',
    )

    work_trips_id = colander.SchemaNode(
        colander.Integer(),
        name='workTripId',
    )

    note = colander.SchemaNode(
        colander.String(),
        preparer=[strip_space],
        name='note',
        validator=colander.Length(
            max=1000,
            max_err='Слишком длинное примечание'
        ),
        missing=None
    )
