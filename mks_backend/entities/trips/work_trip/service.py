from typing import List

from .model import WorkTrip
from .repository import WorkTripRepository


class WorkTripService:

    def __init__(self):
        self.repo = WorkTripRepository()

    def get_all_work_trips(self) -> List[WorkTrip]:
        return self.repo.get_all_work_trips()

    def get_work_trip_by_id(self, id_: int) -> WorkTrip:
        return self.repo.get_work_trip_by_id(id_)

    def add_work_trip(self, work_trip: WorkTrip) -> None:
        self.repo.add_work_trip(work_trip)

    def update_work_trip(self, new_work_trip: WorkTrip) -> None:
        self.repo.update_work_trip(new_work_trip)

    def delete_work_trip_by_id(self, id_: int) -> None:
        self.repo.delete_work_trip_by_id(id_)

    def get_work_trips(self, filter_params=None) -> List[WorkTrip]:
        if filter_params:
            params = self.switch_case(filter_params)
            return self.repo.get_filtered_work_trips(params)
        else:
            return self.repo.get_all_work_trips()

    def switch_case(self, filter_params: dict) -> dict:
        case_switcher = {
            'tripName': 'trip_name',
            'tripDateStart': 'trip_date_start',
            'tripDateEnd': 'trip_date_end',
            'leadershipPosition': 'leadership_positions_id',
            'escortOfficer': 'escort_officer',

            'haveProtocol': 'have_protocol',
            'protocolDateStart': 'protocol_date_start',
            'protocolDateEnd': 'protocol_date_end',
            'protocolNumber': 'protocol_num',

            'projectCode': 'project_code',
            'isCritical': 'is_critical',
            'region': 'region',
            'haveFile': 'have_file'
        }

        params = {}
        for key, value in filter_params.items():
            if key in case_switcher and value is not None:
                params[case_switcher[key]] = filter_params[key]

        return params
