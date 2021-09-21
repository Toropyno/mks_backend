def include_miv(config):
    config.add_route('miv_notify', '/miv/message/notify/', request_method='POST')
    config.add_route('miv_options', '/miv/message/receive/', request_method='OPTIONS')
    config.add_route('miv_receive', '/miv/message/receive/', request_method='POST')
    config.add_route('miv_send', '/miv/message/send', request_method='POST')
