import json

from mks_backend.repositories import DBSession
from mks_backend.models._loggers.miv import MIVLog


class MIVLogger:

    def log(self, notify: str):
        log_record = json.loads(notify).get('message_status')
        DBSession.add(MIVLog(**log_record))
        DBSession.commit()
