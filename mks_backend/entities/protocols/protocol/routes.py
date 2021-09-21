def include_protocols(config):
    config.add_route('get_all_protocols', '/protocol', request_method='GET')
    config.add_route('add_protocol', '/protocol', request_method='POST')
    config.add_route('delete_protocol', '/protocol/{id}', request_method='DELETE')
    config.add_route('edit_protocol', '/protocol/{id}', request_method='PUT')
    config.add_route('get_protocol', '/protocol/{id}', request_method='GET')
