from .model import MilitaryRank

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler


class MilitaryRankSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, military_rank: MilitaryRank) -> dict:
        return {
            'id': military_rank.military_ranks_id,
            'fullName': military_rank.fullname,
        }

    def convert_schema_to_object(self, schema: dict) -> MilitaryRank:
        military_rank = MilitaryRank()

        military_rank.military_ranks_id = schema.get('id')
        military_rank.fullname = schema.get('fullName')

        return military_rank
