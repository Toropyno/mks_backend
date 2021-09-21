def include_commissions(config):
    config.add_route('get_all_commissions', '/commission', request_method='GET')
    config.add_route('add_commission', '/commission', request_method='POST')
    config.add_route('delete_commission', '/commission/{id}', request_method='DELETE')
    config.add_route('edit_commission', '/commission/{id}', request_method='PUT')
    config.add_route('get_commission', '/commission/{id}', request_method='GET')
