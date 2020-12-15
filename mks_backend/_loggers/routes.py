def include_logs(config):
    config.add_route('get_db_errors', '/db_error', request_method='GET')
