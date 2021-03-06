from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.entities.work_list.element_type import ElementTypeSerializer
from mks_backend.entities.work_list.measure_unit import MeasureUnitSerializer
from mks_backend.entities.work_list.work_type import WorkTypeSerializer
from mks_backend.utils.date_and_time import get_date_string

from .model import WorkList


class WorkListSerializer(BaseSerializer):

    def to_json(self, work_list: WorkList) -> dict:
        return {
            'id': work_list.works_list_id,
            'constructionObject': work_list.construction_objects_id,
            'element': ElementTypeSerializer.to_json(
                work_list.element_type
            ),
            'elementDescription': work_list.element_description,
            'weight': work_list.weight,
            'beginDate': get_date_string(work_list.begin_date),
            'endDate': get_date_string(work_list.end_date),
            'plan': float(work_list.plan),
            'fact': float(work_list.fact),
            'measureUnit': MeasureUnitSerializer.to_json(
                work_list.measure_unit
            ),
            'workType': WorkTypeSerializer.to_json(
                work_list.work_type
            ),
            'workDescription': work_list.work_description,
            'relevanceDate': get_date_string(work_list.relevance_date),
            'note': work_list.note
        }

    def to_mapped_object(self, schema: dict) -> WorkList:
        work_list = WorkList()

        work_list.works_list_id = schema.get('id')
        work_list.construction_objects_id = schema.get('constructionObject')
        work_list.element_types_id = schema.get('element')
        work_list.weight = schema.get('weight')
        work_list.element_description = schema.get('elementDescription')
        work_list.begin_date = schema.get('beginDate')
        work_list.end_date = schema.get('endDate')
        work_list.unit_id = schema.get('measureUnit')
        work_list.plan = schema.get('plan')
        work_list.fact = schema.get('fact')
        work_list.work_types_id = schema.get('workType')
        work_list.work_description = schema.get('workDescription')
        work_list.note = schema.get('note')
        work_list.relevance_date = schema.get('relevanceDate')

        return work_list
