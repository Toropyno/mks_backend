from typing import List

from mks_backend.errors import serialize_error_handler

from .model import ClassRank
from .schema import ClassRankSchema


class ClassRankSerializer:

    def __init__(self):
        self.schema = ClassRankSchema()

    @classmethod
    @serialize_error_handler
    def to_json(cls, class_rank: ClassRank) -> dict:
        return {
            'id': class_rank.class_ranks_id,
            'fullName': class_rank.fullname,
        }

    def convert_list_to_json(self, class_ranks: List[ClassRank]) -> List[dict]:
        return list(map(self.to_json, class_ranks))

    def convert_schema_to_object(self, schema: dict) -> ClassRank:
        class_rank = ClassRank()

        class_rank.class_ranks_id = schema.get('id')
        class_rank.fullname = schema.get('fullName')

        return class_rank
