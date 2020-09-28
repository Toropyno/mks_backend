def includeme(config):
    # protocols
    config.add_route('download_file', '/protocol/download/{uuid}', request_method='GET')
    config.add_route('upload_file', '/protocol/upload', request_method='POST')
    config.add_route('get_file_info', '/protocol/file_info', request_method='GET')

    config.add_route('get_meetings', '/meeting', request_method='GET')

    config.add_route('get_all_protocols', '/protocol', request_method='GET')
    config.add_route('add_protocol', '/protocol', request_method='POST')
    config.add_route('delete_protocol', '/protocol/{id}', request_method='DELETE')
    config.add_route('edit_protocol', '/protocol/{id}', request_method='PUT')
    config.add_route('get_protocol', '/protocol/{id}', request_method='GET')
    # ----------------------------------------------------------------------

    # ISP
    config.add_route('get_all_constructions', '/construction', request_method='GET')
    config.add_route('add_construction', '/construction', request_method='POST')
    config.add_route('delete_construction', '/construction/{id}', request_method='DELETE')
    config.add_route('edit_construction', '/construction/{id}', request_method='PUT')
    config.add_route('get_construction', '/construction/{id}', request_method='GET')

    config.add_route('get_construction_objects_by_parent', 'construction/{construction_id}/construction_objects',
                     request_method='GET')

    config.add_route('add_construction_object', '/construction_object', request_method='POST')
    config.add_route('delete_construction_object', '/construction_object/{id}', request_method='DELETE')
    config.add_route('edit_construction_object', '/construction_object/{id}', request_method='PUT')
    config.add_route('get_construction_object', '/construction_object/{id}', request_method='GET')

    config.add_route('get_all_construction_categories', '/construction_category', request_method='GET')
    config.add_route('add_construction_category', '/construction_category', request_method='POST')
    config.add_route('delete_construction_category', '/construction_category/{id}', request_method='DELETE')
    config.add_route('edit_construction_category', '/construction_category/{id}', request_method='PUT')
    config.add_route('get_construction_category', '/construction_category/{id}', request_method='GET')

    config.add_route('get_all_construction_subcategories', '/construction_subcategory', request_method='GET')
    config.add_route('add_construction_subcategory', '/construction_subcategory', request_method='POST')
    config.add_route('delete_construction_subcategory', '/construction_subcategory/{id}', request_method='DELETE')
    config.add_route('edit_construction_subcategory', '/construction_subcategory/{id}', request_method='PUT')
    config.add_route('get_construction_subcategory', '/construction_subcategory/{id}', request_method='GET')

    config.add_route('get_all_construction_stages', '/construction_stage', request_method='GET')
    config.add_route('add_construction_stage', '/construction_stage', request_method='POST')
    config.add_route('delete_construction_stage', '/construction_stage/{id}', request_method='DELETE')
    config.add_route('edit_construction_stage', '/construction_stage/{id}', request_method='PUT')
    config.add_route('get_construction_stage', '/construction_stage/{id}', request_method='GET')

    config.add_route('get_all_object_categories', '/object_category', request_method='GET')
    config.add_route('add_object_category', '/object_category', request_method='POST')
    config.add_route('delete_object_category', '/object_category/{id}', request_method='DELETE')
    config.add_route('edit_object_category', '/object_category/{id}', request_method='PUT')
    config.add_route('get_object_category', '/object_category/{id}', request_method='GET')

    config.add_route('get_all_zones', '/zone', request_method='GET')
    config.add_route('add_zone', '/zone', request_method='POST')
    config.add_route('delete_zone', '/zone/{id}', request_method='DELETE')
    config.add_route('edit_zone', '/zone/{id}', request_method='PUT')
    config.add_route('get_zone', '/zone/{id}', request_method='GET')

    config.add_route('get_all_commissions', '/commission', request_method='GET')
    config.add_route('add_commission', '/commission', request_method='POST')
    config.add_route('delete_commission', '/commission/{id}', request_method='DELETE')
    config.add_route('edit_commission', '/commission/{id}', request_method='PUT')
    config.add_route('get_commission', '/commission/{id}', request_method='GET')

    config.add_route('get_military_units', '/military_unit', request_method='GET')

    config.add_route('get_coordinates', '/coordinate', request_method='GET')

    config.add_route('get_subcategories_lists', '/subcategories_lists', request_method='GET')
    config.add_route('get_object_categories_lists', '/object_categories_list', request_method='GET')

    config.add_route('get_all_object_documents', '/object_document', request_method='GET')

    config.add_route('get_construction_documents_by_construction',
                     'construction/{id}/construction_documents',
                     request_method='GET')
    config.add_route('get_construction_documents_by_object',
                     'construction_object/{id}/construction_documents',
                     request_method='GET')
    config.add_route('get_all_construction_documents', '/construction_document', request_method='GET')
    config.add_route('get_construction_document', '/construction_document/{id}', request_method='GET')
    config.add_route('add_construction_document', '/construction_document', request_method='POST')
    config.add_route('edit_construction_document', '/construction_document/{id}', request_method='PUT')
    config.add_route('delete_construction_document', '/construction_document/{id}', request_method='DELETE')

    config.add_route('get_all_construction_progresses_by_object',
                     'construction_object/{id}/construction_progresses',
                     request_method='GET')
    config.add_route('get_last_construction_progress_by_object',
                     'construction_object/{id}/construction_progress',
                     request_method='GET')
    config.add_route('add_construction_progress', '/construction_progress', request_method='POST')
    config.add_route('get_construction_progress', '/construction_progress/{id}', request_method='GET')
    config.add_route('edit_construction_progress', '/construction_progress/{id}', request_method='PUT')
    config.add_route('delete_construction_progress', '/construction_progress/{id}', request_method='DELETE')

    config.add_route('get_all_location_types', '/location_type', request_method='GET')
    config.add_route('add_location_type', '/location_type', request_method='POST')
    config.add_route('delete_location_type', '/location_type/{id}', request_method='DELETE')
    config.add_route('edit_location_type', '/location_type/{id}', request_method='PUT')
    config.add_route('get_location_type', '/location_type/{id}', request_method='GET')

    config.add_route('get_all_construction_companies', '/company', request_method='GET')
    config.add_route('add_construction_company', '/company', request_method='POST')
    config.add_route('delete_construction_company', '/company/{id}', request_method='DELETE')
    config.add_route('edit_construction_company', '/company/{id}', request_method='PUT')
    config.add_route('get_construction_company', '/company/{id}', request_method='GET')

    config.add_route('get_all_oksms', '/oksm', request_method='GET')
    config.add_route('add_oksm', '/oksm', request_method='POST')
    config.add_route('delete_oksm', '/oksm/{id}', request_method='DELETE')
    config.add_route('edit_oksm', '/oksm/{id}', request_method='PUT')
    config.add_route('get_oksm', '/oksm/{id}', request_method='GET')

    config.add_route('get_all_construction_types', '/construction_type', request_method='GET')
    config.add_route('add_construction_type', '/construction_type', request_method='POST')
    config.add_route('delete_construction_type', '/construction_type/{id}', request_method='DELETE')
    config.add_route('edit_construction_type', '/construction_type/{id}', request_method='PUT')
    config.add_route('get_construction_type', '/construction_type/{id}', request_method='GET')

    config.add_route('get_all_doc_types', '/doc_type', request_method='GET')
    config.add_route('add_doc_type', '/doc_type', request_method='POST')
    config.add_route('delete_doc_type', '/doc_type/{id}', request_method='DELETE')
    config.add_route('edit_doc_type', '/doc_type/{id}', request_method='PUT')
    config.add_route('get_doc_type', '/doc_type/{id}', request_method='GET')

    config.add_route('get_all_realty_types', '/realty_type', request_method='GET')
    config.add_route('add_realty_type', '/realty_type', request_method='POST')
    config.add_route('delete_realty_type', '/realty_type/{id}', request_method='DELETE')
    config.add_route('edit_realty_type', '/realty_type/{id}', request_method='PUT')
    config.add_route('get_realty_type', '/realty_type/{id}', request_method='GET')

    config.add_route('get_all_work_types', '/work_type', request_method='GET')
    config.add_route('add_work_type', '/work_type', request_method='POST')
    config.add_route('delete_work_type', '/work_type/{id}', request_method='DELETE')
    config.add_route('edit_work_type', '/work_type/{id}', request_method='PUT')
    config.add_route('get_work_type', '/work_type/{id}', request_method='GET')

    config.add_route('get_all_measure_units', '/measure_unit', request_method='GET')
    config.add_route('add_measure_unit', '/measure_unit', request_method='POST')
    config.add_route('delete_measure_unit', '/measure_unit/{id}', request_method='DELETE')
    config.add_route('edit_measure_unit', '/measure_unit/{id}', request_method='PUT')
    config.add_route('get_measure_unit', '/measure_unit/{id}', request_method='GET')

    config.add_route('get_all_object_files', '/object_file', request_method='GET')
