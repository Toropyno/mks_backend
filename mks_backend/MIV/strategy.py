from mks_backend.settings import SETTINGS

from .parsing import DefaultStrategy, SAKURAStrategy

STRATEGIES = {
    SETTINGS['EXTR_DOCS_MIV_SENDER']: SAKURAStrategy,
}


class Context:
    """
    Depending on the sender, selects the appropriate strategy
    for processing the received data
    """
    def __init__(self, sender: str) -> None:
        self._strategy = STRATEGIES.get(sender, DefaultStrategy)

    def do_algorithm(self, *args) -> None:
        result = self._strategy(*args).do_algorithm()
        return result
