def include_object_documents(config):
    config.add_route('get_construction_documents_by_object', 'construction_object/{id}/document', request_method='GET')
    config.add_route('edit_construction_document_and_object_relations', 'construction_object/{id}/document', request_method='PUT')
