def include_contract_statuses(config):
    config.add_route('get_all_contract_statuses', '/contract_status', request_method='GET')
    config.add_route('add_contract_status', '/contract_status', request_method='POST')
    config.add_route('delete_contract_status', '/contract_status/{id}', request_method='DELETE')
    config.add_route('edit_contract_status', '/contract_status/{id}', request_method='PUT')
    config.add_route('get_contract_status', '/contract_status/{id}', request_method='GET')
