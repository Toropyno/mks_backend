from os import environ

from mks_backend.session import DBSession


def tween_factory(handler, registry):
    """
    Фабрика для производства tween
    https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/hooks.html#registering-tweens
    """
    def rewrite_KRB5CCNAME_in_environ(request):
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

    return rewrite_KRB5CCNAME_in_environ
