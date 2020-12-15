from pyramid.view import view_config

from .loger import DBErrorLogger


class DBErrorController:

    def __init__(self, request):
        self.request = request
        self.service = DBErrorLogger()

    @view_config(route_name='get_db_errors', renderer='json')
    def get_db_errors(self):
        return self.service.get_db_errors()
