from mks_backend.models.commission import Commission


class CommissionSerializer:

    @classmethod
    def convert_object_to_json(cls, commission):
        return {
            'id': commission.commission_id,
            'code': commission.code,
            'fullName': commission.fullname
        }

    def convert_list_to_json(self, constructions):
        return list(map(self.convert_object_to_json, constructions))

    def convert_schema_to_object(self, schema):
        commission = Commission()

        commission.commission_id = schema.get('id')
        commission.code = schema.get('code')
        commission.fullname = schema.get('fullName')

        return commission
