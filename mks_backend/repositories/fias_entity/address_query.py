import requests


class FIASAPIRepository:
    AUTHORIZATION_FIAS_in_DEV = 'Basic dXNlcjoxMTExMTExMQ=='
    URL_FIAS_API = 'http://172.23.137.67/fiasapi/'

    def __init__(self):
        self.suggests = 15

    def get_fias_response(self, search_text: str) -> requests.Response:
        return requests.get(
            url=self.URL_FIAS_API + 'find/' + search_text + '?suggests=' + str(self.suggests),
            headers={
                'Authorization': self.AUTHORIZATION_FIAS_in_DEV
            },
        )

    def get_details_by_aoid(self, aoid: str) -> requests.Response:
        return requests.get(
            url=self.URL_FIAS_API + 'expand/' + aoid,
            headers={
                'Authorization': self.AUTHORIZATION_FIAS_in_DEV
            },
        )
