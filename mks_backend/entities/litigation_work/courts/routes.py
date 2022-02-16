def include_court(config):
    config.add_route('get_all_courts', '/court', request_method='GET')
    config.add_route('add_court', '/court', request_method='POST')
    config.add_route('delete_court', '/court/{id}', request_method='DELETE')
    config.add_route('edit_court', '/court/{id}', request_method='PUT')
    config.add_route('get_court', '/court/{id}', request_method='GET')
