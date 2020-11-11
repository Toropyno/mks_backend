from sqlalchemy import event
from mks_backend.models import DBSession


@event.listens_for(DBSession, 'after_commit')
def receive_after_commit(session):
    print('Transaction was successful.')
