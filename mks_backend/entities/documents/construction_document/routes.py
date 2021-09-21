def include_construction_documents(config):
    config.add_route('get_construction_documents_by_construction', 'construction/{id}/construction_documents', request_method='GET')
    config.add_route('get_construction_document', '/construction_document/{id}', request_method='GET')
    config.add_route('add_construction_document', '/construction_document', request_method='POST')
    config.add_route('edit_construction_document', '/construction_document/{id}', request_method='PUT')
    config.add_route('delete_construction_document', '/construction_document/{id}', request_method='DELETE')
