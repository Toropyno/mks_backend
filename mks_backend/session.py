from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import engine_from_config, create_engine

from pyramid.paster import get_appsettings, setup_logging

from mks_backend.settings import SETTINGS


def bind_session(engine):
    DBSession.configure(bind=engine)


def get_engine_by_uri(config_uri):
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    return engine_from_config(settings, 'sqlalchemy.')


Base = declarative_base()
DBSession = scoped_session(sessionmaker())

engine = create_engine(SETTINGS['sqlalchemy.url'])
DBSession.configure(bind=engine)
Base.metadata.bind = engine
