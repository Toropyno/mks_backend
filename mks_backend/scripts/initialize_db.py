# Do not delete import models
from mks_backend.models import Base

from mks_backend.models.protocol import Protocol
from mks_backend.models.filestorage import Filestorage
from mks_backend.models.meeting import Meeting

from mks_backend.models.commission import Commission
from mks_backend.models.construction import Construction
from mks_backend.models.construction_category import ConstructionCategory
from mks_backend.models.construction_object import ConstructionObject
from mks_backend.models.construction_stage import ConstructionStage
from mks_backend.models.construction_subcategory import ConstructionSubcategory
from mks_backend.models.military_unit import MilitaryUnit
from mks_backend.models.object_category import ObjectCategory
from mks_backend.models.object_category_list import ObjectCategoryList
from mks_backend.models.subcategory_list import SubcategoryList
from mks_backend.models.zone import Zone
from mks_backend.models.construction_company import ConstructionCompany
from mks_backend.models.oksm import OKSM
from mks_backend.models.construction_type import ConstructionType
from mks_backend.models.realty_type import RealtyType
from mks_backend.models.work_type import WorkType

from mks_backend.models.military_unit_models.combatarm import Combatarm
from mks_backend.models.military_unit_models.keyword import Keyword
from mks_backend.models.military_unit_models.militarycity import MilitaryCity
from mks_backend.models.military_unit_models.namemilitaryunit import NameMilitaryUnit
from mks_backend.models.military_unit_models.purposemu import PurposeMU
from mks_backend.models.military_unit_models.sortarmedforces import SortArmedForces

from mks_backend.models.coordinate import Coordinate
from mks_backend.models.location_type import LocationType

from mks_backend.models.documents.object_document import ObjectDocument
from mks_backend.models.documents.construction_document import ConstructionDocument
from mks_backend.models.documents.doc_type import DocType

from mks_backend.models.construction_progress import ConstructionProgress
from mks_backend.models.measure_unit import MeasureUnit

from mks_backend.models.object_file import ObjectFile

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
