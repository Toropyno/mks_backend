import requests
from requests import Response


class FIASAPIRepository:
    AUTHORIZATION_FIAS_in_DEV = 'Basic dXNlcjoxMTExMTExMQ=='

    def __init__(self):
        self.suggests = 15

    def get_fias_response(self, search_text: str) -> Response:
        return requests.get(
            url='http://172.23.137.67/fiasapi/find/' + search_text + '?suggests=' + str(self.suggests),
            headers={
                'Authorization': self.AUTHORIZATION_FIAS_in_DEV
            },
        )

    def get_details_by_aoid(self, aoid: str) -> Response:
        return requests.get(
            url='http://172.23.137.67/fiasapi/expand/' + aoid,
            headers={
                'Authorization': self.AUTHORIZATION_FIAS_in_DEV
            },
        )
