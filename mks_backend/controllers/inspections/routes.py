def include_inspections(config):
    config.add_route('get_all_inspections', '/inspection', request_method='GET')
    config.add_route('add_inspection', '/inspection', request_method='POST')
    config.add_route('delete_inspection', '/inspection/{id}', request_method='DELETE')
    config.add_route('edit_inspection', '/inspection/{id}', request_method='PUT')
    config.add_route('get_inspection', '/inspection/{id}', request_method='GET')

    config.add_route(
        'get_inspected_objects_by_inspection',
        '/inspection/{inspection_id}/inspected_object',
        request_method='GET'
    )
    config.add_route(
        'delete_inspected_object',
        '/inspection/{inspection_id}/inspected_object/{construction_id}',
        request_method='DELETE'
    )
    config.add_route(
        'add_inspected_object',
        '/inspection/{inspection_id}/inspected_object',
        request_method='POST'
    )

    config.add_route('get_files_by_inspection', '/inspection/{inspection_id}/file', request_method='GET')
    config.add_route('add_inspection_file', '/inspection/{inspection_id}/file', request_method='POST')
    config.add_route('delete_inspection_file', '/inspection/{inspection_id}/file/{file_id}', request_method='DELETE')
