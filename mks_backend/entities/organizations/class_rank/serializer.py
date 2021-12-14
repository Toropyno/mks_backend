from .schema import ClassRankSchema
from .model import ClassRank

from mks_backend.errors import serialize_error_handler


class ClassRankSerializer:

    def __init__(self):
        self.schema = ClassRankSchema()

    def to_mapped_object(self, class_rank: dict) -> ClassRank:
        deserialized = self.schema.deserialize(class_rank)
        return ClassRank(**deserialized)

    @classmethod
    @serialize_error_handler
    def to_json(cls, class_rank: ClassRank) -> dict:
        return {
            'id': class_rank.class_ranks_id,
            'fullName': class_rank.fullname,
        }

    def convert_list_to_json(self, class_rank: list) -> list:
        return list(map(self.to_json, class_rank))

    def convert_schema_to_object(self, schema: dict) -> ClassRank:
        class_rank = ClassRank()

        class_rank.class_rank_id = schema.get('id')
        class_rank.fullname = schema.get('fullName')

        return class_rank
