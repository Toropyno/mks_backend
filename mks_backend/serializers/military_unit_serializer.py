from mks_backend.errors.serilize_error import serialize_error_handler


class MilitaryUnitSerializer:

    @serialize_error_handler
    def convert_object_to_json(self, military_unit):
        return {
            'id': military_unit.idMU,
            'fullName': self.get_correct_military_unit_name(military_unit),
        }

    def convert_list_to_json(self, military_units):
        return list(map(self.convert_object_to_json, military_units))

    def convert_list_to_json_tree(self, military_units):
        tree = []
        for military_unit in military_units:
            node = self.convert_object_to_json(military_unit)
            children = self.convert_list_to_json_tree(military_unit.children)
            if children != []:
                node['children'] = children
            else:
                node['children'] = []
            tree.append(node)

        return tree

    def get_correct_military_unit_name(self, military_unit):
        if military_unit.vChNumber and military_unit.idNameMU:
            return military_unit.vChNumber + ' ' + military_unit.name_military_unit.namemu
        else:
            return military_unit.name_military_unit.namemu
