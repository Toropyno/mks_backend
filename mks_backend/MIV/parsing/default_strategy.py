import json
from os import environ
from os import path as os_path

from .abstract_strategy import Strategy


class DefaultStrategy(Strategy):
    """
    Save input message to the JSON_PATH (if meta != None) as {uid}.json
    and to the FILESTORAGE_PATH (if payload != None) as {uid} without extension
    """
    JSON_PATH = environ.get('MIV_JSON_PATH', '/tmp')
    FILESTORAGE_PATH = environ.get('MIV_FILESTORAGE_PATH', '/tmp')

    def __init__(self, meta, payload, uid):
        self.meta = meta
        self.payload = payload
        self.uid = uid

    def do_algorithm(self, *args):
        if self.meta:
            path = os_path.join(self.JSON_PATH, '{uid}'.format(uid=self.uid))
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(self.meta, f, ensure_ascii=False, indent=4)

        if self.payload:
            path = os_path.join(self.FILESTORAGE_PATH, self.uid)
            with open(path, 'wb') as output_stream:
                output_stream.write(self.payload)
