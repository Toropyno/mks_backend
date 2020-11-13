import argparse

from mks_backend.env_vars import setup_env_vars

from mks_backend.repositories.miv.miv import MIVRepository


def register():
    print(MIVRepository().register_endpoint())


def send():
    print(MIVRepository().send_message({'meta': {'foo': 'bar'}}, 'mks@int.aorti.tech'))


if __name__ == '__main__':
    setup_env_vars()
    parser = argparse.ArgumentParser()
    parser.add_argument('action')
    args = parser.parse_args()

    if args.action == 'send':
        send()
    elif args.action == 'register':
        register()
