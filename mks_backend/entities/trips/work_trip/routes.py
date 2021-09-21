def include_work_trips(config):
    config.add_route('get_all_work_trips', '/work_trip', request_method='GET')
    config.add_route('add_work_trip', '/work_trip', request_method='POST')
    config.add_route('delete_work_trip', '/work_trip/{id}', request_method='DELETE')
    config.add_route('edit_work_trip', '/work_trip/{id}', request_method='PUT')
    config.add_route('get_work_trip', '/work_trip/{id}', request_method='GET')
