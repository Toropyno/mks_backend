import json
import logging
from os import path
from typing import Optional, List

from mks_backend.SVIP.repository import SVIPRepository
from mks_backend.settings import SVIP_HOST, BASE_DIRECTORY, KRB_AUTH_REALM


class SVIP:
    COLLECTION_NAME = 'МКС'

    def __init__(self):
        self.repo = SVIPRepository()

    def get_set_uuid(self) -> str:
        """
        Получаем uuid набора по наименованию набора
        """
        sets_url = '{host}/idm/set/'.format(host=SVIP_HOST)
        sets = self.repo.get_from_all_pages(sets_url)
        try:
            return next(elem['uid'] for elem in sets if elem['name'] == self.COLLECTION_NAME)
        except StopIteration:
            raise ValueError('Такой коллекции разрешений нет в СВИП')

    def get_permissions(self, username_with_realm: str) -> dict:
        """
        Получаем словарь разрешений и их статусов.
        Ex.:
        {
            'access.isp_crud': True,
            'protocols_crud': False
        }
        """
        permission_url = '{host}/idm/{set_uuid}/check_permission/?account_id={username}'.format(
            host=SVIP_HOST,
            set_uuid=self.get_set_uuid(),
            username=username_with_realm
        )
        permission_data = self.repo.get_from_all_pages(permission_url)
        return {
            element['function_name']: element['is_allow'] for element in permission_data
        }

    def create_set(self) -> Optional[str]:
        """
        Создаёт коллекцию в СВИП, если она ещё не была создана

        :return: uuid коллекции
        """
        set_url = '{host}/idm/set/'.format(host=SVIP_HOST)
        response = self.repo.custom_post(url=set_url, json_data={'name': self.COLLECTION_NAME})

        collection_uuid = response['data']['uid']
        logging.info('Коллекция {} создана в СВИП uuid={}'.format(self.COLLECTION_NAME, collection_uuid))
        return collection_uuid

    def add_users(self, collection_uuid: str) -> None:
        """
        Добавляет пользователей в коллекцию СВИП без прав на редактирование

        :param collection_uuid: uuid коллекции
        :return:
        """
        path_to_accounts = path.join(BASE_DIRECTORY, 'SVIP/initial_data/accounts.json')
        with open(path_to_accounts) as f:
            accounts = json.load(f)

        url = '{host}/idm/{collection_uuid}/set_owner/'.format(host=SVIP_HOST, collection_uuid=collection_uuid)
        for account in accounts:
            json_data = {
                'set_id': collection_uuid,
                'owner_id': '{account}@{realm}'.format(account=account, realm=KRB_AUTH_REALM.lower()),
                'id_edit': False
            }
            self.repo.custom_post(url, json_data=json_data)

    def create_permissions(self, collection_uuid: str) -> List[str]:
        """
        Создаёт разрешения в СВИП

        :param collection_uuid: uuid коллекции
        :return: список из uuid созданных разрешений
        """
        path_to_permissions = path.join(BASE_DIRECTORY, 'SVIP/initial_data/permissions.json')
        with open(path_to_permissions) as f:
            permissions = json.load(f)

        permissions_uuid = []
        set_url = '{host}/idm/{collection_uuid}/permission/'.format(host=SVIP_HOST, collection_uuid=collection_uuid)
        for permission in permissions:
            response = self.repo.custom_post(url=set_url, json_data=permission)
            permissions_uuid.append(response['data']['uid'])

        return permissions_uuid

    def link_permissions_to_user(self, collection_uuid: str, permissions: List[str]) -> None:
        """
        Связывает пользователей и разрешения
        Минимальная реализация - одни могут всё, другие не могу ничего

        :param collection_uuid: uuid коллекции
        :param permissions: массив из uuid разрешений
        :return: None
        """
        path_to_accounts = path.join(BASE_DIRECTORY, 'SVIP/initial_data/account_permissions.json')
        with open(path_to_accounts) as f:
            accounts = json.load(f)

        url = '{host}/idm/{collection_uuid}/account_permission/'.format(host=SVIP_HOST, collection_uuid=collection_uuid)
        for permission in permissions:
            for account in accounts['accounts_with_all_permissions']:
                json_data = {
                    'account_id': '{account}@{realm}'.format(account=account, realm=KRB_AUTH_REALM.lower()),
                    'permission_id': permission,
                    'is_allow': True
                }
                self.repo.custom_post(url, json_data=json_data)

            for account in accounts['accounts_with_no_permissions']:
                json_data = {
                    'account_id': '{account}@{realm}'.format(account=account, realm=KRB_AUTH_REALM.lower()),
                    'permission_id': permission,
                    'is_allow': False
                }
                self.repo.custom_post(url, json_data=json_data)

    def delete_collection(self):
        """
        Находит коллекцию по имени COLLECTION_NAME и удаляет её из СВИП
        :return: None
        """
        collection_uuid = self.get_set_uuid()
        url = '{host}/idm/set/{collection_uuid}/'.format(host=SVIP_HOST, collection_uuid=collection_uuid)
        logging.info(url)
        self.repo.custom_delete(url)
