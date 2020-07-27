from .. import models


def fake_filestorage_object(request):
    """
    Create fake filestorage object

    :return: None
    """
    files_query = request.dbsession.query(models.Filestorage)
    files_query.session.add(models.Filestorage(filename='third_file_name',
                                               uri='https://www.google.com/',
                                               filesize=1024,
                                               mimeType='text/plain',
                                               description='third file description',
                                               authorid=2))
