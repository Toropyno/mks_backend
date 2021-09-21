def include_doc_types(config):
    config.add_route('get_all_doc_types', '/doc_type', request_method='GET')
    config.add_route('add_doc_type', '/doc_type', request_method='POST')
    config.add_route('delete_doc_type', '/doc_type/{id}', request_method='DELETE')
    config.add_route('edit_doc_type', '/doc_type/{id}', request_method='PUT')
    config.add_route('get_doc_type', '/doc_type/{id}', request_method='GET')
