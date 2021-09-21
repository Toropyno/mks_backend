def include_constructions(config):
    config.add_route('get_all_constructions', '/construction', request_method='GET')
    config.add_route('add_construction', '/construction', request_method='POST')
    config.add_route('delete_construction', '/construction/{id}', request_method='DELETE')
    config.add_route('edit_construction', '/construction/{id}', request_method='PUT')
    config.add_route('get_construction', '/construction/{id}', request_method='GET')
