from typing import List, Optional

import requests
from requests.auth import HTTPBasicAuth

from mks_backend.settings import SETTINGS


class FIASAPI:
    def __init__(self):
        self.url = SETTINGS['FIAS_URL']
        self.auth = HTTPBasicAuth(SETTINGS['FIAS_USER'], SETTINGS['FIAS_PASSWORD'])

    def get_suggests(self, input_str: str) -> List[dict]:
        response = requests.get(
            self.url + '/find/{}'.format(input_str),
            params={'suggests': 10},
            auth=self.auth
        ).json()
        return response

    def get_strong_suggest(self, input_str: str) -> Optional[dict]:
        response = requests.get(
            self.url + '/find/{}'.format(input_str),
            params={'strong': 1},
            auth=self.auth
        ).json()

        if isinstance(response, dict):
            return None
        else:
            return response[0]

    def expand(self, aoid: str) -> List[dict]:
        response = requests.get(
            self.url + '/expand/{}'.format(aoid),
            auth=self.auth
        ).json()

        return response
