from pyramid.paster import get_app, setup_logging

from mks_backend.env_vars import setup_env_vars


ini_path = '/home/atimchenko/MKS/backend/development.ini'
setup_logging(ini_path)
setup_env_vars()
application = get_app(ini_path, 'main')
