def include_construction_subcategories(config):
    config.add_route('get_all_construction_subcategories', '/construction_subcategory', request_method='GET')
    config.add_route('add_construction_subcategory', '/construction_subcategory', request_method='POST')
    config.add_route('delete_construction_subcategory', '/construction_subcategory/{id}', request_method='DELETE')
    config.add_route('edit_construction_subcategory', '/construction_subcategory/{id}', request_method='PUT')
    config.add_route('get_construction_subcategory', '/construction_subcategory/{id}', request_method='GET')
