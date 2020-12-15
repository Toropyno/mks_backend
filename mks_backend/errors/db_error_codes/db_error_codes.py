from mks_backend.errors.db_error_codes.already_deleted import ALREADY_DELETED_ERROR
from mks_backend.errors.db_error_codes.programming_error import PROGRAMMING_ERROR
from mks_backend.errors.db_error_codes.duplicates import DUPLICATE_ERROR
from mks_backend.errors.db_error_codes.not_found import NOT_FOUND_ERROR
from mks_backend.errors.db_error_codes.fkeys import FOREIGN_KEY_ERROR
from mks_backend.errors.db_error_codes.logical import LOGICAL_ERROR

DB_ERROR_CODES = dict(
    **ALREADY_DELETED_ERROR,
    **PROGRAMMING_ERROR,
    **DUPLICATE_ERROR,
    **NOT_FOUND_ERROR,
    **FOREIGN_KEY_ERROR,
    **LOGICAL_ERROR,
)
