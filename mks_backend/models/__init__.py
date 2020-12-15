from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()
DBSession = scoped_session(sessionmaker())

ORGANIZATION_SCHEMA = 'organization'
STATE_CONTRACT_SCHEMA = 'state_contract'

MIV_SCHEMA = 'miv'
LOG_SCHEMA = 'logs'

SCHEMAS = (
    ORGANIZATION_SCHEMA,
    STATE_CONTRACT_SCHEMA,

    MIV_SCHEMA,
    LOG_SCHEMA
)
