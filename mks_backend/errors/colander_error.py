def get_collander_error_dict(errors: dict) -> dict:
    return {'code': 'validationError', 'message': '.\n\n'.join(errors.values())}
