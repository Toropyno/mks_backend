def include_subcategories_lists(config):
    config.add_route('get_subcategories_lists', '/subcategories_lists', request_method='GET')
