def include_construction_objects(config):
    config.add_route(
        'get_construction_objects_by_parent',
        'construction/{construction_id}/construction_objects',
        request_method='GET'
    )

    config.add_route('add_construction_object', '/construction_object', request_method='POST')
    config.add_route('delete_construction_object', '/construction_object/{id}', request_method='DELETE')
    config.add_route('edit_construction_object', '/construction_object/{id}', request_method='PUT')
    config.add_route('get_construction_object', '/construction_object/{id}', request_method='GET')
