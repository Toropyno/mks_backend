def include_officials(config):
    config.add_route('add_official', '/official', request_method='POST')
    config.add_route('edit_official', '/official/{id}', request_method='PUT')
    config.add_route('delete_official', '/official/{id}', request_method='DELETE')
    config.add_route('get_official_by_id', '/official/{id}', request_method='GET')
    config.add_route(
        'get_officials_by_organization',
        '/organization/{organization_uuid}/official',
        request_method='GET',
    )
