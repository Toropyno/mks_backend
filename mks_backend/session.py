from os import environ

from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, scoped_session

from mks_backend.settings import SETTINGS


class SessionFactory(Session):

    def __init__(self) -> None:
        super().__init__(autoflush=False)
        self.url = self._url
        self.bind = self._engine

    @property
    def _url(self) -> str:
        """
        URL для подключения к БД

        Если нет заголовка REMOTE_USER, то подставляет дефолтный логин:пароль
        Если такой заголовок есть, подставляем только логин,
        и подключение к БД происходит через kerberos, посредством KRB5CCNAME,
        который мы положили в окружение в tweens.py
        """
        if SETTINGS['AUTH_TYPE'] == 'explicit':
            current_user = SETTINGS['DATABASE_USER'] + ':' + SETTINGS['DATABASE_PASSWORD']
        else:
            current_user = environ.get('REMOTE_USER') or SETTINGS['DATABASE_USER']

        url = 'postgresql://{user}@{host}:{port}/{dbname}'.format(
            user=current_user,
            host=SETTINGS['DATABASE_HOST'],
            port=SETTINGS['DATABASE_PORT'],
            dbname=SETTINGS['DATABASE_NAME']
        )
        return url

    @property
    def _engine(self) -> Engine:
        """
        Движок подключения к БД
        """
        return create_engine(self.url)


Base = declarative_base()
DBSession = scoped_session(SessionFactory)
