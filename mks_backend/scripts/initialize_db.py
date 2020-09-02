# Do not delete import models
from mks_backend.models import Base
from mks_backend.models.protocol import Protocol

from mks_backend.models.filestorage import Filestorage
from mks_backend.models.meeting import MeetingsType

from mks_backend.models.commission import Commission
from mks_backend.models.construction import Construction
from mks_backend.models.construction_categories import ConstructionCategories
from mks_backend.models.construction_objects import ConstructionObjects
from mks_backend.models.construction_stages import ConstructionStages
from mks_backend.models.construction_subcategories import ConstructionSubcategories
from mks_backend.models.military_unit import MilitaryUnit
from mks_backend.models.object_categories import ObjectCategories
from mks_backend.models.object_categories_list import ObjectCategoriesList
from mks_backend.models.subcategories_list import SubcategoriesList
from mks_backend.models.zones import Zones

from mks_backend.models.military_unit_models.combatarm import Combatarm
from mks_backend.models.military_unit_models.keyword import Keyword
from mks_backend.models.military_unit_models.militarycity import MilitaryCity
from mks_backend.models.military_unit_models.namemilitaryunit import NameMilitaryUnit
from mks_backend.models.military_unit_models.purposemu import PurposeMU
from mks_backend.models.military_unit_models.sortarmedforces import SortArmedForces

import os
import sys

from pyramid.paster import get_appsettings, setup_logging
from sqlalchemy import engine_from_config

from mks_backend.models import DBSession, Base


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
