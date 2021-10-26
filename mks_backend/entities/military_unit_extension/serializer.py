from .model import MilitaryUnitExtension
from mks_backend.errors import serialize_error_handler
from mks_backend.utils.date_and_time import get_date_string


class MilitaryUnitExtensionSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, military_unit_extension: MilitaryUnitExtension) -> dict:
        return {
            'idMU': military_unit_extension.idMU,
            'reportName': military_unit_extension.report_name,
            'startDate': get_date_string(military_unit_extension.start_date),
                 }

    def convert_list_to_json(self, court: list) -> list:
        return list(map(self.convert_object_to_json, court))

    def convert_schema_to_object(self, schema: dict):
        military_unit_extension = MilitaryUnitExtension()
        military_unit_extension.idMU = schema.get('idMU')
        military_unit_extension.report_name = schema.get('reportName')
        military_unit_extension.start_date = schema.get('date')
        return military_unit_extension