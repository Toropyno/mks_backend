def include_leadership_positions(config):
    config.add_route('get_all_leadership_positions', '/leadership_position', request_method='GET')
    config.add_route('add_leadership_position', '/leadership_position', request_method='POST')
    config.add_route('delete_leadership_position', '/leadership_position/{id}', request_method='DELETE')
    config.add_route('edit_leadership_position', '/leadership_position/{id}', request_method='PUT')
    config.add_route('get_leadership_position', '/leadership_position/{id}', request_method='GET')
