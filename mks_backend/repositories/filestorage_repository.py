from mks_backend.models.filestorage import Filestorage
from mks_backend.models import DBSession


class FilestorageRepository(object):

    def add_file(self, file):
        DBSession.add(file)
        DBSession.commit()

    def get_file(self, uuid):
        return DBSession.query(Filestorage).get(uuid)
