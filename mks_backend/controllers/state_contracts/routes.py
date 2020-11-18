def include_state_contracts(config):
    config.add_route('add_contract_work_type', '/contract_work_type', request_method='POST')
    config.add_route('edit_contract_work_type', '/contract_work_type/{id}', request_method='PUT')
    config.add_route('get_all_contract_work_types', '/contract_work_type', request_method='GET')
    config.add_route('get_contract_work_type', '/contract_work_type/{id}', request_method='GET')
    config.add_route('delete_contract_work_type', '/contract_work_type/{id}', request_method='DELETE')
