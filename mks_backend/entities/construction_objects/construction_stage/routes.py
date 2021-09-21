def include_construction_stages(config):
    config.add_route('get_all_construction_stages', '/construction_stage', request_method='GET')
    config.add_route('add_construction_stage', '/construction_stage', request_method='POST')
    config.add_route('delete_construction_stage', '/construction_stage/{id}', request_method='DELETE')
    config.add_route('edit_construction_stage', '/construction_stage/{id}', request_method='PUT')
    config.add_route('get_construction_stage', '/construction_stage/{id}', request_method='GET')
