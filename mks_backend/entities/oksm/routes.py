def include_oksms(config):
    config.add_route('get_all_oksms', '/oksm', request_method='GET')
    config.add_route('add_oksm', '/oksm', request_method='POST')
    config.add_route('delete_oksm', '/oksm/{id}', request_method='DELETE')
    config.add_route('edit_oksm', '/oksm/{id}', request_method='PUT')
    config.add_route('get_oksm', '/oksm/{id}', request_method='GET')
