from typing import List

import requests

from mks_backend.auth import Authorization


class SVIPRepository:
    TIMEOUT = 5

    def __init__(self):
        self.auth_service = Authorization()

    def custom_get(self, url: str, params=None) -> dict:
        response = requests.get(url=url, auth=self.auth_service.auth, timeout=self.TIMEOUT, params=params)
        if not response.ok:
            raise ValueError(response.text)
        return response.json()

    def custom_post(self, url: str, json_data) -> dict:
        response = requests.post(url=url, auth=self.auth_service.auth, timeout=self.TIMEOUT, json=json_data)
        if not response.ok:
            raise ValueError(response.text)
        return response.json()

    def custom_delete(self, url: str) -> None:
        response = requests.delete(url=url, auth=self.auth_service.auth, timeout=self.TIMEOUT)
        if not response.ok:
            raise ValueError(response.text)

    def get_from_all_pages(self, url: str, page: int = 1) -> List[dict]:
        data = []
        while page is not None:
            response = self.custom_get(url=url, params={'page_size': 100, 'page': page})
            page = response['pagination']['next_page']
            data += response['data']

        return data
