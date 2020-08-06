from os import path as os_path, remove as os_remove
from shutil import copyfileobj
from mimetypes import guess_type as guess_mimetype


class FilestorageHDD:
    PROTOCOL_STORAGE = '/tmp/protocols/'

    def create_file(self, id_file_storage, file):
        try:
            file_path = os_path.join(self.PROTOCOL_STORAGE, id_file_storage)
            with open(file_path, 'wb') as output_file:
                copyfileobj(file.file, output_file)
        except OSError:
            raise FilestorageException(4)

    def guess_mime_type(self, filename):
        mime_type = guess_mimetype(filename, strict=False)[0]  # return (type, encoding)

        if mime_type and len(mime_type) < 45:  # max length for models.Filestorage.mimeType
            return mime_type
        else:
            return 'unknow/type'

    def get_file(self, id):
        protocol_file = self.PROTOCOL_STORAGE + id
        if os_path.exists(protocol_file):
            return protocol_file
        else:
            raise FilestorageException(5)

    @classmethod
    def delete_by_id(cls, id):
        path_to_file = cls.PROTOCOL_STORAGE + id
        if os_path.exists(path_to_file):
            os_remove(path_to_file)


class FilestorageException(Exception):
    codes = {
        1: 'Файл не был получен сервером!',
        2: 'Файл слишком большой!',
        3: 'Расширение файла недопустимо или отсутствует!',
        4: 'Файл не был записан из-за внутренней ошибки',
        5: 'Файл не найден на жестком диске!',
        6: 'Файл не найден в базе данных!',
    }

    def __init__(self, code):
        self.code = code
        self.msg = self.codes[code]
