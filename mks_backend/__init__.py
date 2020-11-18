from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from mks_backend.models import DBSession, Base
from mks_backend.controllers.trips.routes import include_trips
from mks_backend.controllers.protocols.routes import include_protocols
from mks_backend.controllers.inspections.routes import include_inspections
from mks_backend.controllers.work_list.routes import include_work_list
from mks_backend.controllers.organizations.routes import include_organizations
from mks_backend.controllers.state_contracts.routes import include_state_contracts
from mks_backend.controllers.miv.routes import include_miv
from mks_backend.routes import includeme

from mks_backend.env_vars import setup_env_vars


def main(global_config, **settings):
    setup_env_vars()
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include(includeme)
    config.include(include_trips)
    config.include(include_protocols)
    config.include(include_inspections)
    config.include(include_work_list)
    config.include(include_organizations)
    config.include(include_state_contracts)
    config.include(include_miv)
    config.scan()
    return config.make_wsgi_app()
