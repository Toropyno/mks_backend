from warnings import filterwarnings

from pyramid.paster import get_app

filterwarnings(action='ignore', module='requests_kerberos')

ini_path = '/opt/mks/backend/development.ini'
application = get_app(ini_path, 'main')
