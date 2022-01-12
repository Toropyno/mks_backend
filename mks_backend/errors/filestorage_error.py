class FilestorageError(Exception):
    codes = {
        'not_received': 'Файл не был получен сервером!',
        'too_big': 'Файл слишком большой: размер загружаемого файла не должен превышать 1 Гб!',
        'extension_error': 'Расширение файла недопустимо или отсутствует!',
        'internal_error': 'Файл не был записан из-за внутренней ошибки',
        'nf_in_hdd': 'Файл не найден на жестком диске!',
        'nf_in_db': 'Файл не найден в базе данных!',
    }

    def __init__(self, code: str):
        self.code = code
        self.msg = self.codes[code]
