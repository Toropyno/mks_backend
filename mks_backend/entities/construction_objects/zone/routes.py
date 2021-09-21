def include_zones(config):
    config.add_route('get_all_zones', '/zone', request_method='GET')
    config.add_route('add_zone', '/zone', request_method='POST')
    config.add_route('delete_zone', '/zone/{id}', request_method='DELETE')
    config.add_route('edit_zone', '/zone/{id}', request_method='PUT')
    config.add_route('get_zone', '/zone/{id}', request_method='GET')
