from mks_backend.services.fias_entity.fias import (
    append_address,
    get_by_socr_name,
)


class LocalityService:

    def __init__(self):
        self.text = ''

    def set_text(self, text):
        self.text = text
