from .model import Commission


class CommissionSerializer:

    @classmethod
    def convert_object_to_json(cls, commission: Commission) -> dict:
        return {
            'id': commission.commission_id,
            'code': commission.code,
            'fullName': commission.fullname,
            'indexNumber': commission.index_number,
        }

    def convert_list_to_json(self, commissions: list) -> list:
        return list(map(self.convert_object_to_json, commissions))

    def convert_schema_to_object(self, schema: dict) -> Commission:
        commission = Commission()

        commission.commission_id = schema.get('id')
        commission.code = schema.get('code')
        commission.fullname = schema.get('fullName')
        commission.index_number = schema.get('indexNumber')

        return commission
