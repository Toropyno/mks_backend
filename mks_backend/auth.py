import logging
import requests
from os import environ
from subprocess import Popen, PIPE

from requests_kerberos import HTTPKerberosAuth


logging.basicConfig(level=logging.INFO)


class Authorization:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.auth = self._auth

    @property
    def login_with_realm(self):
        return self.username + '@' + environ['KRB_AUTH_REALM']

    @property
    def _auth(self):
        auth_type = environ['AUTH_TYPE']
        if auth_type == 'kerberos':
            # TODO: Слишком частое создание тикета
            self.create_ticket()
            auth = HTTPKerberosAuth(principal=self.login_with_realm)
            return auth
        elif auth_type == 'explicit':
            return ExplicitAuth(self.login_with_realm)

    def check_ticket(self):
        # TODO: Можно сделать умнее
        whoami = requests.get(environ['MIV_WHOAMI_URL'], auth=self.auth)
        is_authorized = True if whoami.status_code == 200 else False

        if not is_authorized:
            logging.info('CREATING TICKET')
            self.create_ticket()
            self.check_ticket()
        else:
            logging.info('I AM {}'.format(whoami.json()))

    def create_ticket(self):
        kinit = Popen(['/usr/bin/kinit', self.username], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        kinit.communicate(input=bytes(self.password + '\n', encoding='utf-8'))
        kinit.wait(timeout=3)


class ExplicitAuth(requests.auth.AuthBase):

    def __init__(self, login_with_realm: str):
        self.login_with_realm = login_with_realm

    def __call__(self, request: requests.PreparedRequest) -> requests.PreparedRequest:
        request.headers['Authorization'] = 'Explicit {}'.format(self.login_with_realm)
        return request
