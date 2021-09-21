def include_object_files(config):
    config.add_route('get_all_object_files', '/object_file', request_method='GET')
    config.add_route('add_object_file', '/object_file', request_method='POST')
    config.add_route('delete_object_file', '/object_file/{id}', request_method='DELETE')
    config.add_route('edit_object_file', '/object_file/{id}', request_method='PUT')
    config.add_route('get_object_file', '/object_file/{id}', request_method='GET')
    config.add_route('get_object_files_by_object', 'construction_object/{id}/object_files', request_method='GET')
