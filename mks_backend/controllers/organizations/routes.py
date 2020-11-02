def include_organizations(config):
    config.add_route('get_organizations_tree', '/organization', request_method='GET')
    config.add_route('delete_organization', '/organization/{organization_uuid}', request_method='DELETE')
