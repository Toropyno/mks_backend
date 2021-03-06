import json

from mks_backend.session import DBSession

from .model import MIVLog


class MIVLogger:

    def log(self, notify: str):
        log_record = json.loads(notify).get('message_status')
        DBSession.add(MIVLog(**log_record))
        DBSession.commit()
