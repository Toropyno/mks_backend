from typing import Tuple

from .model import LitigationSubject


class LitigationSubjectSerializer:

    def to_mapped_object(self, litigation_id: int, construction_id: int) -> LitigationSubject:
        return LitigationSubject(litigation_id=litigation_id, construction_id=construction_id)

    def convert_list_to_objects(self, litigation_id: int, constructions: list) -> Tuple[LitigationSubject]:
        return tuple(
            self.to_mapped_object(litigation_id, construction_id) for construction_id in constructions
        )
