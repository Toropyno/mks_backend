from os import environ

from pyramid.request import Request
from streaming_form_data import StreamingFormDataParser

from .repository import MIVRepository
from .strategy import Context
from .targets import JSONTarget, PayloadTarget


class MIVService:

    def __init__(self):
        self.repo = MIVRepository()

    def process_data(self, request: Request):
        sender = environ['HTTP_KRN_SENDER']
        uid = environ['HTTP_KRN_UID']

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
