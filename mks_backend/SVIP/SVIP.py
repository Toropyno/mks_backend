from os import environ

from typing import List

from mks_backend.SVIP.custom_tools import CustomRequest
from mks_backend.auth import Authorization


class SVIP:

    def __init__(self):
        self.request = CustomRequest(Authorization(environ['SVIP_USER'], environ['SVIP_PASSWORD']))
        self.idm_set_url = environ['SVIP_HOST'] + 'idm/set/'

    @staticmethod
    def find_by_name(collection: List[dict], name: str) -> str:
        return next(elem['uid'] for elem in collection if elem['name'] == name)

    def get_set_uuid(self) -> str:
        """
        Получаем uuid набора по наименованию набора
        """
        try:
            sets = self.request.get_from_all_pages(self.idm_set_url)
            return self.find_by_name(sets, 'МКС')
        except StopIteration:
            return ''

    def get_permissions(self, username_with_realm: str) -> dict:
        permission_url = environ['SVIP_HOST'] \
                         + 'idm/' + self.get_set_uuid() \
                         + '/check_permission/?account_id=' \
                         + username_with_realm.lower()
        permission_data = self.request.get_from_all_pages(permission_url)

        return {
            element['function_name']: element['is_allow'] for element in permission_data
        }
