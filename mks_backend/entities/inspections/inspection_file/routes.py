def include_inspection_files(config):
    config.add_route('get_files_by_inspection', '/inspection/{inspection_id}/file', request_method='GET')
    config.add_route('add_inspection_file', '/inspection/{inspection_id}/file', request_method='POST')
    config.add_route('delete_inspection_file', '/inspection/{inspection_id}/file/{file_id}', request_method='DELETE')
