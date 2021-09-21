from typing import Optional

from .api import FIASAPI
from .repository import FIASrepo
from .model import FIAS

REGIONS = ['Область', 'Край']
AREAS = ['Район']
CITIES = ['Город']
SETTLEMENTS = ['Населенный пункт', 'Поселок']
STREETS = ['Улица', 'Квартал']
HOMES = ['Дом']
BODIES = ['Корпус']
STRUCTURES = ['Строение', 'Территория']


class FIASService:
    def __init__(self):
        self.repo = FIASrepo()
        self.api = FIASAPI()

    def get_suggests(self, search_text: str):
        return self.api.get_suggests(search_text)

    def get_fias_address(self, search_text: str) -> Optional[FIAS]:
        """
        Get strong fias address by search text
        """
        fias_address = self.api.get_strong_suggest(search_text)
        if fias_address:
            fias_address = self.expand_adress(fias_address['aoid'])
        return fias_address

    def create_address_from_dict(self, address_dict: dict):
        """
        Create search text by dict with keys:
        [region, area, city, settlement, street, home, body, structure]
        """
        address = filter(lambda x: x, [
            address_dict.get('region'),
            address_dict.get('area'),
            address_dict.get('city'),
            address_dict.get('settlement'),
            address_dict.get('street'),
            address_dict.get('home'),
            address_dict.get('body'),
            address_dict.get('structure'),
        ])
        search_text = ', '.join(map(str, address))
        return search_text

    def expand_adress(self, aoid: str) -> FIAS:
        """
        Create FIAS-sqlalchemy object from expanded dict
        """
        fias_address = self.repo.get_fias_by_aoid(aoid)
        if not fias_address:
            fias_address = FIAS(aoid=aoid)
            expanded_address = self.api.expand(aoid)
            for row in expanded_address:
                socrname = row['socrname']
                value = row['shortname'] + ' ' + row['formalname']
                if socrname in REGIONS:
                    fias_address.region = value
                elif socrname in AREAS:
                    fias_address.area = value
                elif socrname in CITIES:
                    fias_address.city = value
                elif socrname in SETTLEMENTS:
                    fias_address.settlement = value
                elif socrname in STREETS:
                    fias_address.street = value
                elif socrname in HOMES:
                    fias_address.home = value
                elif socrname in BODIES:
                    fias_address.body = value
                elif socrname in STRUCTURES:
                    fias_address.structure = value
                else:
                    print('Идентификатор "{}" не найден'.format(socrname))
        return fias_address

    def get_data_for_filtration(self):
        """
        return all regions, areas, cities, settlements fir filtration
        """
        regions = self.repo.get_distincts(FIAS.region)
        areas = self.repo.get_distincts(FIAS.area)
        cities = self.repo.get_distincts(FIAS.city)
        settlements = self.repo.get_distincts(FIAS.settlement)

        return {
            'regions': [{'name': value} for value in regions] if regions else None,
            'areas': [{'name': value} for value in areas] if areas else None,
            'cities': [{'name': value} for value in cities] if cities else None,
            'settlements': [{'name': value} for value in settlements] if settlements else None,
        }
