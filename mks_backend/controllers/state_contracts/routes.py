def include_state_contracts(config):
    config.add_route('add_contract_work_type', '/contract_work_type', request_method='POST')
    config.add_route('edit_contract_work_type', '/contract_work_type/{id}', request_method='PUT')
    config.add_route('get_all_contract_work_types', '/contract_work_type', request_method='GET')
    config.add_route('get_contract_work_type', '/contract_work_type/{id}', request_method='GET')
    config.add_route('delete_contract_work_type', '/contract_work_type/{id}', request_method='DELETE')

    config.add_route(
        'get_all_contracts_by_construction_id',
        '/construction/{construction_id}/contract',
        request_method='GET'
    )
    config.add_route('add_contract', '/contract', request_method='POST')
    config.add_route('delete_contract', '/contract/{id}', request_method='DELETE')
    config.add_route('edit_contract', '/contract/{id}', request_method='PUT')
    config.add_route('get_contract', '/contract/{id}', request_method='GET')

    config.add_route('get_all_contract_statuses', '/contract_status', request_method='GET')
    config.add_route('add_contract_status', '/contract_status', request_method='POST')
    config.add_route('delete_contract_status', '/contract_status/{id}', request_method='DELETE')
    config.add_route('edit_contract_status', '/contract_status/{id}', request_method='PUT')
    config.add_route('get_contract_status', '/contract_status/{id}', request_method='GET')
