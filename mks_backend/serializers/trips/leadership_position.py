from mks_backend.models.trips.leadership_position import LeadershipPosition

from mks_backend.errors.serialize_error import serialize_error_handler


class LeadershipPositionSerializer:

    @classmethod
    @serialize_error_handler
    def to_json(cls, leadership_position: LeadershipPosition) -> dict:
        return {
            'id': leadership_position.leadership_positions_id,
            'code': leadership_position.code,
            'fullName': leadership_position.fullname
        }

    def convert_list_to_json(self, leadership_positions: list) -> list:
        return list(map(self.to_json, leadership_positions))

    def convert_schema_to_object(self, schema: dict) -> LeadershipPosition:
        leadership_position = LeadershipPosition()

        leadership_position.leadership_positions_id = schema.get('id')
        leadership_position.code = schema.get('code')
        leadership_position.fullname = schema.get('fullName')

        return leadership_position
