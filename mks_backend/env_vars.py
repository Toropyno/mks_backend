from os import environ


def setup_env_vars():
    # ------ Filestorage ---------
    environ['FILE_STORAGE'] = '/home/atimchenko/MKS/filestorage/'
    environ['ALLOWED_EXTENSIONS'] = ', '.join([
        'doc', 'docx', 'docm', 'pdf', 'odt', 'ppt', 'odp'
        'txt', 'jpg', 'png', 'mp4', 'avi', 'mkv'
    ])

    # ------------ MIV ------------
    environ['MIV_USER'] = ''
    environ['MIV_USER_PASSWORD'] = ''
    environ['MIV_REGISTER_URL'] = 'http://1krn-balancer01.int.aorti.tech:8860/public/api/1.0/account_endpoint/'
    environ['MIV_SEND_URL'] = 'http://1krn-balancer01.int.aorti.tech:8860/public/api/1.0/message/receive/'
    environ['MIV_WHOAMI_URL'] = 'http://1krn-balancer01.int.aorti.tech:8860/public/api/1.0/whoami/'
    environ['MIV_FILESTORAGE_PATH'] = '/home/atimchenko/MKS/miv_data'
    environ['MIV_JSON_PATH'] = '/home/atimchenko/MKS/miv_data/json'

    # ------------ FIASService ------------
    environ['FIAS_URL'] = 'http://172.23.137.67/fiasapi'
    environ['FIAS_USER'] = 'user'
    environ['FIAS_PASSWORD'] = '11111111'
    # -----------------------------

    # ------------ REALM and AUTH ------------
    environ['KRB_AUTH_REALM'] = 'INT.AORTI.TECH'
    environ['AUTH_TYPE'] = 'kerberos'

    # ------------ SVIP ------------
    environ['SVIP_HOST'] = 'http://1adr-book02.int.aorti.tech:8820/public/api/'
    environ['SVIP_USER'] = 'mks'
    environ['SVIP_PASSWORD'] = 'iEfG02AE'
