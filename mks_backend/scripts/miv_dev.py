from os import path
import argparse

from dotenv import load_dotenv

from mks_backend.entities.miv.repository import MIVRepository


def register():
    print(MIVRepository().register_endpoint())


def send():
    print(MIVRepository().send_message({'meta': {'foo': 'bar'}}, 'mks@int.aorti.tech'))


if __name__ == '__main__':
    load_dotenv(path.join(path.realpath(path.dirname(__file__)), '.env'))
    parser = argparse.ArgumentParser()
    parser.add_argument('action')
    args = parser.parse_args()

    if args.action == 'send':
        send()
    elif args.action == 'register':
        register()
