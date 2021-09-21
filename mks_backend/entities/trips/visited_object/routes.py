def include_visited_objects(config):
    config.add_route('get_visited_objects_by_work_trip', '/work_trip/{work_trip_id}/visited_object',
                     request_method='GET')
    config.add_route('add_visited_object', '/work_trip/{work_trip_id}/visited_object', request_method='POST')
    config.add_route('delete_visited_object', '/work_trip/{work_trip_id}/visited_object/{construction_id}',
                     request_method='DELETE')
