from os import environ, path

from dotenv import load_dotenv


PROJECT_DIRECTORY = path.dirname(path.dirname(path.abspath(__file__)))
BASE_DIRECTORY = path.join(PROJECT_DIRECTORY, 'mks_backend')
load_dotenv(path.join(BASE_DIRECTORY, '.env'))

# ------ Filestorage ---------
FILE_STORAGE = environ['FILE_STORAGE']
ALLOWED_EXTENSIONS = environ['ALLOWED_EXTENSIONS']

# ------------ MIV ------------
MIV_USER = environ['MIV_USER']
MIV_USER_PASSWORD = environ['MIV_USER_PASSWORD']
MIV_REGISTER_URL = environ['MIV_REGISTER_URL']
MIV_SEND_URL = environ['MIV_SEND_URL']
MIV_WHOAMI_URL = environ['MIV_WHOAMI_URL']
MIV_FILESTORAGE_PATH = environ['MIV_FILESTORAGE_PATH']
MIV_JSON_PATH = environ['MIV_JSON_PATH']

# ------------ FIASService ------------
FIAS_URL = environ['FIAS_URL']
FIAS_USER = environ['FIAS_USER']
FIAS_PASSWORD = environ['FIAS_PASSWORD']
# -----------------------------

# ------------ REALM and AUTH ------------
KRB_AUTH_REALM = environ['KRB_AUTH_REALM']
AUTH_TYPE = environ['AUTH_TYPE']

# ------------ SVIP ------------
SVIP_HOST = environ['SVIP_HOST']
MKS_USER = environ['MKS_USER']
MKS_PASSWORD = environ['MKS_PASSWORD']
