from mimetypes import guess_type as guess_mimetype
from os import path as os_path, remove as os_remove
from shutil import copyfileobj

from webob.compat import cgi_FieldStorage

from mks_backend.errors.filestorage_error import FilestorageError
from mks_backend.settings import SETTINGS


class FilestorageHDD:
    FILE_STORAGE = SETTINGS['FILE_STORAGE']
    PHOTO_ALLOWED_EXTENSIONS = SETTINGS['PHOTO_ALLOWED_EXTENSIONS']

    def create_file(self, id_file_storage: str, file: cgi_FieldStorage, all_formats: bool = True) -> None:
        if not isinstance(file, cgi_FieldStorage):
            raise FilestorageError('not_received')
        elif file.limit > 5e+9:  # > ~5Gbytes
            raise FilestorageError('too_big')
        elif '.' not in file.filename:
            raise FilestorageError('extension_error')
        elif not all_formats and file.filename.split('.')[-1] not in self.PHOTO_ALLOWED_EXTENSIONS:
            raise FilestorageError('extension_error')

        file_path = os_path.join(self.FILE_STORAGE, id_file_storage)
        try:
            with open(file_path, 'wb') as output_file:
                copyfileobj(file.file, output_file)
        except OSError:
            raise FilestorageError('internal_error')

    def guess_mime_type(self, filename: str) -> str:
        mime_type = guess_mimetype(filename, strict=False)[0]  # return (type, encoding)

        if mime_type and len(mime_type) < 45:  # max length for models.Filestorage.mimeType
            return mime_type
        else:
            return 'unknown/type'

    def get_path_to_file(self, uuid: str) -> str:
        protocol_file = os_path.join(self.FILE_STORAGE, uuid)
        if os_path.exists(protocol_file):
            return protocol_file
        else:
            raise FilestorageError('nf_in_hdd')

    def delete_by_id(self, uuid: str) -> None:
        path_to_file = os_path.join(self.FILE_STORAGE, uuid)
        if os_path.exists(path_to_file):
            os_remove(path_to_file)
