import argparse
import logging

from pyramid.httpexceptions import HTTPForbidden

from mks_backend.auth import Authorization
from mks_backend.settings import SETTINGS
from mks_backend.SVIP import SVIP

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action')
    args = parser.parse_args()

    if SETTINGS['AUTH_TYPE'] == 'kerberos':
        # прежде всего, нужно создать kerberos-ticket для пользователя,
        # от чьего лица будет наполняться коллекция в СВИП
        Authorization.create_ticket(SETTINGS['MKS_USER'], SETTINGS['MKS_PASSWORD'])
    elif SETTINGS['AUTH_TYPE'] == 'explicit':
        pass

    if args.action == 'create':
        create_svip()
    elif args.action == 'delete':
        delete_svip()


def create_svip():
    service = SVIP()

    try:
        collection_uuid = service.get_set_uuid()
    except HTTPForbidden:
        # Обычно этот кейс возникает, когда пользователь не входит в коллекцию,
        # но если мы используем служебного пользователя,
        # то это может означать только то, что такой коллекции просто не существует
        logger.info('Создаём коллекцию {}'.format(service.COLLECTION_NAME))
        collection_uuid = service.create_set()
    else:
        logger.info('Коллекция "{}" уже существует, используется существующая'.format(service.COLLECTION_NAME))

    logger.info('Добавляем пользователей в коллекцию')
    service.add_users(collection_uuid)

    logger.info('Создаём разрешения')
    permissions = service.create_permissions(collection_uuid)

    logger.info('Привязываем пользователей к разрешениям')
    service.link_permissions_to_user(collection_uuid, permissions)


def delete_svip():
    service = SVIP()
    try:
        service.delete_collection()
    except HTTPForbidden:
        # Обычно этот кейс возникает, когда пользователь не входит в коллекцию,
        # но если мы используем служебного пользователя,
        # то это может означать только то, что такой коллекции просто не существует
        logger.info('Коллекция {} не существует'.format(service.COLLECTION_NAME))
    else:
        logger.info('Коллекция {} удалена'.format(service.COLLECTION_NAME))


if __name__ == '__main__':
    main()
