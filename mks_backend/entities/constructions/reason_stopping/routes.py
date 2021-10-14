def include_reason_stoppings(config):
    config.add_route('get_all_reason_stoppings', '/reason_stoppings', request_method='GET')
    config.add_route('add_reason_stopping', '/reason_stopping', request_method='POST')
    config.add_route('delete_reason_stopping', '/reason_stopping/{id}', request_method='DELETE')
    config.add_route('edit_reason_stopping', '/reason_stopping/{id}', request_method='PUT')
    config.add_route('get_reason_stopping', '/reason_stopping/{id}', request_method='GET')
