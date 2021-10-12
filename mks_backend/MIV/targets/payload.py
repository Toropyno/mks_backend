from datetime import datetime

from streaming_form_data.targets import BaseTarget

from ..storage import StorageRepository, Storage

from mks_backend.settings import SETTINGS


class PayloadTarget(BaseTarget):
    """
    Used to process the 'payload' field in the message.
    'payload' could be any mime-type, default - application/octet-stream
    Writes (streams) the input to an on-disk file in FILESTORAGE_PATH
    """
    FILESTORAGE_PATH = SETTINGS['MIV_FILESTORAGE_PATH']

    def __init__(self, sender, uid, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sender = sender
        self.uid = uid
        self._values = []
        self.repo = StorageRepository()

    def on_data_received(self, chunk: bytes):
        self._values.append(chunk)

    def on_finish(self):
        if self._values:
            self.write_to_db()

    def write_to_db(self):
        self.repo.add_storage(Storage(
            uid=self.uid,
            type='binary',
            sender=self.sender,
            dt_received=datetime.now()
        ))

    @property
    def value(self):
        return b''.join(self._values)
