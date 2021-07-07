import argparse
import logging

from mks_backend.SVIP import SVIP
from mks_backend.auth import Authorization

from mks_backend.settings import MKS_USER, MKS_PASSWORD


logging.basicConfig(level=logging.INFO)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action')
    args = parser.parse_args()

    if args.action == 'create':
        create_svip()
    elif args.action == 'delete':
        delete_svip()


def create_svip():
    service = SVIP()

    # прежде, чем начнём, нужно создать kerberos-ticket для пользователя,
    # от чьего лица будет наполняться коллекция в СВИП
    Authorization.create_ticket(MKS_USER, MKS_PASSWORD)

    try:
        collection_uuid = service.get_set_uuid()
    except ValueError:
        logging.info('Создаём коллекцию {}'.format(service.COLLECTION_NAME))
        collection_uuid = service.create_set()
    else:
        logging.info('Коллекция "{}" уже существует, используется существующая'.format(service.COLLECTION_NAME))

    logging.info('Добавляем пользователей в коллекцию')
    service.add_users(collection_uuid)

    logging.info('Создаём разрешения')
    permissions = service.create_permissions(collection_uuid)

    logging.info('Привязываем пользователей к разрешениям')
    service.link_permissions_to_user(collection_uuid, permissions)


def delete_svip():
    service = SVIP()

    Authorization.create_ticket(MKS_USER, MKS_PASSWORD)
    service.delete_collection()
    logging.info('Коллекция {} удалена'.format(service.COLLECTION_NAME))


if __name__ == '__main__':
    main()
