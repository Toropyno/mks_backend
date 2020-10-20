import requests
from requests import Response


def get_fias_response(search_text: str) -> Response:
    return requests.get(
        url='http://172.23.137.67/fiasapi/find/' + search_text + '?suggests=15',
        headers={
            'Authorization': 'Basic dXNlcjoxMTExMTExMQ=='
        },
    )


def get_by_AOID_response(aoid: str) -> Response:
    return requests.get(
        url='http://172.23.137.67/fiasapi/expand/' + aoid,
        headers={
            'Authorization': 'Basic dXNlcjoxMTExMTExMQ=='
        },
    )
