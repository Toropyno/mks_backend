def include_court_decision(config):
    config.add_route('get_all_court_decisions', '/court_decision', request_method='GET')
    config.add_route('add_court_decision', '/court_decision', request_method='POST')
    config.add_route('delete_court_decision', '/court_decision/{id}', request_method='DELETE')
    config.add_route('edit_court_decision', '/court_decision/{id}', request_method='PUT')
    config.add_route('get_court_decision', '/court_decision/{id}', request_method='GET')
