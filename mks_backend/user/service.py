from pyramid.threadlocal import get_current_request

from mks_backend.SVIP.SVIP import SVIP


class UserService:

    def __init__(self):
        self.SVIP = SVIP()

    @property
    def current_username_with_realm(self) -> str:
        request = get_current_request()
        username = request.environ.get('REMOTE_USER')
        return username

    def get_permissions(self) -> dict:
        return self.SVIP.get_permissions(self.current_username_with_realm.lower())
