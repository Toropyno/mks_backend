from os import path as os_path, remove as os_remove
from urllib import request as urllib_request
from shutil import copyfileobj
from mimetypes import guess_type as guess_mimetype

from webob.compat import cgi_FieldStorage

from mks_backend.models.filestorage import Filestorage
from mks_backend.models import DBSession


class FilestorageRepository(object):
    PROTOCOL_STORAGE = '/tmp/protocols/'
    ALLOWED_EXTENSIONS = [
        'doc', 'docx', 'docm',
        'pdf', 'odt', 'txt',
    ]

    def add_filestorage(self, file):
        DBSession.add(file)
        DBSession.commit()

    def create_file(self, id_file_storage, file):
        if not isinstance(file, cgi_FieldStorage):
            raise ValueError('Файл не был получен сервером!')
        elif file.limit > 2.6e+7:  # > ~25Mbytes
            raise ValueError('Файл слишком большой!')
        elif '.' not in file.filename or \
                file.filename.split('.')[1] not in self.ALLOWED_EXTENSIONS:
            raise ValueError('Расширение файла недопустимо или отсутствует!')

        try:
            file_path = os_path.join(self.PROTOCOL_STORAGE, id_file_storage)
            with open(file_path, 'wb') as output_file:
                copyfileobj(file.file, output_file)
        except OSError:
            # frontend doesn't need to know confidential data
            raise OSError('Файл не был записан из-за внутренней ошибки!')

    def guess_mime_type(self, filename):
        mime_type = guess_mimetype(filename, strict=False)[0]  # return (type, encoding)

        if mime_type and len(mime_type) < 30:  # max length for models.Filestorage.mimeType
            return mime_type
        else:
            return 'unknow/type'

    def get_file(self, id):
        protocol_file = self.PROTOCOL_STORAGE + id
        if os_path.exists(protocol_file):
            file = self.get_filestorage_by_id(id)
            protocol_filename = file.filename
            protocol_filename = urllib_request.quote(protocol_filename.encode('utf-8'))
            return protocol_file, protocol_filename
        else:
            return None, None

    @classmethod
    def get_filestorage_by_id(cls, id):
        return DBSession.query(Filestorage).get(id)

    @classmethod
    def delete_filestorage_by_id(cls, id):
        # delete from DB
        filestorage = cls.get_filestorage_by_id(id)
        DBSession.delete(filestorage)
        DBSession.commit()
        #  delete from filesystem
        path_to_file = cls.PROTOCOL_STORAGE + id
        if os_path.exists(path_to_file):
            os_remove(path_to_file)
