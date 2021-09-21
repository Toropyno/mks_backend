def include_inspected_objects(config):
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
