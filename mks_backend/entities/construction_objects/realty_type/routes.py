def include_realty_types(config):
    config.add_route('get_all_realty_types', '/realty_type', request_method='GET')
    config.add_route('add_realty_type', '/realty_type', request_method='POST')
    config.add_route('delete_realty_type', '/realty_type/{id}', request_method='DELETE')
    config.add_route('edit_realty_type', '/realty_type/{id}', request_method='PUT')
    config.add_route('get_realty_type', '/realty_type/{id}', request_method='GET')
