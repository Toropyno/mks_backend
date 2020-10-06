from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from mks_backend.models import DBSession, Base

from mks_backend.routes import includeme
from mks_backend.controllers.trips.routes import include_trips


def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include(includeme)
    config.include(include_trips)
    config.scan()
    return config.make_wsgi_app()
