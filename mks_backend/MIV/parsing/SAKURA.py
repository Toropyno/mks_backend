from xml.etree import ElementTree

from .abstract_strategy import Strategy
from .constructions import ConstructionsParserXML

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
        self.payload = ElementTree.fromstring(payload)
        self._strategy = SAKURA_STRATEGIES[self.payload.tag]

    def do_algorithm(self, *args, **kwargs):
        self._strategy(self.meta, self.payload, args, kwargs).do_algorithm()
