from .model import MilitaryRank

from mks_backend.errors import serialize_error_handler


class MilitaryRankSerializer:

    @classmethod
    @serialize_error_handler
    def to_json(cls, military_rank: MilitaryRank) -> dict:
        return {
            'id': military_rank.military_ranks_id,
            'fullName': military_rank.fullname,
        }

    def convert_list_to_json(self, military_ranks: list) -> list:
        return list(map(self.to_json, military_ranks))

    def convert_schema_to_object(self, schema: dict) -> MilitaryRank:
        military_rank = MilitaryRank()

        military_rank.military_ranks_id = schema.get('id')
        military_rank.fullname = schema.get('fullName')

        return military_rank