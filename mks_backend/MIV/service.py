from pyramid.request import Request
from streaming_form_data import StreamingFormDataParser

from .targets import PayloadTarget, JSONTarget
from .repository import MIVRepository

from .strategy import Context


class MIVService:

    def __init__(self):
        self.repo = MIVRepository()

    def process_data(self, request: Request):
        sender = request.headers.environ.get('HTTP_KRN_SENDER')
        uid = request.headers.environ.get('HTTP_KRN_UID')

        meta_target = JSONTarget(sender=sender, uid=uid)
        payload_target = PayloadTarget(sender=sender, uid=uid)

        parser = StreamingFormDataParser(headers=request.headers)
        parser.register('meta', meta_target)
        parser.register('payload', payload_target)

        for chunk in request.body_file_raw:
            parser.data_received(chunk)

        Context(sender).do_algorithm(
            meta_target.value,
            payload_target.value,
            uid,
        )

    def send_message(self, message: dict, recipient: str):
        return self.repo.send_message(message=message, recipient=recipient)
