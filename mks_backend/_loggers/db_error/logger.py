from datetime import datetime
from datetime import timedelta as time_d

from sqlalchemy import desc

from mks_backend.session import DBSession

from .model import DBError


class DBErrorLogger:

    def __init__(self):
        self._query = DBSession.query(DBError)

    def log(self, error_raw: str) -> None:
        DBSession.add(DBError(error_raw=error_raw))
        DBSession.commit()

    def get_db_errors(self, timedelta=None):
        timedelta = timedelta or time_d(minutes=10)
        return self._query.filter(
            DBError.time >= (datetime.now() - timedelta)
        ).order_by(desc(DBError.time)).all()
