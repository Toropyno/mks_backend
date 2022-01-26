import logging
from os import environ

from pyramid.authentication import extract_http_basic_credentials
from pyramid.httpexceptions import HTTPUnauthorized

from mks_backend.session import DBSession
from mks_backend.settings import SETTINGS

logger = logging.getLogger(__name__)


def tween_factory(handler, registry):
    """
    Фабрика для производства tween
    https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/hooks.html#registering-tweens
    """
    def reconfigure_session_and_set_env_vars(request):

        if SETTINGS['AUTH_TYPE'] == 'kerberos':
            set_env_vars_for_kerberos(request)
        elif SETTINGS['AUTH_TYPE'] == 'explicit':
            set_env_vars_for_explicit(request)
        else:
            raise ValueError('Не установлен AUTH_TYPE в конфигурационном файле')

        # Переписываем значение KRB5CCNAME в окружении на тот, что пришёл с реквестом
        # Так же, записываем имя пришедшего пользователя, чтобы упростить к нему доступ
        if 'KRB5CCNAME' in request.environ.keys():
            environ['KRB5CCNAME'] = request.environ['KRB5CCNAME']
            environ['REMOTE_USER'] = request.environ['REMOTE_USER'].split('@')[0]

        # обрабатываем входящий request нашим приложением
        response = handler(request)

        # закрываем сессию после обработки запроса
        DBSession.remove()
        return response

    def set_env_vars_for_kerberos(request):
        """
        Пишем в переменные окружения следующие значения:
            KRB5CCNAME - путь к kerberos-тикету в файловой системе
            REMOTE_USER - текущий пользователь без REALM, например kvdv01, а не kvdv01@int.aorti.tech

        Опционально:
            Если это МИВ отправляет нам сообщения
            HTTP_KRN_SENDER - имя отправителя сообщения, без REALM
            HTTP_KRN_RECIPIENT - имя получателя сообщения (на одной машине может быть зарегистрировано несколько)
        """
        # Переписываем значение KRB5CCNAME в окружении на тот, что пришёл с реквестом
        environ['KRB5CCNAME'] = request.environ['KRB5CCNAME']

        # Записываем значение username текущего пользователя в переменные окружения, для упрощения доступа
        remote_username = request.environ['REMOTE_USER'].split('@')[0]
        environ['REMOTE_USER'] = remote_username

        if (request.method == 'POST') and ('kraken' in remote_username):
            # МИВ отправил нам сообщение, сохраним имя отправителя и получателя
            environ['HTTP_KRN_SENDER'] = request.headers.environ.get('HTTP_KRN_SENDER').split('@')[0]
            environ['HTTP_KRN_RECIPIENT'] = request.headers.environ.get('HTTP_KRN_RECIPIENT').split('@')[0]
            environ['HTTP_KRN_UID'] = request.headers.environ.get('HTTP_KRN_UID')

    def set_env_vars_for_explicit(request):
        """
        Пишем в переменные окружения следующие значения:
            REMOTE_USER - текущий пользователь без REALM, например kvdv01, а не kvdv01@dev.aorti.tech
            Чтобы получить его, запросы должны содержать заголовок Authorization c типом Basic,
            например Authorization: Basic a3ZkdjAxOjMwMjI1MU1q

            Такой сценарий используется при локальной разработке
        """
        try:
            username, _ = extract_http_basic_credentials(request)
        except TypeError:
            raise HTTPUnauthorized(json_body={'message': 'Заголовок Authorization пуст. Кто вы?'})
        environ['REMOTE_USER'] = username

    return reconfigure_session_and_set_env_vars
