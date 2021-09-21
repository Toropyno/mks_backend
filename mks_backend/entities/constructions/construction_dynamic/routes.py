def include_construction_dynamic(config):
    config.add_route('get_dynamics_by_construction', '/construction/{construction_id}/dynamic', request_method='GET')
    config.add_route('add_construction_dynamic', '/dynamic', request_method='POST')
    config.add_route('get_construction_dynamic', '/dynamic/{id}', request_method='GET')
    config.add_route('edit_construction_dynamic', '/dynamic/{id}', request_method='PUT')
    config.add_route('delete_construction_dynamic', '/dynamic/{id}', request_method='DELETE')
