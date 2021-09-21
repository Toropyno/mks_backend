def include_meeting_types(config):
    config.add_route('get_all_meeting_types', '/meeting_type', request_method='GET')
    config.add_route('add_meeting_type', '/meeting_type', request_method='POST')
    config.add_route('delete_meeting_type', '/meeting_type/{id}', request_method='DELETE')
    config.add_route('edit_meeting_type', '/meeting_type/{id}', request_method='PUT')
    config.add_route('get_meeting_type', '/meeting_type/{id}', request_method='GET')
