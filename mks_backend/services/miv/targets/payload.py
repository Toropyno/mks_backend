from os import environ
from os import path as os_path
from datetime import datetime

from streaming_form_data.targets import BaseTarget

from mks_backend.repositories.miv.storage import StorageRepository, Storage


class PayloadTarget(BaseTarget):
    """
    Used to process the 'payload' field in the message.
    'payload' could be any mime-type, default - application/octet-stream
    Writes (streams) the input to an on-disk file in FILESTORAGE_PATH
    """
    FILESTORAGE_PATH = environ['MIV_FILESTORAGE_PATH']

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
            self.write_to_file()

    def write_to_db(self):
        self.repo.add_storage(Storage(
            uid=self.uid,
            type='binary',
            sender=self.sender,
            dt_received=datetime.now()
        ))

    def write_to_file(self):
        path = os_path.join(self.FILESTORAGE_PATH, self.uid)
        with open(path, 'wb') as output_stream:
            output_stream.write(self.value)

    @property
    def value(self):
        return b''.join(self._values)
