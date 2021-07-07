from subprocess import Popen, PIPE

import requests
from requests_kerberos import HTTPKerberosAuth

from mks_backend.settings import AUTH_TYPE, MKS_USER, KRB_AUTH_REALM


class Authorization:

    def __init__(self):
        self.auth = self._auth

    @property
    def _auth(self):
        if AUTH_TYPE == 'kerberos':
            return HTTPKerberosAuth()
        elif AUTH_TYPE == 'explicit':
            return ExplicitAuth('{username}@{realm}'.format(username=MKS_USER, realm=KRB_AUTH_REALM))

    @classmethod
    def create_ticket(cls, username: str, password: str) -> None:
        """
        Создаёт kerberos ticket для пользователя по логину и паролю
        Должен использоваться только для скриптов, например, для первоначального наполнения СВИП

        TODO: возможно в контуре главного конструктора такой трюк не пройдёт из-за того, что мы можем не знать пароль пользователя
        :param username: имя пользователя - владельца коллекции в СВИП
        :param password: пароль пользователя - владельца коллекции в СВИП
        :return:
        """
        kinit = Popen(['/usr/bin/kinit', username], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        kinit.communicate(input=bytes(password + '\n', encoding='utf-8'))
        kinit.wait(timeout=3)


class ExplicitAuth(requests.auth.AuthBase):

    def __init__(self, login_with_realm: str):
        self.login_with_realm = login_with_realm

    def __call__(self, request: requests.PreparedRequest) -> requests.PreparedRequest:
        request.headers['Authorization'] = 'Explicit {}'.format(self.login_with_realm)
        return request
