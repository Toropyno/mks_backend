from pyramid.view import view_config, view_defaults
from pyramid.response import Response

from mks_backend.services.miv.miv import MIVService
from mks_backend.services._loggers.miv import MIVLogger


@view_defaults(renderer='json')
class MIVController:
    def __init__(self, request):
        self.request = request
        self.service = MIVService()
        self._logger = MIVLogger()

    @view_config(route_name='miv_receive')
    def receive_message(self):
        self.service.process_data(self.request)
        return Response(status=201)

    @view_config(route_name='miv_options')
    def miv_options(self):
        response = Response(status=204)
        response.headers['Access-Control-Allow-Methods'] = 'POST,OPTIONS'
        return response

    @view_config(route_name='miv_notify')
    def receive_status_notification_message(self):
        self._logger.log(self.request.body.decode())
        return Response(status=200)

    @view_config(route_name='miv_send')
    def send_message(self):
        message = self.request.json_body
        recipient = self.request.json_body['recipient']
        return self.service.send_message(message, recipient)
