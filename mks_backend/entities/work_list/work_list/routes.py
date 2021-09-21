def include_work_list(config):
    config.add_route('add_work_list', '/work_list', request_method='POST')
    config.add_route('delete_work_list', '/work_list/{id}', request_method='DELETE')
    config.add_route('edit_work_list', '/work_list/{id}', request_method='PUT')
    config.add_route('get_work_list', '/work_list/{id}', request_method='GET')

    config.add_route(
        'get_work_list_for_construction_object',
        '/construction_object/{id}/work_list',
        request_method='GET'
    )
