def include_fias(config):
    config.add_route('get_all_fiases_for_filtration', '/fias-filter', request_method='GET')
