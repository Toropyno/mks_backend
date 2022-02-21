from .already_deleted import ALREADY_DELETED_ERROR
from .duplicates import DUPLICATE_ERROR
from .fkeys import FOREIGN_KEY_ERROR
from .logical import LOGICAL_ERROR
from .not_found import NOT_FOUND_ERROR
from .programming_error import PROGRAMMING_ERROR
from .still_referenced import STILL_REFERENCED


DB_ERROR_CODES = dict(
    **ALREADY_DELETED_ERROR,
    **PROGRAMMING_ERROR,
    **DUPLICATE_ERROR,
    **NOT_FOUND_ERROR,
    **FOREIGN_KEY_ERROR,
    **LOGICAL_ERROR,
    **STILL_REFERENCED,
)
