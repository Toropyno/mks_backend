from datetime import datetime


def update_idfilestorage_with_upload_date(construction_document, old_idfilestorage):
    schema_idfilestorage = construction_document.idfilestorage
    if old_idfilestorage:
        if str(old_idfilestorage) != str(schema_idfilestorage):
            construction_document.idfilestorage = schema_idfilestorage
            construction_document.upload_date = datetime.now()
    else:
        if schema_idfilestorage:
            construction_document.upload_date = datetime.now()
    return construction_document


def set_upload_date(construction_document_deserialized, old_construction_document):
    construction_document_deserialized['uploadDate'] = old_construction_document.upload_date
