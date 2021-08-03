from pyramid.config import Configurator

from mks_backend.security import SecurityPolicy
from mks_backend.controllers.trips.routes import include_trips
from mks_backend.controllers.protocols.routes import include_protocols
from mks_backend.controllers.inspections.routes import include_inspections
from mks_backend.controllers.work_list.routes import include_work_list
from mks_backend.controllers.organizations.routes import include_organizations
from mks_backend.controllers.state_contracts.routes import include_state_contracts
from mks_backend.controllers.miv.routes import include_miv
from mks_backend.routes import includeme
from mks_backend._loggers.routes import include_logs


def main(global_config, **settings):
    config = Configurator(settings=settings)

    config.set_authentication_policy(SecurityPolicy())
    config.set_authorization_policy(SecurityPolicy())

    config.include(includeme)
    config.include(include_trips)
    config.include(include_protocols)
    config.include(include_inspections)
    config.include(include_work_list)
    config.include(include_organizations)
    config.include(include_state_contracts)
    config.include(include_miv)
    config.include(include_logs)

    # хуки, которые срабатывает до начала обработки request нашим приложением и после
    config.add_tween('mks_backend.tweens.tween_factory')

    config.scan()
    return config.make_wsgi_app()
