class BusinessLogicError(Exception):
    codes = {
        'no_details': 'Для юридического лица должны быть заполнены ИНН, КПП и ОГРН',
    }

    def __init__(self, code: str):
        self.code = code
        self.msg = self.codes[code]
