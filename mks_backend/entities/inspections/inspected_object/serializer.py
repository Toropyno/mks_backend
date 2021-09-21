from typing import Tuple

from .model import InspectedObject


class InspectedObjectSerializer:
    def to_object(self, inspection_id: int, contruction_id: int) -> InspectedObject:
        return InspectedObject(inspections_id=inspection_id, construction_id=contruction_id)

    def convert_list_to_objects(self, inspection_id: int, contructions: list) -> Tuple[InspectedObject]:
        return tuple(
            self.to_object(inspection_id, construction_id) for construction_id in contructions
        )
