def include_construction_categories(config):
    config.add_route('get_all_construction_categories', '/construction_category', request_method='GET')
    config.add_route('add_construction_category', '/construction_category', request_method='POST')
    config.add_route('delete_construction_category', '/construction_category/{id}', request_method='DELETE')
    config.add_route('edit_construction_category', '/construction_category/{id}', request_method='PUT')
    config.add_route('get_construction_category', '/construction_category/{id}', request_method='GET')
