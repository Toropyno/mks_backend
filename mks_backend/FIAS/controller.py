from pyramid.request import Request
from pyramid.view import view_config, view_defaults

from .service import FIASService


@view_defaults(renderer='json')
class FIASController:

    def __init__(self, request: Request):
        self.request = request
        self.service = FIASService()

    @view_config(route_name='get_all_fiases_for_filtration')
    def get_all_construction_companies(self):
        """
        return all regions, areas, cities, settlements fir filtration
        """
        return []
