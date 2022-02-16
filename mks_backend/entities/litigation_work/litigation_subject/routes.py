def include_litigation_subjects(config):
    config.add_route(
        'get_litigation_subjects_by_litigation',
        '/litigation/{litigation_id}/litigation_subject',
        request_method='GET'
    )
    config.add_route(
        'delete_litigation_subject',
        '/litigation/{litigation_id}/litigation_subject/{construction_id}',
        request_method='DELETE'
    )
    config.add_route(
        'add_litigation_subject',
        '/litigation/{litigation_id}/litigation_subject',
        request_method='POST'
    )
