class ConstructionStageSerializer:

    def convert_object_to_json(self, construction_stage):
        construction_stage_dict = {
            'id': construction_stage.construction_stages_id,
            'code': construction_stage.code,
            'fullName': construction_stage.fullname,
        }
        return construction_stage_dict

    def convert_list_to_json(self, construction_stages):
        construction_stages_array = []

        for construction_stage in construction_stages:
            construction_stage_dict = self.convert_object_to_json(construction_stage)
            construction_stages_array.append(construction_stage_dict)

        return construction_stages_array
