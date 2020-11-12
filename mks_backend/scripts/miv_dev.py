from os import environ
import argparse

from mks_backend.repositories.miv.miv import MIVRepository


environ['MIV_USER'] = ''
environ['MIV_USER_PASSWORD'] = ''
environ['MIV_REGISTER_URL'] = 'http://1krn-balancer01.int.aorti.tech:8860/public/api/1.0/account_endpoint/'
environ['MIV_SEND_URL'] = 'http://1krn-balancer01.int.aorti.tech:8860/public/api/1.0/message/receive/'
environ['MIV_WHOAMI_URL'] = 'http://1krn-balancer01.int.aorti.tech:8860/public/api/1.0/whoami/'


def register():
    print(MIVRepository().register_endpoint())


def send():
    print(MIVRepository().send_message({'meta': {'foo': 'bar'}}, 'mks@int.aorti.tech'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action')
    args = parser.parse_args()

    if args.action == 'send':
        send()
    elif args.action == 'register':
        register()
