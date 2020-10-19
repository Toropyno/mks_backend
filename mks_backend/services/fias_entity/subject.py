from mks_backend.services.fias_entity.fias import (
    append_address,
    get_by_socr_name,
)


class SubjectService:

    def __init__(self):
        self.search_subject = ''

    def set_search_subject(self, search_subject):
        self.search_subject = search_subject

    def get_subjects(self, addresses):
        subjects = []
        for row_address in addresses:
            self.append_subject_if_in_row_address(row_address, 'обл. ', subjects)
            self.append_subject_if_in_row_address(row_address, 'обл ', subjects)
            self.append_subject_if_in_row_address(row_address, 'Респ. ', subjects)
            self.append_subject_if_in_row_address(row_address, 'Респ ', subjects)
            self.append_subject_if_in_row_address(row_address, 'край ', subjects)
        return subjects

    def append_subject_if_in_row_address(self, row_address, socr_name, subjects):
        if socr_name in row_address:
            subj = get_by_socr_name(row_address, socr_name)
            if socr_name + self.search_subject.lower() in subj.lower():
                append_address(subj, subjects)
