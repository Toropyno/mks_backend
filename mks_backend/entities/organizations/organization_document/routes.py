def include_organization_document(config):
    config.add_route('add_organization_document', '/organization_document', request_method='POST')
    config.add_route('edit_organization_document', '/organization_document/{id}', request_method='PUT')
    config.add_route('delete_organization_document', '/organization_document/{id}', request_method='DELETE')
    config.add_route('get_document_by_organization', '/organization_document/{id}', request_method='GET')
    config.add_route(
        'get_documents_by_organization',
        '/organization/{organization_uuid}/organization_document',
        request_method='GET',
    )
