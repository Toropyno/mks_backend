def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('protocols', '/protocols')
    config.add_route('add_protocol', '/protocols/add')
