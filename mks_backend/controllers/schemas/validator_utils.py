import re
from datetime import datetime

import colander

strip_space = lambda v: v.strip(' \t\n\r') if v else v


def date_validator(node: colander.SchemaNode, value: str) -> None:
    try:
        value = datetime.strptime(value, '%a %b %d %Y')
    except ValueError:
        raise colander.Invalid(node, 'Неверный формат даты')


def uuid_validator(node: colander.SchemaNode, value: str) -> None:
    pattern = '^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[4][0-9a-fA-F]{3}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
    res = re.match(pattern, value)
    if res is None:
        raise colander.Invalid(node, 'Недопустимая информация о файле')
