import sys
from pprint import pprint

from mks_backend.MIV.repository import MIVRepository


def register():
    response = MIVRepository().register_endpoint()
    pprint(response)


def send(recipient: str, path_to_file: str = None):
    message = {'meta': 'message for {}'.format(recipient)}

    if path_to_file:
        message['payload'] = path_to_file

    response = MIVRepository().send_message(message, recipient)
    pprint(response)


def main(args=sys.argv):
    if len(args) == 2 and args[1] == 'register':
        # miv register
        register()
    elif len(args) == 3 and args[1] == 'send':
        # miv send mks@int.aorti.tech
        send(args[2])
    elif len(args) == 4 and args[1] == 'send':
        # miv send mks@int.aorti.tech /path/to/file.txt
        send(args[2], args[3])
    else:
        print('Wrong command')
