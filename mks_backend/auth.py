from subprocess import PIPE, Popen

import requests
from requests_kerberos import HTTPKerberosAuth

from mks_backend.settings import SETTINGS


class Authorization:

    def __init__(self):
        self.auth_type = SETTINGS['AUTH_TYPE']
        self.auth = self._auth

    @property
    def _auth(self):
        if self.auth_type == 'kerberos':
            return HTTPKerberosAuth()
        elif self.auth_type == 'explicit':
            return ExplicitAuth()

    @classmethod
    def create_ticket(cls, username: str, password: str) -> None:
        """
        Создаёт kerberos ticket для пользователя по логину и паролю
        Должен использоваться только для скриптов, например, для первоначального наполнения СВИП

        TODO: возможно в контуре STG такой трюк не пройдёт из-за того, что мы можем не знать пароль пользователя
        :param username: имя пользователя - владельца коллекции в СВИП
        :param password: пароль пользователя - владельца коллекции в СВИП
        :return:
        """
        kinit = Popen(['/usr/bin/kinit', username], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        kinit.communicate(input=bytes(password + '\n', encoding='utf-8'))
        kinit.wait(timeout=3)


class ExplicitAuth(requests.auth.AuthBase):

    def __call__(self, request: requests.PreparedRequest) -> requests.PreparedRequest:
        request.headers['Authorization'] = 'Explicit {}@{}'.format(SETTINGS['MIO_USER'], SETTINGS['KRB_AUTH_REALM'])
        return request
