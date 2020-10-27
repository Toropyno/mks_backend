from sqlalchemy import event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


Base = declarative_base()
DBSession = scoped_session(sessionmaker())


@event.listens_for(DBSession, 'after_commit')
def receive_after_commit(session):
    print('Transaction was successful.')
