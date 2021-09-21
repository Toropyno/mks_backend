def include_military_units(config):
    config.add_route('get_military_units', '/military_unit', request_method='GET')
