from datetime import datetime


def set_upload_date(document_deserialized, old_document):
    document_deserialized['uploadDate'] = old_document.upload_date


def set_upload_date_by_idfilestorage(document, old_document):
    if not document.idfilestorage:
        document.upload_date = None
    elif (not old_document and document.idfilestorage) or \
            (str(old_document.idfilestorage) != str(document.idfilestorage)):
        document.upload_date = datetime.now()
    else:
        document.upload_date = old_document.upload_date
