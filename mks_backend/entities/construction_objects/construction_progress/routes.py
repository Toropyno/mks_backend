def include_construction_progress(config):
    config.add_route('get_all_construction_progresses_by_object',
                     'construction_object/{id}/construction_progresses',
                     request_method='GET')
    config.add_route('get_last_construction_progress_by_object',
                     'construction_object/{id}/construction_progress',
                     request_method='GET')
    config.add_route('add_construction_progress', '/construction_progress', request_method='POST')
    config.add_route('get_construction_progress', '/construction_progress/{id}', request_method='GET')
    config.add_route('edit_construction_progress', '/construction_progress/{id}', request_method='PUT')
    config.add_route('delete_construction_progress', '/construction_progress/{id}', request_method='DELETE')
