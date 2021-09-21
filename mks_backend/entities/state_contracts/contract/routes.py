def include_contracts(config):
    config.add_route(
        'get_all_contracts_by_construction_id',
        '/construction/{construction_id}/contract',
        request_method='GET'
    )
    config.add_route('add_contract', '/contract', request_method='POST')
    config.add_route('delete_contract', '/contract/{id}', request_method='DELETE')
    config.add_route('edit_contract', '/contract/{id}', request_method='PUT')
    config.add_route('get_contract', '/contract/{id}', request_method='GET')
