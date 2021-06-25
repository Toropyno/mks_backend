import logging
from time import sleep

import requests

logging.basicConfig(level=logging.INFO)


def try_again(code):
    def wrap(func):
        def wrapped_f(*args, **kwargs):
            msg = kwargs.get('msg', func.__name__)
            for attempt in range(5):
                try:
                    response = func(*args, **kwargs)
                except requests.exceptions.Timeout:
                    continue
                if response.status_code != code:
                    sleep(1)
                    logging.warning('Try #{}: Failed to {}'.format(attempt, msg))
                else:
                    logging.info('Succeed to {}'.format(msg))
                    return response
            logging.error('Aborting!')
            exit(1)
        return wrapped_f

    return wrap
