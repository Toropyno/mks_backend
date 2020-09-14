def get_collander_error_dict(errors: dict) -> dict:
    return {'code': 'validationError', 'message': '.\n\r'.join(errors.values())}
