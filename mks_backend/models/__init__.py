from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.schema import MetaData
from sqlalchemy import event


# for alembic revision autogeneration
# NAMING_CONVENTION = {
#     "ix": "ix_%(column_0_label)s",
#     "uq": "uq_%(table_name)s_%(column_0_name)s",
#     "ck": "ck_%(table_name)s_%(constraint_name)s",
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
#     "pk": "pk_%(table_name)s"
# }
#
# metadata = MetaData(naming_convention=NAMING_CONVENTION)
# Base = declarative_base(metadata=metadata)

Base = declarative_base()
DBSession = scoped_session(sessionmaker())


@event.listens_for(DBSession, 'after_commit')
def receive_after_commit(session):
    print('Transaction was successful.')
