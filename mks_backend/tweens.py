from os import environ


def tween_factory(handler, registry):
    """
    Фабрика для производства tween
    https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/hooks.html#registering-tweens
    """
    def rewrite_KRB5CCNAME_in_environ(request):
        # Переписываем значение KRB5CCNAME в окружении на тот, что пришёл с реквестом
        if 'REMOTE_USER' in request.environ.keys():
            environ['KRB5CCNAME'] = request.environ['KRB5CCNAME']

        # обрабатываем входящий request нашим приложением
        response = handler(request)

        return response

    return rewrite_KRB5CCNAME_in_environ
