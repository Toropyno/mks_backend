def include_completion_dates(config):
    config.add_route('get_all_completion_dates_by_contract', '/contract/{id}/completion_date', request_method='GET')
    config.add_route('add_completion_date', '/completion_date', request_method='POST')
    config.add_route('edit_completion_date', '/completion_date/{id}', request_method='PUT')
    config.add_route('get_completion_date', '/completion_date/{id}', request_method='GET')
    config.add_route('delete_completion_date', '/completion_date/{id}', request_method='DELETE')
