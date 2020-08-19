class CommissionSerializer:
    def convert_object_to_json(self, commission):
        return {
            'id': commission.commission_id,
            'code': commission.code,
            'fullName': commission.fullname
        }

    def convert_list_to_json(self, constructions):
        return list(map(self.convert_object_to_json, constructions))
