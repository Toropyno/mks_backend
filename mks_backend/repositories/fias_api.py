from typing import List, Optional
from os import environ

import requests
from requests.auth import HTTPBasicAuth


class FIASAPI:
    def __init__(self):
        self.url = environ.get('FIAS_URL', 'http://172.23.137.67/fiasapi')
        self.auth = HTTPBasicAuth(
            environ.get('FIAS_USER', 'user'),
            environ.get('FIAS_PASSWORD', '11111111')
        )

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
