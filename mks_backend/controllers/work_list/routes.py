def include_work_list(config):
    config.add_route('add_work_list', '/work_list', request_method='POST')
    config.add_route('delete_work_list', '/work_list/{id}', request_method='DELETE')
    config.add_route('edit_work_list', '/work_list/{id}', request_method='PUT')
    config.add_route('get_work_list', '/work_list/{id}', request_method='GET')

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

    config.add_route('get_all_element_types', '/element_type', request_method='GET')
    config.add_route('add_element_type', '/element_type', request_method='POST')
    config.add_route('delete_element_type', '/element_type/{id}', request_method='DELETE')
    config.add_route('edit_element_type', '/element_type/{id}', request_method='PUT')
    config.add_route('get_element_type', '/element_type/{id}', request_method='GET')
