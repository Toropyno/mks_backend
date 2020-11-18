import json
from os import environ
from os import path as os_path

from streaming_form_data.targets import BaseTarget

from mks_backend.repositories.miv.storage import StorageRepository, Storage


class JSONTarget(BaseTarget):
    """
    Used to process the 'meta' field in the message. 'meta' is always JSON
    Received data are writes (streams) the input to an on-disk file in JSON_PATH
    """
    JSON_PATH = environ['MIV_JSON_PATH']

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
            type='json',
            sender=self.sender
        ))

    def write_to_file(self):
        path = os_path.join(self.JSON_PATH, '{uid}'.format(uid=self.uid))
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self.value, f, ensure_ascii=False, indent=4)

    @property
    def value(self):
        decoded = b''.join(self._values).decode('utf-8')
        return json.loads(decoded)
