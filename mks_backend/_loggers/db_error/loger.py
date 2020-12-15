from datetime import datetime, timedelta as time_d

from sqlalchemy import desc

from .model import DBError
from mks_backend.models import DBSession


class DBErrorLogger:

    def __init__(self):
        self._query = DBSession.query(DBError)

    def log(self, error_raw: str) -> None:
        DBSession.add(DBError(error_raw=error_raw))
        DBSession.commit()

    def get_db_errors(self, timedelta=time_d(minutes=10)):
        return self._query.filter(
            DBError.time >= (datetime.now() - timedelta)
        ).order_by(desc(DBError.time)).all()
