import logging
from base64 import b64decode
from xml.etree import ElementTree

from .abstract_strategy import Strategy
from .constructions import ConstructionsParserXML

logger = logging.getLogger(__name__)

SAKURA_STRATEGIES = {
    'Package': ConstructionsParserXML,
}


class SAKURAStrategy(Strategy):
    """
    Depending on the name of the table in the received xml,
    selects an appropriate strategy
    for processing and writing data to the DB
    """
    def __init__(self, meta: dict, payload: bytes, *args, **kwargs):
        self.meta = meta
        self.payload = payload
        self._strategy = SAKURA_STRATEGIES[self.payload.tag]

    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, value: bytes):
        """
        Нам нужно достать интересующий нас файл из обертки и декодировать его

        :param value:
        :return:
        """
        extr_doc_xml = ElementTree.fromstring(value)
        for child in extr_doc_xml:
            if child.tag == 'document':
                doc_body = b64decode(child.text)
                break
        else:
            logger.error('There is no "document" tag in xml')
            raise KeyError('There is no "document" tag in xml')

        self._payload = ElementTree.fromstring(doc_body)

    def do_algorithm(self, *args, **kwargs):
        self._strategy(self.meta, self.payload, args, kwargs).do_algorithm()
