def include_filestorage(config):
    config.add_route('download_file', '/file/{uuid}', request_method='GET')
    config.add_route('upload_file', '/file', request_method='POST')
    config.add_route('get_file_info', '/protocol/file_info', request_method='GET')

    config.add_route('get_filestorages_by_object',
                     'construction_object/{id}/filestorages',
                     request_method='GET')
    config.add_route('delete_file', '/file/{uuid}', request_method='DELETE')
