from os import environ

from pyramid.paster import get_app, setup_logging

# ------------ MIV ------------
environ['MIV_USER'] = ''
environ['MIV_USER_PASSWORD'] = ''
environ['MIV_REGISTER_URL'] = 'http://1krn-balancer01.int.aorti.tech:8860/public/api/1.0/account_endpoint/'
environ['MIV_SEND_URL'] = 'http://1krn-balancer01.int.aorti.tech:8860/public/api/1.0/message/receive/'
environ['MIV_WHOAMI_URL'] = 'http://1krn-balancer01.int.aorti.tech:8860/public/api/1.0/whoami/'
environ['MIV_FILESTORAGE_PATH'] = '/home/atimchenko/MKS/miv_data'
environ['MIV_JSON_PATH'] = '/home/atimchenko/MKS/miv_data/json'
# -----------------------------

ini_path = '/home/atimchenko/MKS/backend/development.ini'
setup_logging(ini_path)
application = get_app(ini_path, 'main')
