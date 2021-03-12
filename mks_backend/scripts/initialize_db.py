import os
import sys

from pyramid.paster import get_appsettings, setup_logging

from sqlalchemy import engine_from_config
from sqlalchemy.schema import CreateSchema
from sqlalchemy.engine import Engine

from mks_backend.session import Base, DBSession
from mks_backend.db_schemas import SCHEMAS
from mks_backend.models import *


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    create_schemas(engine)
    Base.metadata.create_all(engine)


def create_schemas(engine: Engine) -> None:
    for schema in SCHEMAS:
        if not engine.dialect.has_schema(engine, schema):
            engine.execute(CreateSchema(schema))
