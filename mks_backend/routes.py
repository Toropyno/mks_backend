def includeme(config):
    config.add_route('protocols', '/protocols')
    config.add_route('add_protocol', '/protocols/add')
    config.add_route('download_file', '/protocols/download/{uuid}')
    config.add_route('upload_file', '/protocols/upload')
    config.add_route('get_file_info', '/protocols/file_info')
    config.add_route('protocols_delete_change_and_view', '/protocols/{id}')
