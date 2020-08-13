def includeme(config):
    config.add_route('protocols', '/protocols')
    config.add_route('add_protocol', '/protocols/add')
    config.add_route('download_file', '/protocols/download/{uuid}')
    config.add_route('upload_file', '/protocols/upload')
    config.add_route('protocols_delete_change_and_view', '/protocols/{id}')

    config.add_route('subcategories_lists', '/subcategories_lists')
    config.add_route('add_subcategories_list', '/subcategories_lists/add')
    config.add_route('subcategories_list_delete_change_and_view', '/subcategories_lists/{id}')
