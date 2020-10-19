from mks_backend.services.fias_entity.fias import (
    append_address,
    get_by_socr_name,
)


class SubjectService:

    def __init__(self):
        self.search_subject = ''
        self.subjects = []

    def set_search_subject(self, search_subject: str) -> None:
        self.search_subject = search_subject

    def get_subjects(self, addresses: list) -> list:
        self.subjects = []
        socr_names = ['обл. ', 'обл ', 'Респ. ', 'Респ ', 'край ']
        for row_address in addresses:
            for socr in socr_names:
                self.append_subject_if_in_row_address(row_address, socr)
        return self.subjects

    def append_subject_if_in_row_address(self, row_address: str, socr_name: str) -> None:
        if socr_name + self.search_subject.lower() in row_address.lower():
            subject = get_by_socr_name(row_address, socr_name)
            if socr_name + self.search_subject.lower() in subject.lower():
                append_address(subject, self.subjects)
