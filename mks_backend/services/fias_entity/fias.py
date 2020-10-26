from mks_backend.errors.db_basic_error import db_error_handler

from mks_backend.models.fias import FIAS
from mks_backend.repositories.fias_entity.api import FIASAPIRepository
from mks_backend.repositories.fias_entity.fias import FIASRepository
from mks_backend.services.fias_entity.api import FIASAPIService
from mks_backend.services.fias_entity.utils import get_search_address

from mks_backend.services.fias_entity.city_locality import CityLocalityService
from mks_backend.services.fias_entity.district import DistrictService
from mks_backend.services.fias_entity.remaining_address import RemainingAddressService
from mks_backend.services.fias_entity.subject import SubjectService


class FIASService:

    def __init__(self):
        self.repo = FIASRepository()
        self.service_api = FIASAPIService()
        self.repo_api = FIASAPIRepository()

    def add_address_fias(self, fias):
        search_address = get_search_address(fias)
        if search_address == '':
            return

        aoid = self.get_aoid(search_address)
        fias_db = self.get_fias_by_aoid(aoid)

        if not fias_db:
            fias.aoid = aoid
            self.add_fias(fias)
        else:
            fias = fias_db

        return fias

    def get_fias_by_aoid(self, aoid: str) -> FIAS:
        return self.repo.get_fias_by_aoid(aoid)

    @db_error_handler
    def add_fias(self, fias: FIAS) -> None:
        self.repo.add_fias(fias)

    def get_all_fiases(self) -> list:
        return self.repo.get_all_fiases()

    def get_fias_by_id(self, id: int) -> FIAS:
        return self.repo.get_fias_by_id(id)

    def delete_fias_by_id(self, id: int) -> None:
        self.repo.delete_fias_by_id(id)

    def delete_unnecessary_fias(self, id: int) -> None:
        allowed = self.check_for_links_in_constructions(id)
        if allowed:
            self.repo.delete_fias_by_id(id)

    def check_for_links_in_constructions(self, id: int) -> bool:
        fias = self.get_fias_by_id(id)
        if not fias.constructions:
            return True
        else:
            return False

    def get_split_full_fias(self, full_fias: str):
        street = 0
        for name in RemainingAddressService.SORC_NAMES:
            if name in full_fias:
                street += 1
        if street == 0:
            return

        fias = FIAS()

        aoid = self.get_aoid(full_fias)
        fias.aoid = aoid

        address_by_aoid = self.repo_api.get_by_aoid_response(aoid).json()
        fill_in_all_fields(address_by_aoid, fias)
        if not fias.remaining_address:
            return
        return fias

    def get_aoid(self, search_address: str) -> str:
        return self.service_api.get_aoid(search_address)


def fill_in_all_fields(address_by_aoid, fias) -> None:
    subject = ''
    district = ''
    city = ''
    locality = ''
    remaining_address = ''

    for row in address_by_aoid:
        subject_row = fill_in_field(row, SubjectService.SORC_NAMES)
        if subject_row:
            subject += subject_row + ' '

        district_row = fill_in_field(row, DistrictService.SORC_NAMES)
        if district_row:
            district += district_row + ' '

        city_row = fill_in_field(row, CityLocalityService.CITY_SORC_NAMES)
        if city_row:
            city += city_row + ' '

        locality_row = fill_in_field(row, CityLocalityService.LOCALITY_SORC_NAMES)
        if locality_row:
            locality += locality_row + ' '

        remaining_address_row = fill_in_field(row, RemainingAddressService.SORC_NAMES)
        if remaining_address_row:
            remaining_address += remaining_address_row + ' '

    if subject:
        fias.subject = subject.strip(' ')
    if district:
        fias.district = district.strip(' ')
    if city:
        fias.city = city.strip(' ')
    if locality:
        fias.locality = locality.strip(' ')
    if remaining_address:
        fias.remaining_address = remaining_address.strip(' ')


def fill_in_field(row: dict, socr_names: list) -> str:
    for socr_name in socr_names:
        if socr_name.strip(' ') == row.get('shortname'):
            return row.get('shortname') + ' ' + row.get('formalname')
