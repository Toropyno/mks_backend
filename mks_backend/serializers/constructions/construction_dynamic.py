from mks_backend.models.constructions.construction_dynamic import ConstructionDynamic

from mks_backend.serializers.utils.date_and_time import get_date_time_string, get_date_string


class ConstructionDynamicSerializer:

    def convert_list_to_json(self, construction_dynamics: list) -> list:
        return list(map(self.to_json, construction_dynamics))

    def to_json(self, construction_dynamic: ConstructionDynamic) -> dict:
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

    def to_mapped_object(self, dynamic: dict):
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
            construction_id=dynamic.get('constructionId')
        )
