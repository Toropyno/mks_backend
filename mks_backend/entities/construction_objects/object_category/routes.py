def include_object_category(config):
    config.add_route('get_all_object_categories', '/object_category', request_method='GET')
    config.add_route('add_object_category', '/object_category', request_method='POST')
    config.add_route('delete_object_category', '/object_category/{id}', request_method='DELETE')
    config.add_route('edit_object_category', '/object_category/{id}', request_method='PUT')
    config.add_route('get_object_category', '/object_category/{id}', request_method='GET')
