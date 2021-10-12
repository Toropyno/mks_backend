def include_critical_categories(config):
    config.add_route('get_all_critical_categories',
                     '/critical_category', request_method='GET')
    config.add_route('add_critical_category', '/critical_category', request_method='POST')
    config.add_route('delete_critical_category',
                     '/critical_category/{id}', request_method='DELETE')
    config.add_route('edit_critical_category',
                     '/critical_category/{id}', request_method='PUT')
    config.add_route('get_critical_category', '/critical_category/{id}', request_method='GET')
