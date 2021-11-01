def include_litigation(config):
    config.add_route('get_all_litigations', '/litigation', request_method='GET')
    config.add_route('add_litigation', '/litigation', request_method='POST')
    config.add_route('delete_litigation', '/litigation/{id}', request_method='DELETE')
    config.add_route('edit_litigation', '/litigation/{id}', request_method='PUT')
    config.add_route('get_litigation', '/litigation/{id}', request_method='GET')
