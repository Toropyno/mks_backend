from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


Base = declarative_base()
DBSession = scoped_session(sessionmaker())

ORGANIZATION_SCHEMA = 'organization'
