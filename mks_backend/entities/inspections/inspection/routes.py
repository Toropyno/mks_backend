def include_inspections(config):
    config.add_route('get_all_inspections', '/inspection', request_method='GET')
    config.add_route('add_inspection', '/inspection', request_method='POST')
    config.add_route('delete_inspection', '/inspection/{id}', request_method='DELETE')
    config.add_route('edit_inspection', '/inspection/{id}', request_method='PUT')
    config.add_route('get_inspection', '/inspection/{id}', request_method='GET')
