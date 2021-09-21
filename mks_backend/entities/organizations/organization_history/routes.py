def include_organization_history(config):
    config.add_route('add_organization_history', '/organization-history', request_method='POST')
    config.add_route('update_organization_history', '/organization-history/{history_id}', request_method='PUT')
    config.add_route('delete_organization_history', '/organization-history/{history_id}', request_method='DELETE')
    config.add_route(
        'get_organization_history_by_organization',
        '/organization/{organization_uuid}/organization-history',
        request_method='GET',
    )
