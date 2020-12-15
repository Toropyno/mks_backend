def include_trips(config):
    config.add_route('get_all_leadership_positions', '/leadership_position', request_method='GET')
    config.add_route('add_leadership_position', '/leadership_position', request_method='POST')
    config.add_route('delete_leadership_position', '/leadership_position/{id}', request_method='DELETE')
    config.add_route('edit_leadership_position', '/leadership_position/{id}', request_method='PUT')
    config.add_route('get_leadership_position', '/leadership_position/{id}', request_method='GET')

    config.add_route('get_visited_objects_by_work_trip', '/work_trip/{work_trip_id}/visited_object',
                     request_method='GET')
    config.add_route('add_visited_object', '/work_trip/{work_trip_id}/visited_object', request_method='POST')
    config.add_route('delete_visited_object', '/work_trip/{work_trip_id}/visited_object/{construction_id}',
                     request_method='DELETE')

    config.add_route('get_all_work_trips', '/work_trip', request_method='GET')
    config.add_route('add_work_trip', '/work_trip', request_method='POST')
    config.add_route('delete_work_trip', '/work_trip/{id}', request_method='DELETE')
    config.add_route('edit_work_trip', '/work_trip/{id}', request_method='PUT')
    config.add_route('get_work_trip', '/work_trip/{id}', request_method='GET')
