def include_construction_critical_categories(config):
    config.add_route('get_all_construction_critical_categories', '/construction_critical_category', request_method='GET')
    config.add_route('add_construction_critical_category', '/construction_critical_category', request_method='POST')
    config.add_route('delete_construction_critical_category', '/construction_critical_category/{id}', request_method='DELETE')
    config.add_route('edit_construction_critical_category', '/construction_critical_category/{id}', request_method='PUT')
    config.add_route('get_construction_critical_category', '/construction_critical_category/{id}', request_method='GET')