def include_construction_companies(config):
    config.add_route('get_all_construction_companies', '/company', request_method='GET')
    config.add_route('add_construction_company', '/company', request_method='POST')
    config.add_route('delete_construction_company', '/company/{id}', request_method='DELETE')
    config.add_route('edit_construction_company', '/company/{id}', request_method='PUT')
    config.add_route('get_construction_company', '/company/{id}', request_method='GET')
