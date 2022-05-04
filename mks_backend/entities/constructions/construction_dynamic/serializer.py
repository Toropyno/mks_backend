from datetime import datetime

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.errors import serialize_error_handler
from mks_backend.utils.date_and_time import get_date_string, get_date_time_string

from .model import ConstructionDynamic


class ConstructionDynamicSerializer(BaseSerializer):

    @classmethod
    @serialize_error_handler
    def to_json(cls, construction_dynamic: ConstructionDynamic) -> dict:
        return {
            'id': construction_dynamic.construction_dynamics_id,
            'constructionId': construction_dynamic.construction_id,
            'reportingDate': get_date_string(construction_dynamic.reporting_date),
            'peoplePlan': construction_dynamic.people_plan,
            'people': construction_dynamic.people,
            'equipmentPlan': construction_dynamic.equipment_plan,
            'equipment': construction_dynamic.equipment,
            'description': construction_dynamic.description,
            'reason': construction_dynamic.reason,
            'problems': construction_dynamic.problems,
            'fromSakura': construction_dynamic.from_sakura,
            'updateDatetime': get_date_time_string(construction_dynamic.update_datetime),
        }

    def to_mapped_object(self, dynamic: dict) -> ConstructionDynamic:
        return ConstructionDynamic(
            construction_dynamics_id=dynamic.get('id'),
            reporting_date=dynamic.get('reportingDate'),
            from_sakura=dynamic.get('fromSakura'),
            people_plan=dynamic.get('peoplePlan'),
            people=dynamic.get('people'),
            equipment_plan=dynamic.get('equipmentPlan'),
            equipment=dynamic.get('equipment'),
            description=dynamic.get('description'),
            reason=dynamic.get('reason'),
            problems=dynamic.get('problems'),
            construction_id=dynamic.get('constructionId'),
            update_datetime=datetime.now()
        )
