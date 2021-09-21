def include_construction_type(config):
    config.add_route('get_all_construction_types', '/construction_type', request_method='GET')
    config.add_route('add_construction_type', '/construction_type', request_method='POST')
    config.add_route('delete_construction_type', '/construction_type/{id}', request_method='DELETE')
    config.add_route('edit_construction_type', '/construction_type/{id}', request_method='PUT')
    config.add_route('get_construction_type', '/construction_type/{id}', request_method='GET')
