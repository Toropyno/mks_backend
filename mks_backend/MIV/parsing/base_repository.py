from mks_backend.session import DBSession, Base


class BaseRepository:

    def __init__(self, model, session=DBSession):
        self.model = model
        self.session = session
        self.query = self.session.query(model)

    def get_all(self) -> list:
        return self.query.all()

    def get_by_field(self, field, value):
        return self.query.filter(field == value)

    def get_by_fields(self, **kwargs):
        return self.query.filter_by(**kwargs)

    def get_or_create(self, field, value) -> Base:
        """
        Возвращает объект по значению поля, или возвращает новый инстанс
        """
        if not value:
            return None

        instance = self.get_by_field(field, value).first()
        if not instance:
            instance = self.create_instance(field, value)

        return instance

    def create_instance(self, field, value):
        instance = self.model()
        setattr(instance, field.key, value)

        self.add_to_session(instance)
        return instance

    def add_to_session(self, instance):
        self.session.add(instance)
