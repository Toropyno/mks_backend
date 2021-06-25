import requests

from mks_backend.SVIP.attempt_decorator import try_again


class CustomRequest:
    TIMEOUT = 5

    def __init__(self, auth_service):
        self.auth_service = auth_service

    @try_again(code=200)
    def custom_get(self, url: str, params=None, msg: str = None):
        return requests.get(url, auth=self.auth_service.auth, timeout=self.TIMEOUT, params=params)

    @try_again(code=201)
    def custom_post(self, url: str, json_data, msg: str = None):
        return requests.post(url=url, auth=self.auth_service.auth, timeout=self.TIMEOUT, json=json_data)

    def get_from_all_pages(self, url: str):
        cur_page = 1
        sets = []
        while cur_page is not None:
            response = self.custom_get(url=url, params={'page_size': 100, 'page': cur_page}).json()
            cur_page = response['pagination']['next_page']
            data = response['data']
            sets = sets + data
        return sets
