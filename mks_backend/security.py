from pyramid.security import Allowed, Denied

from mks_backend.user import UserService


class SecurityPolicy:

    def effective_principals(self, request):
        service = UserService()
        permissions = service.get_permissions()
        return [permission for permission in permissions.keys() if permissions[permission]]

    def permits(self, request, context, permission):
        if any(perm in permission for perm in context):
            return Allowed
        else:
            return Denied('Операция не позволена')
