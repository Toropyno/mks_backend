def include_measure_unit(config):
    config.add_route('get_all_measure_units', '/measure_unit', request_method='GET')
    config.add_route('add_measure_unit', '/measure_unit', request_method='POST')
    config.add_route('delete_measure_unit', '/measure_unit/{id}', request_method='DELETE')
    config.add_route('edit_measure_unit', '/measure_unit/{id}', request_method='PUT')
    config.add_route('get_measure_unit', '/measure_unit/{id}', request_method='GET')
