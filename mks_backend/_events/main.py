from sqlalchemy import event
from mks_backend.session import DBSession


@event.listens_for(DBSession, 'before_commit')
def receive_before_commit(session):
    if session.new:
        new_object = next(iter(session.new))
        print('Trying to ADD {} to DB'.format(new_object))
    elif session._deleted:
        for instance in session._deleted.values():
            print('Trying to DELETE {}'.format(instance))
    elif session.identity_map:
        edited_object = next(iter(session.identity_map._dict.keys()))[0]
        print('Trying to EDIT {} in DB'.format(edited_object))
    else:
        pass
        # print('Unknow event')


@event.listens_for(DBSession, 'after_commit')
def receive_after_commit(session):
    pass
    # print('Commit was successful.')
