def include_litigation_documents(config):
    config.add_route(
        'get_litigation_documents_by_litigation', 'litigation/{id}/litigation_documents', request_method='GET'
    )
    config.add_route('get_litigation_document', '/litigation_document/{id}', request_method='GET')
    config.add_route('add_litigation_document', '/litigation_document', request_method='POST')
    config.add_route('edit_litigation_document', '/litigation_document/{id}', request_method='PUT')
    config.add_route('delete_litigation_document', '/litigation_document/{id}', request_method='DELETE')
