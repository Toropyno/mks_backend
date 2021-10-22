def include_work_trip_files(config):
    config.add_route('get_all_work_trip_files_by_work_trip_id', '/work_trip/{id}/file', request_method='GET')
    config.add_route('add_work_trip_files', '/work_trip_file', request_method='POST')
    config.add_route('delete_work_trip_file', '/work_trip_file/{id}', request_method='DELETE')
