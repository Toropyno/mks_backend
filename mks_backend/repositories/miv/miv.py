import json
from typing import Tuple
from os import environ
from subprocess import Popen, PIPE

import requests
from kerberos import GSSError
from requests_toolbelt import MultipartEncoder
from requests_kerberos import HTTPKerberosAuth


class MIVRepository:
    """
    Interacts with MIV programming complex.
    Before sending a message, checks if kerberos_ticket is available.
    If no ticket is available, it automatically creates one.
    """
    def __init__(self):
        self.user = environ.get('MIV_USER', 'Elliot Alderson')
        self.password = environ.get('MIV_USER_PASSWORD')

        self.register_url = environ.get('MIV_REGISTER_URL')
        self.send_url = environ.get('MIV_SEND_URL')
        self.whoami_url = environ.get('MIV_WHOAMI_URL')

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
        self.check_ticket()

        register_data = MultipartEncoder(fields={
            'receive': 'http://1mks03.int.aorti.tech/api/miv/message/receive/',
            'notify': 'http://1mks03.int.aorti.tech/api/miv/message/notify/',
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
        self.check_ticket()

        send_data = dict()
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