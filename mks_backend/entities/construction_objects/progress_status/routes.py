def include_progress_statuses(config):
    config.add_route('get_all_progress_statuses', '/progress_status', request_method='GET')
    config.add_route('add_progress_status', '/progress_status', request_method='POST')
    config.add_route('delete_progress_status', '/progress_status/{id}', request_method='DELETE')
    config.add_route('edit_progress_status', '/progress_status/{id}', request_method='PUT')
    config.add_route('get_progress_status', '/progress_status/{id}', request_method='GET')
