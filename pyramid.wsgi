from warnings import filterwarnings

from pyramid.paster import get_app, setup_logging

filterwarnings(action='ignore', module='requests_kerberos')

ini_path = '/home/atimchenko/MKS/backend/development.ini'
setup_logging(ini_path)
application = get_app(ini_path, 'main')
