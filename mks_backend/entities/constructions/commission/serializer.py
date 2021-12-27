from .model import Commission

from mks_backend.entities.BASE.serializer import BaseSerializer


class CommissionSerializer(BaseSerializer):

    @classmethod
    def to_json(cls, commission: Commission) -> dict:
        return {
            'id': commission.commission_id,
            'code': commission.code,
            'fullName': commission.fullname,
            'indexNumber': commission.index_number,
        }

    def to_mapped_object(self, schema: dict) -> Commission:
        commission = Commission()

        commission.commission_id = schema.get('id')
        commission.code = schema.get('code')
        commission.fullname = schema.get('fullName')
        commission.index_number = schema.get('indexNumber')

        return commission
