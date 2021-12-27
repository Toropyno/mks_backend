from abc import ABC, abstractmethod
from typing import List, Dict

from mks_backend.session import Base


class BaseSerializer(ABC):

    def convert_list_to_json(self, entities: List[Base]) -> List[Dict]:
        return list(map(self.to_json, entities))

    @abstractmethod
    def to_json(self, entity: Base) -> Dict:
        raise NotImplementedError
