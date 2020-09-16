def includeme(config):
    # protocols
    config.add_route('download_file', '/protocol/download/{uuid}', request_method='GET')
    config.add_route('upload_file', '/protocol/upload', request_method='POST')
    config.add_route('get_file_info', '/protocol/file_info', request_method='GET')

    config.add_route('get_meetings', '/meeting', request_method='GET')

    config.add_route('get_protocols', '/protocol', request_method='GET')
    config.add_route('add_protocol', '/protocol', request_method='POST')
    config.add_route('delete_protocol', '/protocol/{id}', request_method='DELETE')
    config.add_route('edit_protocol', '/protocol/{id}', request_method='PUT')
    config.add_route('get_protocol', '/protocol/{id}', request_method='GET')
    # ----------------------------------------------------------------------

    # ISP
    config.add_route('get_constructions', '/construction', request_method='GET')
    config.add_route('add_construction', '/construction', request_method='POST')
    config.add_route('delete_construction', '/construction/{id}', request_method='DELETE')
    config.add_route('edit_construction', '/construction/{id}', request_method='PUT')
    config.add_route('get_construction', '/construction/{id}', request_method='GET')

    config.add_route('get_construction_objects_by_parent', 'construction/construction_objects/{construction_id}',
                     request_method='GET')

    config.add_route('add_construction_object', '/construction_object', request_method='POST')
    config.add_route('delete_construction_object', '/construction_object/{id}', request_method='DELETE')
    config.add_route('edit_construction_object', '/construction_object/{id}', request_method='PUT')
    config.add_route('get_construction_object', '/construction_object/{id}', request_method='GET')

    config.add_route('get_construction_categories', '/construction_category', request_method='GET')
    config.add_route('add_construction_category', '/construction_category', request_method='POST')
    config.add_route('delete_construction_category', '/construction_category/{id}', request_method='DELETE')
    config.add_route('edit_construction_category', '/construction_category/{id}', request_method='PUT')
    config.add_route('get_construction_category', '/construction_category/{id}', request_method='GET')

    config.add_route('get_construction_subcategories', '/construction_subcategory', request_method='GET')
    config.add_route('add_construction_subcategory', '/construction_subcategory', request_method='POST')
    config.add_route('delete_construction_subcategory', '/construction_category/{id}', request_method='DELETE')
    config.add_route('edit_construction_subcategory', '/construction_category/{id}', request_method='PUT')
    config.add_route('get_construction_subcategory', '/construction_category/{id}', request_method='GET')

    config.add_route('get_construction_stages', '/construction_stage', request_method='GET')
    config.add_route('add_construction_stage', '/construction_stage', request_method='POST')
    config.add_route('delete_construction_stage', '/construction_stage/{id}', request_method='DELETE')
    config.add_route('edit_construction_stage', '/construction_stage/{id}', request_method='PUT')
    config.add_route('get_construction_stage', '/construction_stage/{id}', request_method='GET')

    config.add_route('get_object_categories', '/object_category', request_method='GET')
    config.add_route('add_object_category', '/object_category', request_method='POST')
    config.add_route('delete_object_category', '/object_category/{id}', request_method='DELETE')
    config.add_route('edit_object_category', '/object_category/{id}', request_method='PUT')
    config.add_route('get_object_category', '/object_category/{id}', request_method='GET')

    config.add_route('get_zones', '/zone', request_method='GET')
    config.add_route('add_zone', '/zone', request_method='POST')
    config.add_route('delete_zone', '/zone/{id}', request_method='DELETE')
    config.add_route('edit_zone', '/zone/{id}', request_method='PUT')
    config.add_route('get_zone', '/zone/{id}', request_method='GET')

    config.add_route('get_commissions', '/commission', request_method='GET')
    config.add_route('add_commission', '/commission', request_method='POST')
    config.add_route('delete_commission', '/commission/{id}', request_method='DELETE')
    config.add_route('edit_commission', '/commission/{id}', request_method='PUT')
    config.add_route('get_commission', '/commission/{id}', request_method='GET')

    config.add_route('get_military_units', '/military_unit', request_method='GET')

    config.add_route('get_locations', '/location', request_method='GET')

    config.add_route('get_subcategories_lists', '/subcategories_lists', request_method='GET')
    config.add_route('get_object_categories_lists', '/object_categories_list', request_method='GET')
