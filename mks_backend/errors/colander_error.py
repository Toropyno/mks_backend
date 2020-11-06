def get_collander_error_dict(errors: dict) -> dict:
    return {'code': list(errors.keys()).pop(), 'message': '.\n\n'.join(errors.values())}
