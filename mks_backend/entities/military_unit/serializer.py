from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler

from .models import MilitaryUnit


class MilitaryUnitSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, military_unit: MilitaryUnit) -> dict:
        return {
            'id': military_unit.idMU,
            'fullName': cls.get_correct_military_unit_name(military_unit),
        }

    def convert_list_to_json_tree(self, military_units: list) -> list:
        tree = []
        for military_unit in military_units:
            node = self.to_json(military_unit)
            children = self.convert_list_to_json_tree(military_unit.children)
            if children:
                node['children'] = children
            else:
                node['children'] = []
            tree.append(node)

        return tree

    @classmethod
    @serialize_error_handler
    def get_correct_military_unit_name(cls, military_unit: MilitaryUnit) -> str:
        if military_unit.idPurpose in [130, 140, 150, 160, 310, 410, 510]:
            name = 'Управление '
            if military_unit.parent.vChNumber:
                name += military_unit.parent.vChNumber + ' '
            name += military_unit.parent.name_military_unit.snamemu
        else:
            if military_unit.vChNumber:
                name = military_unit.vChNumber + ' ' + military_unit.name_military_unit.snamemu
            else:
                if military_unit.name_military_unit.snamemu:
                    name = military_unit.name_military_unit.snamemu
                else:
                    name = military_unit.name_military_unit.namemu
        return name
