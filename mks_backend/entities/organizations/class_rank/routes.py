def include_class_rank(config):
    config.add_route('get_all_class_ranks', '/class-rank', request_method='GET')
    config.add_route('add_class_rank', '/class-rank', request_method='POST')
    config.add_route('get_class_rank', '/class-rank/{id}', request_method='GET')
    config.add_route('update_class_rank', '/class-rank/{id}', request_method='PUT')
    config.add_route('delete_class_rank', '/class-rank/{id}', request_method='DELETE')
