def include_location_types(config):
    config.add_route('get_all_location_types', '/location_type', request_method='GET')
    config.add_route('add_location_type', '/location_type', request_method='POST')
    config.add_route('delete_location_type', '/location_type/{id}', request_method='DELETE')
    config.add_route('edit_location_type', '/location_type/{id}', request_method='PUT')
    config.add_route('get_location_type', '/location_type/{id}', request_method='GET')
