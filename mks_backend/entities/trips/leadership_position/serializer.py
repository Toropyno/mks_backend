from .model import LeadershipPosition

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler


class LeadershipPositionSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, leadership_position: LeadershipPosition) -> dict:
        return {
            'id': leadership_position.leadership_positions_id,
            'code': leadership_position.code,
            'fullName': leadership_position.fullname
        }

    def to_mapped_object(self, schema: dict) -> LeadershipPosition:
        leadership_position = LeadershipPosition()

        leadership_position.leadership_positions_id = schema.get('id')
        leadership_position.code = schema.get('code')
        leadership_position.fullname = schema.get('fullName')

        return leadership_position
