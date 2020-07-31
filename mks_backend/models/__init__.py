from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import event


Base = declarative_base()
DBSession = scoped_session(sessionmaker())


@event.listens_for(DBSession, 'after_commit')
def receive_after_commit(session):
    print('Transaction was successful.')
