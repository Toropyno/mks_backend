from datetime import datetime


def set_upload_date_by_idfilestorage(document, old_document):
    if not document.idfilestorage:
        document.upload_date = None
    elif (not old_document and document.idfilestorage) or \
            (old_document.idfilestorage != document.idfilestorage):
        document.upload_date = datetime.now()
    else:
        document.upload_date = old_document.upload_date
