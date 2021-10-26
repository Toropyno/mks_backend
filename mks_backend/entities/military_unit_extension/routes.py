def include_military_unit_extension(config):
    config.add_route('add_military_unit_extension', '/military_unit_extension', request_method='POST')
    config.add_route(
        'delete_military_unit_extension',
        '/military_unit_extension/{id}/date/{date}',
        request_method='DELETE'
    )
    config.add_route('edit_military_unit_extension',
                     '/military_unit_extension/{id}/date/{date}',
                     request_method='PUT'
                     )
    config.add_route('get_military_unit_extension', '/military_unit_extension/{id}/date/{date}', request_method='GET')
