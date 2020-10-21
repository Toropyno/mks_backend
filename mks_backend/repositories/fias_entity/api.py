import requests
from requests import Response


class FIASAPIRepository:

    def __init__(self):
        self.authorization_FIAS_in_DEV = 'Basic dXNlcjoxMTExMTExMQ=='
        self.authorization_FIAS_in_INT = ''

    def get_fias_response(self, search_text: str) -> Response:
        return requests.get(
            url='http://172.23.137.67/fiasapi/find/' + search_text + '?suggests=15',
            headers={
                'Authorization': self.authorization_FIAS_in_DEV
            },
        )

    def get_by_AOID_response(self, aoid: str) -> Response:
        return requests.get(
            url='http://172.23.137.67/fiasapi/expand/' + aoid,
            headers={
                'Authorization': self.authorization_FIAS_in_DEV
            },
        )
