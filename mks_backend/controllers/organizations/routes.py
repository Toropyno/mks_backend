def include_organizations(config):
    config.add_route('get_organizations_tree', '/organization', request_method='GET')
    config.add_route('add_organization', '/organization', request_method='POST')
    config.add_route('move_organization', '/organization', request_method='PATCH')
    config.add_route('delete_organization', '/organization/{organization_uuid}', request_method='DELETE')

    config.add_route('add_organization_history', '/organization-history', request_method='POST')
    config.add_route('update_organization_history', '/organization-history/{history_id}', request_method='PUT')
    config.add_route('delete_organization_history', '/organization-history/{history_id}', request_method='DELETE')
    config.add_route(
        'get_organization_history_by_organization',
        '/organization/{organization_uuid}/organization-history',
        request_method='GET',
    )

    config.add_route('add_organization_document', '/organization_document', request_method='POST')
    config.add_route('edit_organization_document', '/organization_document/{id}', request_method='PUT')
    config.add_route('delete_organization_document', '/organization_document/{id}', request_method='DELETE')
    config.add_route(
        'get_documents_by_organization',
        '/organization/{organization_uuid}/organization_document',
        request_method='GET',
    )

    config.add_route('add_official', '/official', request_method='POST')
    config.add_route('edit_official', '/official/{id}', request_method='PUT')
    config.add_route('delete_official', '/official/{id}', request_method='DELETE')
    config.add_route(
        'get_officials_by_organization',
        '/organization/{organization_uuid}/official',
        request_method='GET',
    )
