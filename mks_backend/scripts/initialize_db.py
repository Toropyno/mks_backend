import os
import sys


# Do not delete import models
from mks_backend.models import Base, DBSession

from mks_backend.models.protocols.protocol import Protocol
from mks_backend.models.filestorage import Filestorage
from mks_backend.models.protocols.meeting import Meeting

from mks_backend.models.commission import Commission
from mks_backend.models.construction import Construction
from mks_backend.models.construction_category import ConstructionCategory
from mks_backend.models.construction_object import ConstructionObject
from mks_backend.models.construction_stage import ConstructionStage
from mks_backend.models.construction_subcategory import ConstructionSubcategory
from mks_backend.models.military_unit.military_unit import MilitaryUnit
from mks_backend.models.object_category import ObjectCategory
from mks_backend.models.object_category_list import ObjectCategoryList
from mks_backend.models.subcategory_list import SubcategoryList
from mks_backend.models.zone import Zone
from mks_backend.models.construction_company import ConstructionCompany
from mks_backend.models.oksm import OKSM
from mks_backend.models.construction_type import ConstructionType
from mks_backend.models.realty_type import RealtyType
from mks_backend.models.work_list.work_type import WorkType
from mks_backend.models.work_list.work_list import WorkList

from mks_backend.models.military_unit.combatarm import Combatarm
from mks_backend.models.military_unit.keyword import Keyword
from mks_backend.models.military_unit.militarycity import MilitaryCity
from mks_backend.models.military_unit.namemilitaryunit import NameMilitaryUnit
from mks_backend.models.military_unit.purposemu import PurposeMU
from mks_backend.models.military_unit.sortarmedforces import SortArmedForces

from mks_backend.models.coordinate import Coordinate
from mks_backend.models.location_type import LocationType

from mks_backend.models.documents.object_document import ObjectDocument
from mks_backend.models.documents.construction_document import ConstructionDocument
from mks_backend.models.documents.doc_type import DocType

from mks_backend.models.construction_progress import ConstructionProgress
from mks_backend.models.progress_status import ProgressStatus
from mks_backend.models.work_list.measure_unit import MeasureUnit
from mks_backend.models.object_file import ObjectFile
from mks_backend.models.trips.work_trip import WorkTrip
from mks_backend.models.trips.leadership_position import LeadershipPosition
from mks_backend.models.trips.visited_object import VisitedObject
from mks_backend.models.contract_status import ContractStatus
from mks_backend.models.work_list.element_type import ElementType
from mks_backend.models.inspections.inspection import Inspection

from mks_backend.models.organizations.organization import Organization
from mks_backend.models.organizations.organization_history import OrganizationHistory
from mks_backend.models.documents.organization_document import OrganizationDocument


from mks_backend.models import Base, DBSession
from pyramid.paster import get_appsettings, setup_logging
from sqlalchemy import engine_from_config


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
