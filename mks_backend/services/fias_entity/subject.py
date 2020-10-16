from mks_backend.services.fias_entity.fias import (
    append_address,
    get_by_socr_name,
)


class SubjectService:

    def __init__(self):
        self.text = ''

    def set_text(self, text):
        self.text = text

    def get_subjects(self, addresses):
        subjects = []
        for row_address in addresses:
            self.append_subject_if_in_row_address(row_address, 'обл.', subjects)
            self.append_subject_if_in_row_address(row_address, 'обл ', subjects)
            self.append_subject_if_in_row_address(row_address, 'Респ.', subjects)
            self.append_subject_if_in_row_address(row_address, 'Респ ', subjects)
            self.append_subject_if_in_row_address(row_address, 'край ', subjects)
        return subjects

    def append_subject_if_in_row_address(self, row_address, socr_name, subjects):
        if socr_name in row_address:
            subject = get_by_socr_name(row_address, socr_name)
            if socr_name + self.text.lower() in subject.lower():
                append_address(subject, subjects)
