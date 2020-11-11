def include_organizations(config):
    config.add_route('get_organizations_tree', '/organization', request_method='GET')
    config.add_route('add_organization', '/organization', request_method='POST'),
    config.add_route('move_organization', '/organization', request_method='PATCH'),
    config.add_route('delete_organization', '/organization/{organization_uuid}', request_method='DELETE')

    config.add_route('add_organization_history', '/organization-history', request_method='POST'),
    config.add_route('delete_organization_history', '/organization-history/{history_id}', request_method='DELETE')
    config.add_route('update_organization_history', '/organization-history/{history_id}', request_method='PUT'),
