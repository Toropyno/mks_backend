def include_participant_statuses(config):
    config.add_route('get_all_participant_statuses', '/participant_status', request_method='GET')
    config.add_route('add_participant_status', '/participant_status', request_method='POST')
    config.add_route('delete_participant_status', '/participant_status/{id}', request_method='DELETE')
    config.add_route('edit_participant_status', '/participant_status/{id}', request_method='PUT')
    config.add_route('get_participant_status', '/participant_status/{id}', request_method='GET')
