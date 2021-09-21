def include_element_types(config):
    config.add_route('get_all_element_types', '/element_type', request_method='GET')
    config.add_route('add_element_type', '/element_type', request_method='POST')
    config.add_route('delete_element_type', '/element_type/{id}', request_method='DELETE')
    config.add_route('edit_element_type', '/element_type/{id}', request_method='PUT')
    config.add_route('get_element_type', '/element_type/{id}', request_method='GET')
