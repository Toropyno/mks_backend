import sys

from mks_backend.session import Base, get_engine_by_uri
from mks_backend.models import *


def clean_db(config_uri=sys.argv[-1]):
    engine = get_engine_by_uri(config_uri)
    for tbl in reversed(Base.metadata.sorted_tables):
        engine.execute(tbl.delete())
