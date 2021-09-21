def include_military_ranks(config):
    config.add_route('add_military_rank', '/military_rank', request_method='POST')
    config.add_route('get_all_military_ranks', '/military_rank', request_method='GET')
    config.add_route('get_military_rank', '/military_rank/{id}', request_method='GET')
    config.add_route('edit_military_rank', '/military_rank/{id}', request_method='PUT')
    config.add_route('delete_military_rank', '/military_rank/{id}', request_method='DELETE')
