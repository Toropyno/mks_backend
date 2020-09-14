def get_dictionary_with_errors_correct_format(errors: dict) -> dict:
    return {'code': 'validationError', 'message': '.\n\r'.join(errors.values())}
