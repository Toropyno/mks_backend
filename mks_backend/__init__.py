from pyramid.config import Configurator

from mks_backend.routes import ROUTES
from mks_backend.security import SecurityPolicy


def main(global_config, **settings):
    config = Configurator(settings=settings)

    config.set_authentication_policy(SecurityPolicy())
    config.set_authorization_policy(SecurityPolicy())

    # Подключаем наши роуты
    for route in ROUTES:
        config.include(route)

    # хуки, которые срабатывает до начала обработки request нашим приложением и после
    config.add_tween('mks_backend.tweens.tween_factory')

    config.scan()
    return config.make_wsgi_app()
