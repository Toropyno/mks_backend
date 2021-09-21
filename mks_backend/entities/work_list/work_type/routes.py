def include_work_types(config):
    config.add_route('get_all_work_types', '/work_type', request_method='GET')
    config.add_route('add_work_type', '/work_type', request_method='POST')
    config.add_route('delete_work_type', '/work_type/{id}', request_method='DELETE')
    config.add_route('edit_work_type', '/work_type/{id}', request_method='PUT')
    config.add_route('get_work_type', '/work_type/{id}', request_method='GET')
