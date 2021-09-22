def include_reference_histories(config):
    config.add_route(
        'get_reference_history_by_object', '/construction_object/{id}/reference-history',
        request_method='GET'
    )
