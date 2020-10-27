from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from mks_backend.models import DBSession, Base

from mks_backend.routes import includeme
from mks_backend.controllers.trips.routes import include_trips
from mks_backend.controllers.protocols.routes import include_protocols
from mks_backend.controllers.inspections.routes import include_inspections
from mks_backend.controllers.work_list.routes import include_work_list


def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include(includeme)
    config.include(include_trips)
    config.include(include_protocols)
    config.include(include_inspections)
    config.include(include_work_list)
    config.scan()
    return config.make_wsgi_app()
