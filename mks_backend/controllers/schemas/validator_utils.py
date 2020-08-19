import re
from datetime import datetime

import colander

from mks_backend.repositories.construction_categories_repository import ConstructionCategoryRepository
from mks_backend.repositories.construction_subcategories_repository import ConstructionSubcategoryRepository


def date_validator(node, value):
    try:
        value = datetime.strptime(value, '%a %b %d %Y')
    except ValueError:
        raise colander.Invalid(node, 'Неверный формат даты')


def uuid_validator(node, value):
    pattern = '^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[4][0-9a-fA-F]{3}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
    res = re.match(pattern, value)
    if res is None:
        raise colander.Invalid(node, 'Недопустимая информация о файле')


def construction_category_validator(node, value):
    if not ConstructionCategoryRepository.get_construction_category_by_id(value):
        raise colander.Invalid(node, 'Такой категории для проекта не существует')


def construction_subcategory_validator(node, value):
    if not ConstructionSubcategoryRepository.get_construction_subcategory_by_id(value):
        raise colander.Invalid(node, 'Такой подкатегории для проекта не существует')
