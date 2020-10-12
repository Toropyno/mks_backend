import requests
from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from mks_backend.errors.handle_controller_error import handle_db_error


@view_defaults(renderer='json')
class FIASController:

    def __init__(self, request: Request):
        self.request = request

    @handle_db_error
    @view_config(route_name='get_fias')
    def get_fias(self):
        text = self.request.matchdict['text']
        url = 'http://172.23.137.67/fiasapi/find/'
        url += text
        url += '?suggests=10'

        resp = requests.get(
            url=url,
            headers={
                'Authorization': 'Basic dXNlcjoxMTExMTExMQ==',
            },
        )

        response = resp.json()
        addresses = [rr['text'] for rr in response]

        return addresses
