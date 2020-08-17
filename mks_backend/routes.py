def includeme(config):
    config.add_route('protocols', '/protocols')
    config.add_route('add_protocol', '/protocols/add')
    config.add_route('download_file', '/protocols/download/{uuid}')
    config.add_route('upload_file', '/protocols/upload')
    config.add_route('protocols_delete_change_and_view', '/protocols/{id}')

    config.add_route('constructions', '/constructions')
    config.add_route('add_construction', '/constructions/add')
    config.add_route('construction_delete_change_and_view', '/constructions/{id}')

    config.add_route('construction_objects', 'construction/construction_objects/{constructionId}')

    config.add_route('add_construction_object', '/construction_objects/add')
    config.add_route('construction_objects_delete_change_and_view', '/construction_objects/{id}')

    config.add_route('construction_categories', '/construction_categories')
    config.add_route('add_construction_category', '/construction_categories/add')
    config.add_route('construction_category_delete_change_and_view', '/construction_categories/{id}')

    config.add_route('subcategories_lists', '/subcategories_lists')
    config.add_route('add_subcategories_list', '/subcategories_lists/add')
    config.add_route('subcategories_list_delete_and_view', '/subcategories_lists/{id}')

    config.add_route('construction_subcategories', '/construction_subcategories')
    config.add_route('add_construction_subcategory', '/construction_subcategories/add')
    config.add_route('construction_subcategory_delete_change_and_view', '/construction_subcategories/{id}')

    config.add_route('construction_stages', '/construction_stages')
    config.add_route('add_construction_stage', '/construction_stages/add')
    config.add_route('construction_stages_delete_change_and_view', '/construction_stages/{id}')

    config.add_route('object_categories', '/object_categories')
    config.add_route('add_object_category', '/object_categories/{id}')
    config.add_route('object_category_delete_change_and_view', '/object_categories/{id}')

    config.add_route('object_categories_lists', '/object_categories_list')
    config.add_route('add_object_categories_list', '/object_categories_list/add')
    config.add_route('object_categories_list_delete_change_and_view', '/object_categories_list/{id}')

    config.add_route('zones', '/zones')
    config.add_route('add_zone', '/zones/add')
    config.add_route('zone_delete_change_and_view', '/zones/{id}')

    config.add_route('commissions', '/commissions')
    config.add_route('add_commission', '/commissions/add')
    config.add_route('commission_delete_change_and_view', '/commissions/{id}')
