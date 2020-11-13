from mks_backend.models.organizations.military_rank import MilitaryRank

from mks_backend.errors.serilize_error import serialize_error_handler


class MilitaryRankSerializer:

    @classmethod
    @serialize_error_handler
    def convert_object_to_json(cls, military_rank: MilitaryRank) -> dict:
        return {
            'id': military_rank.military_ranks_id,
            'fullName': military_rank.fullname,
        }

    def convert_list_to_json(self, military_ranks: list) -> list:
        return list(map(self.convert_object_to_json, military_ranks))


    def convert_schema_to_object(self, schema: dict) -> MilitaryRank:
        military_rank = MilitaryRank()

        military_rank.military_ranks_id = schema.get('id')
        military_rank.fullname = schema.get('fullName')

        return military_rank