import json
from subprocess import PIPE, Popen

import requests
from kerberos import GSSError
from requests_kerberos import HTTPKerberosAuth
from requests_toolbelt import MultipartEncoder

from mks_backend.settings import SETTINGS


class MIVRepository:
    """
    Interacts with MIV programming complex.
    Before sending a message, checks if kerberos_ticket is available.
    If no ticket is available, it automatically creates one.
    """

    def __init__(self):
        self.host = SETTINGS['HTTP_HOST']

        self.user = SETTINGS['MIV_USER']
        self.password = SETTINGS['MIV_PASSWORD']

        self.register_url = SETTINGS['MIV_REGISTER_URL']
        self.send_url = SETTINGS['MIV_SEND_URL']
        self.whoami_url = SETTINGS['MIV_WHOAMI_URL']

    @property
    def kerberos_auth(self) -> HTTPKerberosAuth:
        try:
            auth = HTTPKerberosAuth()
        except GSSError:
            self.create_ticket()
            auth = HTTPKerberosAuth()
        return auth

    def register_endpoint(self) -> dict:
        """
        Register endpoint in MIV programming complex.
        """
        self.create_ticket()

        register_data = MultipartEncoder(fields={
            'receive': self.host + '/api/miv/message/receive/',
            'notify': self.host + '/api/miv/message/notify/',
        })

        register_request = requests.post(
            url=self.register_url,
            headers={
                'Content-Type': register_data.content_type,
            },
            auth=self.kerberos_auth,
            data=register_data.to_string(),
        )

        response = json.loads(register_request.text)
        response['status_code'] = register_request.status_code
        return response

    def send_message(self, message: dict, recipient: str) -> dict:
        """
        Send message to MIV programming complex.
        Before that, checking if kerberos ticket available
        """
        self.create_ticket()

        send_data = {}
        if 'meta' in message:
            send_data['meta'] = (None, json.dumps(message['meta'], ensure_ascii=False), 'application/json')
        if 'payload' in message:
            send_data['payload'] = (None, open(message['payload'], 'rb'), 'application/octet-stream')

        multiparted = MultipartEncoder(fields=send_data)

        send_request = requests.post(
            url=self.send_url,
            headers={
                'KRN-RECIPIENT': recipient,
                'Content-Type': multiparted.content_type,
            },
            data=multiparted.to_string(),
            auth=self.kerberos_auth
        )

        response = json.loads(send_request.text)
        response['status_code'] = send_request.status_code
        return response

    def check_ticket(self):
        whoami = requests.get(self.whoami_url, auth=self.kerberos_auth)
        is_authorized = True if whoami.status_code == 200 else False

        if not is_authorized:
            self.create_ticket()

    def create_ticket(self):
        kinit = Popen(['/usr/bin/kinit', self.user], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        kinit.communicate(input=bytes(self.password + '\n', encoding='utf-8'))
        kinit.wait(timeout=3)
