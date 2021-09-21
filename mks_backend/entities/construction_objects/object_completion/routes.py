def include_object_completion(config):
    config.add_route('get_object_completion_by_object', '/construction_object/{id}/completion', request_method='GET')
