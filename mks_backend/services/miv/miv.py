from pyramid.request import Request
from streaming_form_data import StreamingFormDataParser

from mks_backend.services.miv.targets.payload import PayloadTarget
from mks_backend.services.miv.targets.json import JSONTarget
from mks_backend.repositories.miv.miv import MIVRepository


class MIVService:

    def __init__(self):
        self.repo = MIVRepository()

    def process_data(self, request: Request):
        meta_target = JSONTarget(
            sender=request.headers.environ.get('HTTP_KRN_SENDER'),
            uid=request.headers.environ.get('HTTP_KRN_UID')
        )
        payload_target = PayloadTarget(
            sender=request.headers.environ.get('HTTP_KRN_SENDER'),
            uid=request.headers.environ.get('HTTP_KRN_UID')
        )

        parser = StreamingFormDataParser(headers=request.headers)
        parser.register('meta', meta_target)
        parser.register('payload', payload_target)

        for chunk in request.body_file_raw:
            parser.data_received(chunk)

    def send_message(self, message: dict, recipient: str):
        return self.repo.send_message(message=message, recipient=recipient)
